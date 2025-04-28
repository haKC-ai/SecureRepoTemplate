#!/usr/bin/env python3
import os
from dotenv import load_dotenv

def secure_load_env():
    load_dotenv()
    variables = {}
    for key, value in os.environ.items():
        if key.endswith("_SALT") or key.endswith("_HASH"):
            variables[key] = value
    return variables
