# Hackappa_rev
Files: [hackappa_rev](./hackappa_rev)

Here we are again, this is our favorite pub! You can take the flag and come back without getting drunk in the process?

Author: @Unleashed

## Solution

As always, the first thing I want to do is check `file hackappa_rev` to see if the symbols have been stripped. They have not! That will make decompilation significantly easier.

Now we will load the binary into IDA Freeware, and press `F5` to decompile. We see that the `decrypt()` function is run if the three counters are equal to `10, 7, 11` which we assume corresponds to the drink counters when running the program. So we run the program, purchase that amount of drinks for each, and it presents our flag!

---
## Flag
```
HCTF{3z_Drunk_R3v}
```