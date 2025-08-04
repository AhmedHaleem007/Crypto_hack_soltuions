from pwn import xor

name = "label"

key = 13

pwn_solv = xor ( name.encode()  , key).decode()
print(f"crypto{{{pwn_solv}}}")
