import os
import inquirer
from prompt_toolkit import prompt
import getpass
from .password_manager import PasswordManager

def main():
    pm = PasswordManager()
    
    while True:
        questions = [
            inquirer.List('option',
                message="Select an option:",
                choices=[
                    "1. Create new key",
                    "2. Load existing key",
                    "3. Create new password file",
                    "4. Load existing password file",
                    "5. Add a new password",
                    "6. Get a password",
                    "7. Exit",
                ],
            ),
        ]

        answers = inquirer.prompt(questions)
        option = answers['option']

        try:
            if option == "1. Create new key":
                path = prompt("Enter new key path: ")
                pm.create_key(path)
                print("Key created successfully!")

            elif option == "2. Load existing key":
                path = prompt("Enter existing key path: ")
                pm.load_key(path)
                print("Key loaded successfully!")

            elif option == "3. Create new password file":
                path = prompt("Enter new password file path: ")
                pm.create_password_file(path)
                print("Password file created successfully!")

            elif option == "4. Load existing password file":
                path = prompt("Enter password file path: ")
                pm.load_password_file(path)
                print("Password file loaded successfully!")

            elif option == "5. Add a new password":
                site = prompt("Enter the site: ")
                password = getpass.getpass("Enter the password: ")
                password2 = getpass.getpass("Repeat the password: ")

                if site == '' or password == '' or password2 == "":
                    print("Some fields are empty")
                
                if password != password2:
                    print("Passwords do not match")
                
                pm.add_password(site, password)
                print("Password added successfully!")

            elif option == "6. Get a password":
                site = prompt("Enter the site: ")
                password = pm.get_password(site)
                print(f"The password for {site} is: {password}")

            elif option == "7. Exit":
                print("Exiting...")
                break
            
            input("Press enter to continue")
            clear_screen()
        except Exception as e:
            print(f"Error: {e}")
            break

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run_cli():
    main()

if __name__ == "__main__":
    run_cli()
