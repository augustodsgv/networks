import socket

s1 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s1.bind(('2801:b0:20:59:aa6:4313:ca5c:82ec', 8080))

s1.listen(5)
cliente, _ = s1.accept()

mensagem = cliente.recv(8192)
print(mensagem)
cliente.close()
