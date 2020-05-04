'''
	CALCULADORA PARA HACER ITERACIONES 
	DE PAGERANK, USAR CON CUIDADO
'''

import numpy as np
import torch

def next(n):
	s = [str(round(i,3)) for i in n]
	return ' , '.join(s)

#	===========================================================
#	Aquí va t-1, para calcular 
#	===========================================================
#	
tAnterior = torch.tensor([[
# Pega aqui el resultado del t-1:
	1.0, 0, 0, 0, 0 
]])
#	===========================================================
#	Aquí va la matriz de transiciones (solo se pone una vez xD) 
#	===========================================================
transiciones = torch.tensor([
# Rellena aqui con la matriz de transiciones CON TP
[ ],
[ ],
[ ],
[ ],
[ ]
])


tActual = torch.mm(tAnterior , transiciones)
print("---------------------------------------------------------------")
print(">t actual:",tActual.numpy()[0])
print("---------------------------------------------------------------\n")

print("======  COPIA ESTO PARA LA SIGUIENTE ITERACION ======\n|")
print("|   ",next((tActual.numpy()[0])),"\n|")
print("=====================================================\n")