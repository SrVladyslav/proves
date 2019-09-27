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

t = input("Pon un mensaje...")
if t == "s":
	break
else:
	s.sendall(bytes(t, 'utf-8'))

s.sendall(b'BYE!') 
# close the connection 
s.close()	 
#except:
	#print("Fallo...")
#\trigo\Escritorio\GIT HUB\Python\Cliente-Servidor
