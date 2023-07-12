# Galactic Federation

After escaping galactic federal prison, you (the legendary Rick Sanchez) have just given yourself Level 9 access to the federation headquarters. Now, you must break into their computer systems and find a way to topple the galactic government. [Galactic Federation](./galactic_federation.bin).
```Python
from pwn import * 
p=remote("spaceheroes-galactic-federation.chals.io", 443, ssl=True, sni="spaceheroes-galactic-federation.chals.io")
p.interactive()
```

Author: monkey_noises

250 Points

---
## Solution
This was a two part problem. The first thing we can see is that the .bin file is an executable. After running it, we see that we need to login. We can load the program up in IDA and see that there is an obfuscation function. It takes the user input, runs it through the obfuscation function, and then compares the output with a stored value, similar to hashing.

We can look at this simple function, and write a deobfuscation python script found [here](/Galactic%20Federation/deobfuscate.py) and throw in the stored obfuscated values. We can see that `USERNAME = admin` and `PASSWORD = 1_l0v3_wR4ngL3r_jE4nS` which brings us to the admin console. From the challenge description, we need some way to take down the government, and by poking around the admin console, we can see there is a page cause `adjust_economy`. In that, there is one function called `collapse_economy()` which seems like what we need. We can see that in order to access that function, the current currency needs to be `usd` and the value of currency has to be equal to 0. By looking at the .data of the binary, we can see that currency is initialized to a value of 1.

Now, we can run the program, put in our login credentials. From here, we can go to the `presidential_decree` and change the currency to `usd` and then `go_back`. Then, move over to `adjust_economy` and `inflate_currency`. From here, we can inflate the currency by a value of `-100` which would make currency equal zero. And there we have it, it collapses the economy and gives us our flag.

---
## Flag
```
shctf{w4it_uH_wh0s_P4y1Ng_m3_2_y3L1_@_tH15_gUy?}
```