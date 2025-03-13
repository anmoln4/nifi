#!/usr/bin/python3

import jwt
from datetime import datetime, timedelta

# Your secret key for signing the JWT
secret_key = 'your_secret_key'

# Payload containing information you want to include in the JWT
payload = {
    'user_id': 101,
    'username': 'integration_admin@hcl.com',
    'exp': datetime.utcnow() + timedelta(minutes=2)  # Set expiration time
}

# Create the JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')
print(f"Generated JWT: {token}")
