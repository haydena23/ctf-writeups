def deobfuscate(obfuscated):
    result = ""
    for c in obfuscated:
        result += chr(ord(c) - 7)
    return result

obfuscated = input()
original = deobfuscate(obfuscated)
print(original)

# Username: admin
# Password: 1_l0v3_wR4ngL3r_jE4nS