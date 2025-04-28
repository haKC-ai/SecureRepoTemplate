#!/usr/bin/env python3
import os
import binascii
import hashlib
import questionary
from questionary import Style

style = Style([
    ('qmark', 'fg:#ff9d00 bold'),
    ('question', 'bold'),
    ('answer', 'fg:#00ff00 bold'),
    ('pointer', 'fg:#ff9d00 bold'),
    ('highlighted', 'fg:#ff9d00 bold'),
    ('selected', 'fg:#00ff00 bold'),
])

def create_env(path):
    entries = []
    while True:
        var_name = questionary.text("Enter variable base name (e.g., SERVICE_API)", style=style).ask()
        if not var_name:
            break
        secret_value = questionary.password(f"Enter secret for {var_name} (will be salted and hashed)", style=style).ask()
        salt = os.urandom(16)
        hash_value = hashlib.pbkdf2_hmac("sha256", secret_value.encode(), salt, 100000)
        entries.append(f"{var_name}_SALT={binascii.hexlify(salt).decode()}")
        entries.append(f"{var_name}_HASH={binascii.hexlify(hash_value).decode()}")

    with open(path, "w") as f:
        f.write("\n".join(entries))
    print(f"Secure .env file created at {path}")

if __name__ == "__main__":
    create_env(".env")
