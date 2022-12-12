By opening the file in Ghidra, I found that the entire alphabet was being push to some sort of array.
From here, there is a function that seems to call a significant amount of functions using the address of that list.
Using solve.py, I take the decompiled data from Ghidra, clean up the hex calls, and match the hex calls to the letters in the list.
This provides the flag which is picoCTF{d15a5m_ftw_717bea4}
