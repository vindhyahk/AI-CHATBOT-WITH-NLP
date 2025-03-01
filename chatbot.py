import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

class SimpleNLTKChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Sample responses for different query types
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I assist you?"
            ],
            'farewell': [
                "Goodbye! Have a great day!",
                "Bye! Feel free to chat again later.",
                "See you later! Take care!"
            ],
            'thanks': [
                "You're welcome!",
                "Happy to help!",
                "No problem at all!"
            ],
            'weather': [
                "I don't have access to real-time weather data, but I can help with other questions!",
                "For weather information, you might want to check a weather service."
            ],
            'name': [
                "I'm SimpleBot, a basic NLTK-powered chatbot.",
                "You can call me SimpleBot!"
            ],
            'help': [
                "I can respond to greetings, farewells, and basic questions. What would you like to know?"
            ],
            'default': [
                "I'm not sure I understand. Could you rephrase that?",
                "I'm still learning. Can you try asking in a different way?",
                "I don't have information about that yet."
            ]
        }
        
        # Keywords for identifying query types
        self.keywords = {
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'howdy'],
            'farewell': ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit'],
            'thanks': ['thanks', 'thank you', 'appreciate', 'grateful'],
            'weather': ['weather', 'temperature', 'forecast', 'rain', 'sunny'],
            'name': ['your name', 'who are you', 'call you','name'],
            'help': ['help', 'assist', 'support', 'guide']
        }
    
    def preprocess(self, text):
        """Preprocess the input text by tokenizing, removing punctuation, and lemmatizing."""
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = ''.join([char for char in text if char not in string.punctuation])
        
        # Tokenize and lemmatize
        tokens = nltk.word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        
        return tokens
    
    def identify_intent(self, tokens):
        """Identify the intent of the query based on keywords."""
        for intent, keywords in self.keywords.items():
            if any(keyword in ' '.join(tokens) for keyword in keywords):
                return intent
        return 'default'
    
    def respond(self, query):
        """Generate a response based on the query."""
        tokens = self.preprocess(query)
        intent = self.identify_intent(tokens)
        
        return random.choice(self.responses[intent])

    def run(self):
        """Run the chatbot in an interactive loop."""
        print("SimpleBot: Hello! I'm a simple NLTK-powered chatbot. Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("SimpleBot: Goodbye! Have a nice day!")
                break
            
            response = self.respond(user_input)
            print(f"SimpleBot: {response}")


if __name__ == "__main__":
    chatbot = SimpleNLTKChatbot()
    chatbot.run()