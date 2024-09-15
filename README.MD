# CLI Password Manager

A command-line tool for securely managing passwords. It allows users to store, retrieve, and generate strong passwords, all encrypted with a master key.

## Features
- Securely stores passwords using encryption.
- Generates strong, random passwords.
- Allows easy retrieval and deletion of stored passwords.
- User-friendly CLI interface.

## Installation
Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/4xyy/CLI-Password-Manager.git
cd CLI-Password-Manager
python3 -m venv .venv
source .venv/bin/activate
pip install cryptography

Usage
Setup the Password Manager:
python password_manager.py --setup
Add a New Password:
python password_manager.py --add service_name username password
Retrieve a Password:
python password_manager.py --get service_name
Delete a Password:
python password_manager.py --delete service_name
Generate a Random Password:
python password_manager.py --generate 16
