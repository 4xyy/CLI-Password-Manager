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
git clone https://github.com/<YOUR_USERNAME>/CLI-Password-Manager.git
cd CLI-Password-Manager
python3 -m venv .venv
source .venv/bin/activate
pip install cryptography

