"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Saturday
    OOP intro
    Make a Chatbot class with attributes and a reply() method.
"""
import re

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.user_name = None
        self.state_name = "Initial"
        self.response = {
            'hello': f'Hello! My name is {self.name}. How can I help you?',
            'hola': f'Hola! Mi nombre es {self.name}, I know how to speak spanish',
            'how are you': "I'm doing great, thank you for asking",
            'bye': 'Goodbye! Have a great day.',
            'thank you': 'You are welcome! I am here to help you',
            'name': 'My name is Coda Chatbot~. What is your name?'
        }
        self.default_response = "I'm not sure how to respond to that. Can you rephrase?"
    
    def reply(self, user_input):
        user_input_lower = user_input.lower()
        # for keyword, response in self.response.items():
            # if keyword in user_input_lower:
            #     return response
        if re.search(r'^(hi|hello|hey)', user_input_lower, re.IGNORECASE):
            return self.response["hello"]
        elif re.search(r'^(hola|ey)', user_input_lower, re.IGNORECASE):
            return self.response["hola"]
        elif re.search(r'^(how are you|how have you been|how is going )', user_input_lower, re.IGNORECASE):
            return self.response["how are you"]
        elif re.search(r'^(bye|goodbye|good bye|see you soon)', user_input_lower, re.IGNORECASE):
            return self.response["bye"]
        elif re.search(r'^(thank you|thanks|thankyou)', user_input_lower, re.IGNORECASE):
            return self.response["thank you"]
        elif re.search(r'^(your name|what is your name)', user_input_lower, re.IGNORECASE):
            self.state_name = "asked_name"
            return self.response["name"]
        elif self.state_name == "asked_name":
            self.state_name = "Initial"
            if 'my name' in user_input_lower:
                self.user_name = user_input.split()[3]
            elif "i am" in user_input_lower:
                self.user_name = user_input.split()[2]
            elif "i'm" in user_input_lower or 'im' in user_input_lower:
                self.user_name = user_input.split()[1]
            else:
                self.user_name = user_input.split()[0]

            if self.user_name:
                return f'Nice to meet you {self.user_name}! I love your name!'
            else:
                return "I couldn't get your name. Let's try something else."
        else:
            return self.default_response

my_bot = Chatbot("Coda")
print("Coda:    How can I help you today? Coda chatbot~")
while True:
    user_message = input("You:  ")
    if not user_message.strip():
        print("Coda:    Empty Prompt, please try again!")
        continue
    if user_message.lower() == "exit":
        print("Coda:    Goodbye! See you soon.")
        break
    
    bot_reply = my_bot.reply(user_message)
    print(f"Coda:   {bot_reply}")