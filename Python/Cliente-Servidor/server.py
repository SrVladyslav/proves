import socket			 


# creamos el bjeto del socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado!")

# declaramos el puerto en el que haremos la conexion
port = 23451				

# ponemos a la escucha al servidor a todas las ips entrantes
# al puerto dado
s.bind(('', port))		 
print("socket a la escucha en el puerto: %s" %(port)) 

# ponemos al socket a escuchar aceptando como maximo 5 usuarios 
s.listen(5)	 
print("socket escuchando...")
print("==========================CONEXIONES=========================")		
clientes = 0
# bucle de escucha que acepta las peticiones
while clientes < 3: 
	# estableciendo la conexion con el cliente 
	c, addr = s.accept()	 
	clientes += 1
	print('Peticion entrante de: ', addr) 

	# Devolviendo un mensaje por los jajas. 
	c.sendall(b'Bienvenidos al servidor pirata!') 

	#recibiendo mensajes
	print(f"Cliente " ,clientes ,f"dice:" + str(c.recv(2048)))
	#hacemos un simple Eco
	c.sendall(c.recv(1024))
	# cerrando la conexion (IMPORTANTE o SUSPENDEIS) 
	c.close() 

