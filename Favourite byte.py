from pwn import xor

key1 = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
    de = xor(key1 , i).decode()
    print(de)
    """if "crypto{0x10_15_my_f4v0ur173_by7e}" == de:
        print(i)
        break        

crypto{0x10_15_my_f4v0ur173_by7e} >> this is the key 
but you can search it manual

  """ 
