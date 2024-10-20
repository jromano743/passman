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
        except Exception as e:
            print(f"Error: File has not been created: {e}")

    def load_key(self, path):
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
        except Exception as e:
            print(f"Error: File has not been readed: {e}")
    
    def create_password_file(self, path):
        self.password_file = path
        try:
            with open(self.password_file, 'w') as f:
                f.write('')
        except Exception as e:
            print(f"Error: File has not been created: {e}")
    
    def load_password_file(self, path = None):

        if path is not None:
            self.password_file = path

        try: 
            with open(self.password_file, 'r') as f:
                for line in f:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted)
        except Exception as e:
            print(f"Error: File has not been readed: {e}")

    def add_password(self, site, password):
        self.load_password_file(self.password_file)
        self.password_dict[site] = password

        try:
            if self.password_file is not None:
                with open(self.password_file, 'a+') as f:
                    encrypted = Fernet(self.key).encrypt(password.encode())
                    f.write(f"{site}:{encrypted.decode()}\n")
        except Exception as e:
            print(f"Error: The password has not been added_ {e}")

    def get_password(self, site):
        try:
            self.load_password_file(self.password_file)
            return self.password_dict[site].decode()
        except Exception as e:
            print(f"Error: The password has not been reader: {e}")

# Add show current file and current path