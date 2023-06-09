'''Importing all the necessary libraries'''
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD


'''Creating the lemmatizer'''
lemmatizer = WordNetLemmatizer()

with open('intents.json', "r", encoding='utf-8') as swish_questions:
    intents = json.loads(swish_questions.read(), strict=False)


words = []
classes = []
documents = []

ignore_letters = ['?','!','.',',']

for intent in intents['intents']:
    for i in range(0,47):
        for pattern in intents['intents'][i]['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intents['intents'][i]['tag']))
            if intents['intents'][i]['tag'] not in classes:
                classes.append(intent['tag'])

# print(documents)

words = [nltk.stem.WordNetLemmatizer().lemmatize(word) 
         for word in words if word not in ignore_letters]

words = sorted(set(words))
# print(words)
classes = sorted(set(classes))

pickle.dump(words,open('words.pk1','wb'))
pickle.dump(classes,open('classes.pk1','wb'))


'''Configuring the neural network by vectorizing word inputs in a bag of words model'''

training = []
output_empty = [0] * len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)


train_x = list(training[:,0])
train_y = list(training[:,1])

'''Creating the neural network'''

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x),np.array(train_y), 
                 epochs=200, batch_size=5, verbose=1)

model.save('Swish V1.model', hist)

print('Swish V1 has completed training')
