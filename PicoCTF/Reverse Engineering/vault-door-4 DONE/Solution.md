To solve this, I took the array of values and copied it into a python script.
I then converted all of the hex values to decimal, as well as the octal values to decimal.
From there, just iterate through that list converting the decimal value to chars, and then
add that to a string to get the flag:

picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}