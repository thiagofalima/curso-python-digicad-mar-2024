import socket


# Declarando o host e a porta

HOST = 'localhost'
PORT = 9090

# Criando o tipo de Socket internet IPV4, do tipo TCP
# Apenas para aceitar conecões
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Aqui estamos disponibilizando a porta e o host para conexão

server.bind((HOST, PORT))

# Preparando para receber conexões, quantas não aceitações podemos ter antes de rejeitar novas conexões

server.listen(5)

while True:
    # retorna o addres e o socket para comunicação
    comunicacao_socket, address = server.accept()
    print(f'Conectado ao {address}')
    # Recebendo mensagem com 1024 bytes e decodificando em UTF-8
    msg = comunicacao_socket.recv(1024).decode('utf-8')
    print(f'Mensagem do cliente: {msg}')
    # Enviando mensagem e codificando em utf-8
    comunicacao_socket.send('Mensagem recebida, obrigado!'.encode('utf-8'))
    # Fechando a conexão, podemos fechar ou não
    comunicacao_socket.close()
    print('Conexão com o endereço foi encerrada.')

