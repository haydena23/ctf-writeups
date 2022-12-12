# eXclusive club
Files: [eXclusiveclub](./eXclusiveclub), [solver.py](./solver.py)

I have opened a new exclusive club, but you will need a password to join!

Author: @R3tr0

## Solution

First things first, we can see from `file eXclusiveclub` that the symbols are not stripped, therefore making decompiling easier. It appears that our input is obfuscated, and then sent to a checker function. Looking at the `obfuscation()` function, we can see it loops through the input and `input[i] XOR 0x41`.

In the checker function, we can see that it takes it compares a predetermined number with our `(obfuscated_char + i * 4)`. We can write a Python script to perform the reverse process of this to determine what our input should be. For this, we use the property of XOR stating `if a=b^c, then b=a^c`. This will in thoery produce our flag.

<b>It did not however, ever create a readable flag in solver.py. I will look into it and update this page when I figure out the correct reverse algorithm for this problem!</b>

---
## Flag
```

```