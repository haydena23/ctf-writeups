# Acheron

While researching a foreign planet, you and your team discover a cave with some strange eggs. Upon inspection, something attacked your team. You got separated from them and knocked unconscious. Once awake, you begin running to your ship to regroup with your team. The problem is, you don't remember the way. Find your way back to your ship. [Acheron](./Acheron).
```Python
from pwn import *
p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
p.interactive()
```

Author: Cody

250 Points

---
## Solution
We can examine the file initially by running `file Acheron` and see that it is a 64-bit ELF binary. We can open up and analyze the binary in Ghidra.

After finding the Main function, we can see it is just a series of if statements which checks for the proper user input of `NENWSSEWSNENSSWEENWSNNESS`.

---
## Flag
```
shctf{gam3_0v3r_m@n_game_0ver}
```