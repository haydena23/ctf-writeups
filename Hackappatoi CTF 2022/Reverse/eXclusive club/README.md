# eXclusive club
Files: [eXclusiveclub](./eXclusiveclub), [solver.py](./solver.py)

I have opened a new exclusive club, but you will need a password to join!

Author: @R3tr0

## Solution

First things first, we can see from `file eXclusiveclub` that the symbols are not stripped, therefore making decompiling easier. It appears that our input is obfuscated, and then sent to a checker function. Looking at the `obfuscation()` function, we can see it loops through the input and `input[i] XOR 0x41`.

In the checker function, we can see that it takes it compares a predetermined number with our obfuscated number, so by the XOR property of `if a=b^c then b=a^c`. We can then create a Python script to quickly do that for us and we have the flag!

---
## Flag
```
hctf{eXclU51v3_0r^N♠t?}
```