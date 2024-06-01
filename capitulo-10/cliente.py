import socket

# Aqui estamos interessados no IP do servidor, não no IP privado
# IP publico
HOST = 'localhost'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Aqui estamos conectando

socket.connect((HOST, PORT))

# enviando uma mensagem

socket.send('Hello World'.encode('utf-8'))

# Aguardando por uma resposta

print(socket.recv(1024).decode('utf-8'))



