# Best videogame
Files: [bestvideogame](./bestvideogame)

Can you guess what is my favourite videogame saga? I hope you like it too!

Author: @R3tr0


## Solution

The first thing I always check is `file bestvideogame` to see if the binary is stripped, whih in this case it is not. Then next step is to ppen it up in IDA Freeware and we can see just in main that it has a list of ints, creates some sort of key, and performs an RC4 symmetric encryption. If we can get the key and the ciphertext, we can create th eoriginal input!

We can see that argv[1] has to be `play` or else nothing will happen. That means we have already figured out the first half of our input. We can inspect the generatekey function which is passing in our input `play`, and see that it doesn't actually do anything. That means our encryption key is `play`.

It then performs an RC4 encryption with that key, and to get checks that encryption in a for loop against all of those values we can see at the beginning of the file. That's our ciphertext. We can take all of these values, and convert them to hexadecimal format which gives us `3d a4 aa 27 ef 7b 0d 4d 68 c4 c2 99 1a 75 f8 02 32 0f 8b 74 19 97 9d`.

We can then use any onlin RC4 decryption tool now that we have the key and ciphertext. I personally used [this](https://cryptii.com/pipes/rc4-encryption) website. I clicked decode, put in our key and our ciphertext, and it returned out flag.

---
## Flag
```
hctf{R351d3N7_3viL_5CarY_Uh?}
```