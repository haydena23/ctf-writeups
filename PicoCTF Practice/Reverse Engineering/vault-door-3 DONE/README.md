# Vault-Door-3

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](./VaultDoor3.java).

Author: Mark E. Haase

200 points

---
## Solution

We are given a JavaScript file that compares our input to a predetermined string. We can see upon inspection that it uses four for loops. I created a [Python script](./solve.py) that contains the indexes for each of the for loops, as well as broke the flag up into a list of characters.

From here, I initilized an empty list of size 32, and then in each of the for loops, placed the appropriate character from the original string based off of the for loop index into our new array which holds our flag.

---
## Flag
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}
```