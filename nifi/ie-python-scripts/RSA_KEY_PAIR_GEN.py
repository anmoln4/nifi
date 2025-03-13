#!/usr/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import os

#Genearte Public/Private key pair and saving in directory
def generate_and_save_rsa_key_pair(directory, key_size=2048):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )

    # Save private key to file
    private_key_path = os.path.join(directory, 'private_key.pem')
    with open(private_key_path, 'wb') as f:
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        f.write(private_key_bytes)

    # Save public key to file
    public_key = private_key.public_key()
    public_key_path = os.path.join(directory, 'public_key.pem')
    with open(public_key_path, 'wb') as f:
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        f.write(public_key_bytes)

    print(f"Key pair generated and saved:\nPrivate Key: {private_key_path}\nPublic Key: {public_key_path}")

# Example usage
current_directory = '/opt/nifi/data'
generate_and_save_rsa_key_pair(current_directory)
