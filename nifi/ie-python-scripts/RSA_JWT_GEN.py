#!/usr/bin/python3

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load private key
with open('/opt/nifi/data/private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

# Create a sample payload
payload = {
    'user_id': 101,
    'username': 'integration_admin@hcl.com',
    'exp': datetime.utcnow() + timedelta(minutes=2)  # Set expiration time
}

# Sign the JWT
token = jwt.encode(payload, private_key, algorithm='RS256')
print("JWT Token:", token)
