import os
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize

# Download the required NLTK data
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Define a class for the Elveirdor AI
class ElveirdorAI:
    def __init__(self):
        self.name = "Elveirdor"
        self.version = "1.0"
        self.sia = SentimentIntensityAnalyzer()

    def greet(self):
        return f"Hello, I'm {self.name} AI, version {self.version}."

    def respond(self, input_text):
        sentiment = self.sia.polarity_scores(input_text)
        tokenized_text = word_tokenize(input_text)
        tagged_text = pos_tag(tokenized_text)
        named_entities = ne_chunk(tagged_text)

        entities = []
        for tree in named_entities:
            if hasattr(tree, 'label'):
                entity = ' '.join([leaf[0] for leaf in tree.leaves()])
                entities.append(entity)

        if sentiment['compound'] > 0.5:
            return "I'm glad you're feeling positive!"
        elif sentiment['compound'] < -0.5:
            return "Sorry to hear you're feeling down."
        elif entities:
            return f"I noticed you mentioned {entities[0]}. Can you tell me more about that?"
        else:
            responses = [
                "I'm not sure I understand.",
                "That's an interesting question.",
                "I'm happy to help with that.",
            ]
            return random.choice(responses)

# Create an instance of the Elveirdor AI
ai = ElveirdorAI()

# Test the AI
print(ai.greet())
while True:
    user_input = input("User: ")
    print(f"AI: {ai.respond(user_input)}")
