# Merge sort con listas, como se escribe en cualquier lenguaje (el que se explica en
# el vídeo antes de llevarlo a la granja). Ordena la lista `a` en el sitio,
# de `ini` a `fin` sin incluir `fin`.

# Mezcla las dos partes ya ordenadas, de ini a medio y de medio a fin, con dos
# marcadores y una lista auxiliar (resultado).
def mezclar(a, ini, medio, fin):
	resultado = []
	i = ini
	j = medio
	# Mientras queden elementos en las dos partes, se coge el menor. Con iguales
	# gana el de la izquierda (menor, no menor o igual): así es estable.
	while i < medio and j < fin:
		if a[j] < a[i]:
			resultado.append(a[j])
			j += 1
		else:
			resultado.append(a[i])
			i += 1
	# Una parte se ha vaciado: lo que queda en la otra ya está ordenado.
	while i < medio:
		resultado.append(a[i])
		i += 1
	while j < fin:
		resultado.append(a[j])
		j += 1
	# Devuelve el resultado a su sitio en la lista original.
	for k in range(len(resultado)):
		a[ini + k] = resultado[k]

# Caso base: con cero o un elemento ya está ordenado. Si no, parte por la mitad,
# ordena cada mitad con esta misma función y las mezcla.
def ordenar(a, ini, fin):
	if fin - ini < 2:
		return
	medio = (ini + fin) // 2
	ordenar(a, ini, medio)
	ordenar(a, medio, fin)
	mezclar(a, ini, medio, fin)
