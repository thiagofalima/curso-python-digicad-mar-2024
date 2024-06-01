import threading
import socket

# Definindo uma porta e um host

host = 'localhost'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []

nicknames = []


def transmite(mensagem):

    for client in clients:

        client.send(mensagem)


def gerencia(client):

    while True:

        try:
            message = client.recv(1024)
            transmite(message)
        except:
            indice = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[indice]
            transmite(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break


def recebe():

    while True:

        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname do cliente é {nickname}!')
        transmite(f'{nickname} se cconectou ao chat!'.encode('utf-8'))

        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=gerencia, args=(client,))
        thread.start()


recebe()

