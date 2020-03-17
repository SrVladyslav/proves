import re

s = "asfjaksf -hola- asfasf -hola \n de sd54nuevo- as54 \n fasfsd"
lista = ['6hola -dij1o el- hmmm', 'que tal -el- decia -gh-']

print(re.findall(r'-+[\w\s\.]+-', s))

salida = "> "
for l in lista:
	salida += str(re.findall(r'-\.+-', l))
print(salida)