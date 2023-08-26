import pandas as pd
import random
import incident

# Create an empty DataFrame to store login details

# Define chatbot responses
responses = {

    "hello": ["Hi there!", "Hello!", "Hey!"],

    "how are you": ["I'm just a bot, but I'm here to help!", "I'm good, thanks for asking!",
                    "I don't have feelings, but I'm ready to assist!"],

    "bye": ["Goodbye!", "See you later!", "Bye bye!"],

    "default": ["I'm not sure I understand.", "Could you please rephrase that?",
                "I'm still learning, can you try something else?"]

}

# Define helpline options
helpline_options = {
    "1": "RITM",
    "2": "INC",
    "3": "CHG"
}


# Calling service_now through functions
def call_to_service_now(argument):
    switcher = {
        1: RITM(),
        2: INC(),
        3: CHG(),
    }
    return switcher.get(argument, "nothing")

# function for RITM
def RITM():
    return 1 + 2

# function for INC
def INC():
    var = incident.INCident()
    return var.get("result").get("number")

# function for CHG
def CHG():
    return "yet to be done"

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

def Login():
    try:
        login_data = pd.read_excel('C:/Users/Siddhartha Sen/PycharmProjects/pythonProject/login_details.xlsx')

    except FileNotFoundError:
        login_data = pd.DataFrame(columns=['Employee_ID', 'Username', 'Password'])

    # input for login
    ID = input("Enter your Employee_ID: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # DataFrame for login deatils
    new_login_data = pd.DataFrame({'Employee_ID': [ID], 'Username': [username], 'Password': [password]})
    login_data = pd.concat([login_data, new_login_data], ignore_index=True)
    # Save the DataFrame to an Excel file
    login_data.to_excel('C:/Users/Siddhartha Sen/PycharmProjects/pythonProject/login_details.xlsx', index=False)
    print("Login details saved successfully!")
    return 1

def main():
    x = Login()
    if (x == 1):
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye!")
                break
            if user_input.lower() == "menu":
                display_menu()
                input_item = int(input("Chatbot: Enter the option u want to choose from above list:"))
                print(call_to_service_now(input_item))
                continue
            response = chatbot_response(user_input)
            print("Chatbot:", response)
    else:
        print("Please fill the above data")


if __name__ == "__main__":
    main()
