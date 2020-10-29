li = [5, 8, 9, 10, 7]
lopinto=True

for elemento in li:
	if lopinto:
		print (elemento)
	lopinto=not lopinto


indice=0

for elemento in li:
	if indice%2==0:
		print(elemento)
	indice=indice+1
