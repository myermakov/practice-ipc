import socket 
import json


# initialize listening socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST, PORT = socket.gethostname(), 5555
sock.bind( (HOST, PORT) )
sock.listen(1)
print(f'Listening on: {HOST}')


hi = bytes('hi!'.encode())
gimmie = bytes(f'gimmie!'.encode())
bye = bytes('bye!'.encode())
err = bytes('err!'.encode())
ok = bytes(f'ok'.encode())
NO = bytes(f'NO'.encode())


addme = bytes(f'addme'.encode())

def match(token):
    if token == hi or token == bye:
        return token
    else:
        print('unknown token')
        return err


while True:
    conn, address = sock.accept() # blocks here
    print(f'Accepted connection from {address}')

    # TODO: thread it
    token = conn.recv(4096)

    while token != bye:
        restoken = match(token)
        conn.sendall(restoken)
        print(f'{address[0]}: {token.decode()}')
        print(f'response: {restoken.decode()}')
        token = conn.recv(4096)
    
    assert token == bye
    conn.close()

sock.close()


# NOTE
# for same machine IPC, pipes or shared memory is faste 
#AF_UNIX
# TIPC < linux only
#AF_INET
#(host, port)
#sock = socket.socket()
#sock.create_connection(addr)
#socket.inet_aton(ip_string)
#host = socket.gethostname()
#bind() # binds socket to address
#connect(arrdess) # connect to a remote socket at address
#listen()
#conn, addr = accpet() # must be bound and listening
## conn - socket object
## addr - address bound to the socket on the other end
#close() # can context manager
#bytes = recv(bufsize=4096)
#num_bytes_sent = send(bytes)
#sendall(bytes)
