import sys
import os
import json

from views.App.quiz_app_handler import start_quiz
# load user data function


# Importing built-in python functions and modules.
import json
import os

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Relative path to the user data JSON file from the current directory
relative_path = "User_data/user_data.json"

# Absolute path to the user data JSON file using the relative path
USER_DATA_FILE_PATH = os.path.join(current_directory, relative_path)


# Function to load user data from JSON file
def load_user_data():
    if not os.path.exists(USER_DATA_FILE_PATH):
        # If file doesn't exist, initialize user data as an empty dictionary
        return {}

    try:
        with open(USER_DATA_FILE_PATH, 'r') as file:
            user_data = json.load(file)
    except json.JSONDecodeError:
        # If JSON decoding fails, initialize user data as an empty dictionary
        user_data = {}

    return user_data


# Function to save user data to JSON file
def save_user_data(user_data):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(USER_DATA_FILE_PATH), exist_ok=True)
    with open(USER_DATA_FILE_PATH, 'w') as file:
        json.dump(user_data, file, indent=4)




# Function to sign up a new user
def signup():
    print("\n\n\033[95mSign Up in CoderQuiz App.\033[0m\n\n")
    username = input("\033[1mEnter username: \033[0m")
    password = input("\033[1mEnter password: \033[0m")
    email = input("\033[1mEnter email: \033[0m")

    user_data = load_user_data()

    if not user_data:
        user_data = {username: {'password': password, 'email': email}}
        save_user_data(user_data)
        print("\033[92mSign up successful!\033[0m")
    elif username in user_data:
        print("\033[91mUsername already exists. "
              "Please choose a different username.\033[0m")
    else:
        user_data[username] = {'password': password, 'email': email}
        save_user_data(user_data)
        print("\n\n\033[92mSign up successful!\033[0m\n\n")

# Function to handle user login
def login():
    print("\n\n\033[95mLog In with correct username and password!\033[0m\n\n")
    username = input("\033[1mEnter your username: \033[0m")
    password = input("\033[1mEnter your password: \033[0m")

    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == password:
        print("\n\n\033[92mLogin successful!\033[0m\n\n\n")
        start_quiz(username)
    else:
        print("\033[91mInvalid username or password.\033[0m")

# Function to handle changing user password
def change_password():
    print("\033[95mChange Password\033[0m")
    username = input("\033[1mEnter username: \033[0m")
    old_password = input("\033[1mEnter current password: \033[0m")

    user_data = load_user_data()

    if (username in user_data and
            user_data[username]['password'] == old_password):
        new_password = input("\033[1mEnter new password: \033[0m")
        user_data[username]['password'] = new_password
        save_user_data(user_data)
        print("\033[92mPassword changed successfully!\033[0m")
    else:
        print("\033[91mInvalid username or password.\033[0m")

# Function to start the authentication system
def user_auth_main():
    # User data file path
    USER_DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "User_data/user_data.json")
    
    # Authentication menu loop
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Change Password\n4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("\n\n\033[95mWelcome to CoderQuiz!\033[0m")  # Header in magenta color
    print("Type Y or Yes to start the Quiz App.\n\n")
    choice = input("\033[1mEnter Yes or No: \033[0m").lower()  # Bold prompt for user input
    print(choice)
    if choice == "y" or choice == "yes":
        # Call user authentication main function
        user_auth_main()
    elif choice == 'n' or choice == "no":
        print("\033[92mExiting...\033[0m")  # Green color for "Exiting..."
        sys.exit()
    else:
        print("\n\n\033[91mInvalid choice. Please try again.\033[0m\n\n")  # Red color for error message

if __name__ == "__main__":
    main()
