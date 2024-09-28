from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

# Create a chatbot instance
chatbot = ChatBot('Assistant')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus data
trainer.train('chatterbot.corpus.english')


# Define a function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)


# Function to handle greetings
def handle_greetings(user_input):
    greetings = ['hello', 'hi', 'hey', 'howdy']
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(
                ["Hello! How can I assist you today?", "Hi there! How may I help you?", "Hey! What can I do for you?"])
    return None


# Function to handle user's name
def handle_name(user_input):
    if 'name' in user_input.lower():
        return "My name is Assistant. How can I help you?"
    return None


# Function to handle thank you messages
def handle_thanks(user_input):
    thanks = ['thank', 'thanks', 'appreciate']
    for word in user_input.split():
        if word.lower() in thanks:
            return random.choice(["You're welcome!", "Glad I could help!", "No problem, happy to assist!"])
    return None


# Function to provide a random fact
def provide_fact():
    facts = [
        "Did you know that the Eiffel Tower was constructed in 1889?",
        "Here's a fun fact: The world's oldest known living tree is over 5,000 years old.",
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"
    ]
    return random.choice(facts)


# Function to provide motivation for seeking mental therapy
def provide_motivation():
    motivation_quotes = [
        "Remember, seeking therapy is a brave step towards your well-being and personal growth.",
        "Taking care of your mental health is as important as taking care of your physical health. Therapy can help you on that journey.",
        "You deserve to prioritize your mental well-being. Seeking therapy can provide you with the support and tools you need.",
        "Know that you are not alone. Many people find therapy to be a transformative and empowering experience.",
        "Taking the first step to seek therapy shows strength and self-awareness. It's a positive decision for your overall well-being."
    ]
    return random.choice(motivation_quotes)


# Main loop for the chatbot
while True:
    user_input = input("User: ")

    # Check if the user input includes greetings, name-related keywords, thank you messages, requests for facts, or motivation for seeking therapy
    greetings_response = handle_greetings(user_input)
    name_response = handle_name(user_input)
    thanks_response = handle_thanks(user_input)

    if user_input.lower() == 'bye':
        print("Assistant: Goodbye!")
        break
    elif greetings_response:
        print("Assistant:", greetings_response)
    elif name_response:
        print("Assistant:", name_response)
    elif thanks_response:
        print("Assistant:", thanks_response)
    elif 'fact' in user_input.lower():
        print("Assistant:", provide_fact())
    elif 'therapy' in user_input.lower() or 'mental health' in user_input.lower():
        print("Assistant:", provide_motivation())
    else:
        response = get_response(user_input)
        print("Assistant:", response)

