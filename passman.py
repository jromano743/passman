from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    def create_key(self, path):
        try:
            self.key = Fernet.generate_key()
            with open(path, 'wb') as f:
                f.write(self.key)
        except:
            print(f"Error: File has not been created.")

    def load_key(self, path):
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
        except:
            print(f"Error: File has not been readed.")
    
    def create_password_file(self, path):
        self.password_file = path
        try:
            with open(self.password_file, 'w') as f:
                f.write('')
        except:
            print(f"Error: File has not been created.")
    
    def load_password_file(self, path = None):

        if path is not None:
            self.password_file = path

        try: 
            with open(self.password_file, 'r') as f:
                for line in f:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted)
        except:
            print(f"Error: File has not been readed.")

    def add_password(self, site, password):
        self.load_password_file(self.password_file)
        self.password_dict[site] = password

        try:
            if self.password_file is not None:
                with open(self.password_file, 'a+') as f:
                    encrypted = Fernet(self.key).encrypt(password.encode())
                    f.write(f"{site}:{encrypted.decode()}\n")
        except:
            print(f"Error: The password has not been added.")

    def get_password(self, site):
        try:
            self.load_password_file(self.password_file)
            return self.password_dict[site].decode()
        except:
            print(f"Error: The password has not been reader")

def show_menu():
    print("")
    print("-"*20 + " Pass Man " + "-"*20)
    print("\t1)_ Create new key")
    print("\t2)_ Load existing key")
    print("\t3)_ Create new password file")
    print("\t4)_ Load existing password file")
    print("\t5)_ Add a new password")
    print("\t6)_ Get a password")
    print("\t7)_ Show menu")
    print("\t0)_ Exit")

def main():

    pm = PasswordManager()

    while True:
        
        show_menu()

        opt = input("Enter an option: ")


        if opt == "1":
            path = input("Enter new key path: ")
            pm.create_key(path)
        
        if opt == "2":
            path = input("Enter existing key path: ")
            pm.load_key(path)
        
        if opt == "3":
            path = input("Enter new password file path: ")
            pm.create_password_file(path)
        
        if opt == "4":
            path = input("Enter password file path: ")
            pm.load_password_file(path)

        if opt == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)

        if opt == "6":
            site = input("Enter the site: ")
            print(f"The password of {site} is: {pm.get_password(site)}")

        if opt == "7":
            show_menu()

        if opt == "0":
            print("-"*20 + " Bye bye ^^ " + "-"*20)
            break

if __name__ == '__main__':
    main()