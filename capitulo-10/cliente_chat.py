import threading
import socket

nickname = input('Escolha seu nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 55555))


def recebe():

    while True:

        try:
            mensagem = client.recv(1024).decode('utf-8')

            if mensagem == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print('Um erro ocorreu!')
            client.close()
            break


def escreve():

    while True:
        mensagem = f'{nickname} : {input("")}'
        client.send(mensagem.encode('utf-8'))


recebe_thread = threading.Thread(target=recebe)
recebe_thread.start()

escreve_thread = threading.Thread(target=escreve)
escreve_thread.start()
