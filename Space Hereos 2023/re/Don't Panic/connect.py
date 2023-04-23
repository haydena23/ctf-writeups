from pwn import * 
p=remote("spaceheroes-dontpanic.chals.io", 443, ssl=True, sni="spaceheroes-dontpanic.chals.io")
p.interactive()