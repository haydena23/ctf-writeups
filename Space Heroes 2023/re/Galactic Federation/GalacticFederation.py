from pwn import * 
p=remote("spaceheroes-galactic-federation.chals.io", 443, ssl=True, sni="spaceheroes-galactic-federation.chals.io")
p.interactive()