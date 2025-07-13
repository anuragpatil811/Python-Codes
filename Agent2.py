import openai

class ChatAgent:
    def __init__(self, name, api_key):
        self.name = name
        self.api_key = api_key
    
    def greet(self):
        return f"Hello! I am {self.name}, your AI assistant. How can I help you today?"
    
    def process_input(self, user_input):
        response = self.generate_response(user_input)
        return response
    
    def generate_response(self, user_input):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"].strip()
    
    def chat(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break
            print("Chatbot:", self.process_input(user_input))

if __name__ == "__main__":
    api_key = "your_openai_api_key_here"  # Replace with your OpenAI API key
    agent = ChatAgent("AI Helper", api_key)
    agent.chat()
