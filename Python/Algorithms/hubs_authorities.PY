import torch
import numpy as np 

# ======================= RELLENA LOS DATOS ======================================
# Pon las iteraciones que quieres hacer
ITERACIONES = 10

# Introduce el numero de decimales 
DECIMALES = 3

enlaces = torch.tensor([
	# Rellena la matriz de los tensores 1.0
	[  ],
	[  ],
	[  ],
	[  ],
	[  ]

	# Si cambia la dimension, recuerda mantener la matriz cuadrada
	])

# ==========================NO TOQUES NADA, PORQUE TOCAS? ===============================

hubs = torch.tensor([
	# Rellena aqui con la fila de hubs si cambia
		[1.0, 1.0, 1.0, 1.0, 1.0]
	])

autorities = torch.tensor([
	# Rellena aqui con la fila de hubs si cambia
		[1.0, 1.0, 1.0, 1.0, 1.0]
	])


# ============================================== METODOS DE CALCULO ===================================

# Devuelve para cada fila las posibles transiciones salientes
def indFila(enlaces):
	indices = []
	# Recorro filas
	for i in range(enlaces.size()[0]):
		ind = []
		# Recorro columnas en busqueda de indices
		for j in range(enlaces.size()[1]):
			ind.append(j) if enlaces[i][j].numpy() == 1.0 else True#print("")#enlaces[i][j].numpy())
		indices.append(ind)
	return indices
		
indicesHub = indFila(enlaces)
print("Indices Hub: ",indicesHub)

# Devuelve para cada columna las transiciones entrantes
def indColu(enlaces):
	indices = []
	# Recorro columnas
	for i in range(enlaces.size()[1]):
		ind = []
		# Recorro filas buscando las entradas
		for j in range(enlaces.size()[0]):
			ind.append(j) if enlaces[j][i].numpy() == 1.0 else True #print("")#enlaces[j][i].numpy())
		indices.append(ind)
	return indices

indicesAuto = indColu(enlaces)
print("Indices Autority: ",indicesAuto)


def normalizar(fila, iteraciones, decimales):
	normalizado = []
	for i in range(fila.size()[1]):
		normalizado.append(round((fila.numpy()[iteraciones] /sum(fila.numpy()[iteraciones]))[i], decimales))
	return normalizado


# =============================== ALGORITMO EN SI HASTA K ITERACIONES =========================================
# 1) Obtenemos los indices
indiHub = indFila(enlaces)

indiAutority = indColu(enlaces)

# 2) Algoritmo
for it in range(ITERACIONES):
	# Calculo la siguiente fila de Hubs
	# 2.1) Obtengo la direccion
	# Pilla la fila anterior a la de hubs, ya que siempre será la que va más avanzada 
	filaA = hubs.size()[0] - 1 

	# 2.2 Hago las sumas para cada fila de Hub
	indices = []
	for c in range(hubs.size()[1]):
		indices.append(sum(autorities[filaA][indiHub[c]].numpy()))

	#print(hubs.size())	
	#print(torch.tensor([indices]).size())
	# 2.3 Tengo la nueva fila de Hubs hecha, la añado al tensor
	hubs = torch.cat((hubs,torch.tensor([indices])))

	# 3) Calculo autority
	filaH = autorities.size()[0] - 1

	# 3.1) Hago las sumas
	indices = []
	for c in range(autorities.size()[1]):
		indices.append(sum(hubs[filaH][indiAutority[c]].numpy()))

	# 3.2) Añado la solucion
	autorities = torch.cat((autorities, torch.tensor([indices])))

# ================================================ FIN DEL ALGORITMO, ENTRANDO A PRESENTACION =========================




print("\n====================== SOLUCION =======================")
print("HUBS:")
print(hubs.numpy()[:ITERACIONES])
print("\nNormalizado: ",normalizar(hubs, ITERACIONES, DECIMALES),'\n')


print("AUTORITIES:")
print(autorities.numpy()[:ITERACIONES])	
print("\nNormalizado: ",normalizar(autorities, ITERACIONES, DECIMALES))
print("=========================================================")