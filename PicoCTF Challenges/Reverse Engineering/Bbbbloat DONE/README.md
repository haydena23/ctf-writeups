# Bbbbloat

Can you get the flag? Reverse engineer this [binary](./bbbbloat).

Author: LT 'SYREAL' JONES

300 Points

---
## Solution

The first thing I always do when reverse engineering a binary is to `file bbbbloat`. After doing this, we can see that it is stripped. We can then open up the binary in IDA Freeware and then press `F5` to decompile the code. After inspecting the main function, we can see that it checks `if input = 249255`. When we run the program and type in that number, it gives us our flag.

---
## Flag
```
picoCTF{cu7_7h3_bl047_44f74a60}
```