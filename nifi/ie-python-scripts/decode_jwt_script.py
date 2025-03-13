#!/usr/bin/python3

import jwt
import sys
from datetime import datetime, timedelta

def authenticate_jwt(token, secret_key):
    try:
        # Decode and verify the JWT
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        print("True")
        return True
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return False
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return False

# Example usage:
authenticate_jwt(sys.argv[1], 'your_secret_key')
