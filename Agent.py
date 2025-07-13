class Agent:
    def __init__(self, name, purpose):
        self.name = name 
        self.purpose = purpose
    def describe(self):
        return f"Agent '{self.name}' is designed for {self.purpose}."
agent = Agent("ChatBot", "answering user queries")
print(agent.describe())

import numpy as np
import pandas as pd
import openai
import requests
from transformers import pipeline
class ChatAgent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello ! I am {self.name}, your AI assistant. How can I help you today ?"
agent = ChatAgent("AI Helper")
print(agent.greet())
def process_input(user_input):
    responses = {
        "hello": "Hi there ! How can I assist you ?",
        "bye": "Goodbye ! Have a great day !",
        "help": "I can help you with general queries. Ask me anything !" 
    }
    return responses.get(user_input.lower(), "I'm not sure about that, but I'm learning !")
print(process_input("hello"))

def chat():
    print("Chatbot: Hello! Type 'exit to end the chat.")
    while True:
        user_input = input("You:")
        if user_input.lower()=="exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", process_input(user_input))
def test_agent():
    test_cases = ["hello", "help", "bye", "unknown"]
    for case in test_cases:
        print(f"User:{case}")
        print(f"Agent: {process_input(case)}\n")
test_agent()