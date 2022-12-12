For this problem, I took the base64 encoded bytes and stored them as a literal string in Python.
From here, using the base64 library, I decoded the base64 bytes to give the URL encoded data.
You can then decode this by using the parser from the Python library urllib which returns the flag:

picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}