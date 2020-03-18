import socket

#creo el socket UDP
print("=================Server a la escucha============")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#pongo a la escucha el socket a todos lo puertos
puerto = 23451
s.bind(('127.0.0.1', puerto))

#recibo datos que vengan por casualidad hacia mi
conexiones = 0
while conexiones < 5:
	data, addr = s.recvfrom(2048)

	print(f"Cliente dice: ", data.decode('UTF-8'))

	conexiones += 1
print("=================================================")