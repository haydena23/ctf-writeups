I first tried "file sc.exe" to read the details about the binary. We can see its a .NET binary.

I then wanted to see all of the strings for the file so I tried "strings sc.exe" which presented a lot of cleartext strings

To look at the whole file, I "cat sc.exe" which displayed the flag in cleartext:

flag{5+r1n9Se@rCh15c00l}