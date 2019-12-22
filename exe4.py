#4 - Escreva um programa que ordene uma lista numérica com três elementos.#
def 
lista =[78,57,10001,75,24,93]

print (lista)
for i in range(len(lista)):
	atual = lista[i]
	print (i, " i = ", i, "atual = ",atual)

	for j in range(i+1,len(lista)):
		aux1 = lista[j]
		print (j, " j = ", j, " aux1 = ",aux1)
		if lista[i] > lista[j]:
			aux2 = atual
			print ("aux2 = ", aux2, lista[i], lista[j])
			lista[i] = aux1
			lista[j] = aux2

print (lista)