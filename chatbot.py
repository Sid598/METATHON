import random

# Define chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "I'm good, thanks for asking!", "I don't have feelings, but I'm ready to assist!"],
    "bye": ["Goodbye!", "See you later!", "Bye bye!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm still learning, can you try something else?"]
}

# Define helpline options
helpline_options = {
    "1": "Emergency Services",
    "2": "Technical Support",
    "3": "General Information"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

def display_menu():
    print("Helpline Options:")
    for option, description in helpline_options.items():
        print(f"{option}. {description}")
        
def main():
    print("Chatbot: Hello! I'm here to help. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        if user_input.lower() == "help":
            display_menu()
            continue
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
