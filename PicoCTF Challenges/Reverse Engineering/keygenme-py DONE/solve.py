import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

words = [
    hashlib.sha256(bUsername_trial).hexdigest()[4],
    hashlib.sha256(bUsername_trial).hexdigest()[5],
    hashlib.sha256(bUsername_trial).hexdigest()[3],
    hashlib.sha256(bUsername_trial).hexdigest()[6],
    hashlib.sha256(bUsername_trial).hexdigest()[2],
    hashlib.sha256(bUsername_trial).hexdigest()[7],
    hashlib.sha256(bUsername_trial).hexdigest()[1],
    hashlib.sha256(bUsername_trial).hexdigest()[8]
]

print(words)