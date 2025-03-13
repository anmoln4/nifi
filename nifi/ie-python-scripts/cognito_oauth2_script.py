#!/usr/bin/python3

import sys
import jwt
import requests
from datetime import datetime

# Current time in seconds
current_time = datetime.utcnow().timestamp()

# Step 1: Get Public Key
jwks_url = "https://cognito-idp.eu-central-1.amazonaws.com/eu-central-1_UO11I4jgD/.well-known/jwks.json"
jwks = requests.get(jwks_url).json()
public_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwks["keys"][1])
# Step 2: Decode and Validate Access Token
access_token = sys.argv[1]
try:
    decoded_token = jwt.decode(access_token, public_key, algorithms=["RS256"])
    #Token decoded successfully
    if "exp" in decoded_token and decoded_token["exp"] > current_time:
        #Token is not expired
        expected_issuer = (
            "https://cognito-idp.eu-central-1.amazonaws.com/eu-central-1_UO11I4jgD"
        )
        if "iss" in decoded_token and decoded_token["iss"] == expected_issuer:
            #Issuer is valid.
            print("Authenticated")
        else:
            print("Invalid issuer.")
    else:
        print("Token has expired.")
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError as e:
    print("Invalid token:", str(e))
