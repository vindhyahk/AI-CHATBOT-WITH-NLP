## AI-CHATBOT-WITH-NLP:

COMPANY: CODTECH IT SOLUTIONS

NAME: VINDHYA H K

INTERN ID: CT08WOV

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

OUTPUT:

<img width="581" alt="Image" src="https://github.com/user-attachments/assets/e648a3da-3925-47f9-a78e-84f72f9a07b3" />


# SimpleNLTKChatbot

## Description
SimpleNLTKChatbot is a basic chatbot built using Python and the Natural Language Toolkit (NLTK). It can respond to user queries based on predefined keyword-based intents, such as greetings, farewells, gratitude, weather, and general help. This chatbot applies tokenization, lemmatization, and stopword removal to process user input and generate appropriate responses.

## Features
- Recognizes and responds to greetings, farewells, and thanks.
- Identifies user intent based on keywords.
- Implements text preprocessing with tokenization, punctuation removal, and lemmatization.
- Uses predefined responses for different intents.

## Installation
1. Clone this repository or download the script.
2. Ensure you have Python installed (version 3.x recommended).
3. Install the required dependencies using the following command:
  
   pip install nltk
  
4. Run the script to start the chatbot.

## Required NLTK Resources
Before running the chatbot, ensure that the required NLTK datasets are downloaded. The script will automatically download them if they are not available:
- `punkt` (for tokenization)
- `wordnet` (for lemmatization)
- `stopwords` (for filtering out common words)

## Usage
To start the chatbot, run the following command:

python chatbot.py

Then, you can interact with the chatbot by typing messages. To exit, type `quit`, `exit`, or `bye`.

## Example Interaction
```
SimpleBot: Hello! I'm a simple NLTK-powered chatbot. Type 'quit' to exit.
You: Hi
SimpleBot: Hello! How can I help you today?
You: What's your name?
SimpleBot: I'm SimpleBot, a basic NLTK-powered chatbot.
You: Thanks!
SimpleBot: You're welcome!
You: Bye
SimpleBot: Goodbye! Have a nice day!
```

## Customization
You can customize the chatbot by:
- Modifying the `self.responses` dictionary to add new responses.
- Updating `self.keywords` to recognize more keywords.
- Enhancing the preprocessing function to handle more complex queries.

## License
This project is open-source and can be modified or redistributed freely.


