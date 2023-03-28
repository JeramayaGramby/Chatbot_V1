<br>

## This README file includes:

-An overview of what Swish V1 does<br>
-Swish V1's use cases<br>
-Swish V1's underlying components<br>
-The scalability of Swish V1 and how to scale Swish V1<br>
-The limitations of Swish V1 and plans for Swish V2<br>
-The list of questions the user can ask Swish<br>
-Swish V1's language briefing for the user<br>
-Project photo<br><br>


## Overview of Swish V1

Swish V1 is a 'fanbot' that utilizes shallow NLP methods in combination with a trained 
neural network to answer the most common trivia questions surrounding the Golden State Warriors basketball team.<br><br>
This chatbot is designed to educate curious new fans of the Golden State Warriors who want to understand the
team and can provide answers for trivia questions.<br><br>

## Use Cases for Swish V1:

New or younger Warriors fans are commonly referred to as 'bandwagon' fans by NBA fans because of their perceived
lack of knowledge concerning Golden State's history. In my experience Warriors fans are criticized on their amount of
knowledge on team history, player accomplishments and team trivia more than any other NBA fan.

As a person who has been on the receiving end of many 'bandwagon' allegations and has had to prove
qualifications many times, Swish V1 is the one-stop shop aiming to solve this dilemma.
With just a few keywords a brand-new Warriors fan can find out when and where Draymond Green was drafted,
the names and legacy behind the Warriors 'Run-TMC' trio and even find out where Steph Curry ranks all time for
points scored in his career.<br><br>

## Swish V1's underlying components:

The core functionality of the chatbot goes something like this: A JSON file ('intents.json') contains all the
questions and related questions to a given topic in Warriors Trivia (example: Stephen Curry's draft position) in
combination with an answer or list of answers. This feeds the 200 iterations of the 128 layer deep neural network.

This is how the data gets processed: The JSON data is lemmatized and then serialized into a pickle file.
Any duplicate data created is removed through a 'set' function. <br><br>Once the data is 'pickled' it is then 
put into a 'Bag-of-Words' model. This model vectorizes the data by measuring the frequency of each word 
in each sentence. It helps the neural network determine the topic of a sentence. 
The training data is then shuffled and the Sequential ML model is created. <br><br>The model spans 200 epochs, 
128 layers and a batch size of 5. After the model is created it is saved as a h5 file. For the chatbot file, 
the pickle and model file data is loaded. 4 functions are then used to convert the numerical data created 
from the model file, predict what the words are and test user input against the model.<br><br>


## Scalability of Swish V1

Swish V1 can be scaled in multiple ways. The JSON file could be manually expanded out or 
expanded out with a script. This model is also very well-equipped to receive JSON data from an API. 
This could be an API that I create with Golden State Warrior's trivia information or NBA Trivia information. 
Other APIs currently exist that have most of the trivia data needed.<br><br> It could also utilize JSON data from 
search APIs to expand the question base (which may require a name change from Swish V1). 
The limit to the size of the JSON file (and potential of the model) is limited to the processing 
capabilities of the user's hardware.<br><br>

##                                The limitations of Swish V1 & plans for Swish V2

Swish V1 has many foundational limitations. As of 12/19/2022 Swish V1 is only compatible with Python 3.10 
or older because Tensorflow 2.10 is not yet equipped for Python 3.11. <br><br>Because of varying hardware limitations for
each user Swish V1's model is only functional on Google Colab. While the training and model are functional,
the two-way communication aspect of Swish V1 is currently not functional on Google Colab.

It uses shallow NLP methods that are less reliable with larger amounts of user input like paragraphs.
The word 'next' CANNOT be used in a question. The user can use sentences to communicate with Swish V1, 
but it is highly encouraged that the user uses targeted keywords rather than sentences for a higher probability 
of matching the question to the correct answer. <br><br>In terms of my plans for Swish V2 I am uncertain whether I want 
to utilize API data with a larger variety of trivia answers related to just the Warriors or if I should expand the list of answerable basketball questions.<br><br>

                    
## Current list of answerable questions
-What is Stephen Curry's total amount of points/How many points has Steph Curry Scored?<br>
-Where is Golden State's current location?<br>
-Where were the Golden State Warriors originally located?<br>
-What year did the Warriors win their first championship?<br>
-When was steph curry drafted<br>
-when was klay thompson drafted<br>
-when was draymond green drafted<br>
-When was chris webber drafted<br>
-When was Jason Richardson drafted<br>
-When was Harrison Barnes drafted<br>
-When was Monta Ellis drafted<br>
-When was Gilbert Arenas drafted<br>
-When was Vince Carter drafted<br>
-Were Penny Hardaway and Vince Carter drafted by the Warriors<br>
-When was Chris Mullin Drafted<br>
-When was Mitch Ritchmond drafted<br>
-How many years/how long did Wilt Chamberlain play for the Warriors<br>
-How many years/how long did Kevin Durant play for the Warriors<br>
-How many years/how long did Chris Webber play for the Warriors<br>
-How many years/how long did Latrell Sprewell play for the Warriors<br>
-How many years/how long did Tim Hardaway play for the Warriors<br>
-How many years/how long did Rick Barry play for the Warriors<br>
-What is the Warriors highest draft pick/Did the Warriors ever have the #1 overall draft pick?<br>
-How many rings does Steph have?<br>
-How many rings does Klay have?<br>
-How many rings does Kevin Durant have?/klay rings<br>
-How many championships do the warriors have/warriors total championships<br>
-Have the Golden State Warriors gone by any other names?<br>
-What division do the Golden State Warriors play in?<br>
-Which Warrior holds the NBA record for most 3-pointers in a game?<br>
-What is the best regular season record?<br>
-What is the best postseason record<br>
-Who is Golden State's biggest rival?<br>
-What was the first jersey number retired by the Golden State Warriors?<br>
-Who is the shortest player in Warriors' history?<br>
-Who is the tallest player in Warrior's history?<br>
-Who are the members of Run TMC?<br>
-Who is the Assistant GM for the Warriors?<br>
-Who is the Assistant coach for the Warriors?<br>
-Who is the Head Coach of the Warriors?<br><br>


## Swish V1's Language Briefing Script:

"Hello! My name is Swish. I am an AI that can tell you everything you'd ever wanted to know about the
Golden State Warriors. Please say 'next' to continue"<br><br>

"Please be sure to respond with keywords or entire phrases, ex: arena location or 
Where does Golden State play.
And remember! Currently I can only answer common questions about the Golden State Warriors. 
DO NOT use the word "next" in a question and please let me know when you would like to end the chat."<br><br>

## Project Photo <br><br>
![photo](photos/training.png)