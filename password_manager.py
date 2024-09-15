import os
import json
import base64
from cryptography.fernet import Fernet
from argparse import ArgumentParser
from getpass import getpass

DATA_FILE = 'passwords.json'
KEY_FILE = 'secret.key'

def generate_key():
    """Generate a key for encryption and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from a file."""
    return open(KEY_FILE, 'rb').read()

def encrypt_password(password, key):
    """Encrypt a password using the given key."""
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    """Decrypt a password using the given key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

def load_data():
    """Load password data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    """Save password data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def add_password(service, username, password, key):
    """Add a new password entry."""
    data = load_data()
    encrypted_password = encrypt_password(password, key)
    data[service] = {'username': username, 'password': encrypted_password}
    save_data(data)
    print(f"Password for {service} added successfully.")

def get_password(service, key):
    """Retrieve a password entry."""
    data = load_data()
    if service in data:
        encrypted_password = data[service]['password']
        decrypted_password = decrypt_password(encrypted_password, key)
        print(f"Service: {service}")
        print(f"Username: {data[service]['username']}")
        print(f"Password: {decrypted_password}")
    else:
        print(f"No password found for {service}.")

def delete_password(service):
    """Delete a password entry."""
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        print(f"Password for {service} deleted successfully.")
    else:
        print(f"No password found for {service}.")

def generate_password(length=12):
    """Generate a random password."""
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated password: {password}")
    return password

def main():
    parser = ArgumentParser(description="CLI Password Manager")
    parser.add_argument('--setup', action='store_true', help="Setup the password manager.")
    parser.add_argument('--add', nargs=3, metavar=('SERVICE', 'USERNAME', 'PASSWORD'), help="Add a new password.")
    parser.add_argument('--get', metavar='SERVICE', help="Retrieve a password.")
    parser.add_argument('--delete', metavar='SERVICE', help="Delete a password.")
    parser.add_argument('--generate', type=int, metavar='LENGTH', help="Generate a random password.")
    args = parser.parse_args()

    if args.setup:
        generate_key()
        print("Password manager setup complete. Key generated.")

    elif args.add:
        if not os.path.exists(KEY_FILE):
            print("Error: Key file not found. Run the setup command first.")
            return
        key = load_key()
        service, username, password = args.add
        add_password(service, username, password, key)

    elif args.get:
        if not os.path.exists(KEY_FILE):
            print("Error: Key file not found. Run the setup command first.")
            return
        key = load_key()
        get_password(args.get, key)

    elif args.delete:
        delete_password(args.delete)

    elif args.generate:
        generate_password(args.generate)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

