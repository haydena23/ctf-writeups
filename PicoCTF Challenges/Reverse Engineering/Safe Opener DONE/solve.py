import base64
b64 = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

decoded = base64.b64decode(b64)
print(decoded)