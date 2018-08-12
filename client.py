import socket # and whatever

#initialize
name = input('Enter your name: ')

# server messages TODO: move to a symbols module
hi = bytes('hi!'.encode())
bye = bytes('bye!'.encode())

addme = bytes(f'addme {name}'.encode())
gimmie = bytes('gimmie!'.encode())

ok = bytes(f'ok'.encode())
NO = bytes(f'NO'.encode())

ping = bytes(f'ping'.encode())
pong = bytes(f'pong'.encode())

err = bytes('err!'.encode())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#addr = ('127.0.0.1', 5555)
#addr = ('127.0.0.1', 5555)
addr = ('fedor.fedoraland', 5555)

sock.connect(addr)

sock.sendall(hi) # maybe just send?
msg = sock.recv(4096)
print(f'Response: {msg.decode()}')

sock.sendall(gimmie) 
msg = sock.recv(4096)
print(f'Response: {msg.decode()}')


sock.sendall(addme) 
msg = sock.recv(4096)
print(f'Response: {msg.decode()}')

sock.sendall(bye) 
msg = sock.recv(4096)
print(f'Response: {msg.decode()}')
if msg == bye:
    sock.close()

#action = input('What would you like to do?\n1.register\n2.get contacts\n3.quit')
