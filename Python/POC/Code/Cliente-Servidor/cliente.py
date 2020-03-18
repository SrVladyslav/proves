import socket			 
#try:
# Crenado un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definiendo el puerto 
port = 23451				

# conectando a la IP localhost por el pueto port
s.connect(('127.0.0.1', port)) 

# recibiendo cosas del servidor 
print(s.recv(1024))

while True:
	t = input("Pon un mensaje: ")
	s.sendall(bytes(t, 'utf-8'))
	if t == "info":
		print(s.recv(1024).decode())
	#elif t[0:2] == "eco":
		#print(s.recv(1024).decode()) 
	if t == 's':
		break
#print(s.recv(1024))
print("sale")
s.sendall(b'BYE!') 
# cerrando conexion
s.close()	 
#\trigo\Escritorio\GIT HUB\Python\Cliente-Servidor
