import socket

s1 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

s1.connect(('2801:b0:20:59:aa6:4313:ca5c:82ec', 8080))
mensagem = input('Digite a mensagem: ').encode()
s1.send(mensagem)

s1.close()