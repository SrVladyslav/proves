import socket

#creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	mensaje = input("Pon un mensaje...")
	if(mensaje == 's'): break
	else:
		s.sendto(bytes(mensaje,'UTF-8'), ('127.0.0.1', 23451))

print("Saliendo del programa...")

s.close()