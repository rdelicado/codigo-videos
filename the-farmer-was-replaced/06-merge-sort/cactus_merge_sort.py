# Merge sort (The Farmer Was Replaced)
# El mismo programa que los de bubble sort e insertion sort (04 y 05), cambiando
# solo ordenar_linea: ahora es merge sort, que parte la línea por la mitad,
# ordena cada mitad con la misma función (recursión) y las mezcla. En la granja
# no hay lista auxiliar: solo se puede cambiar un cactus con su vecino, así que
# mezclar es insertar, uno a uno, los cactus del trozo derecho en el izquierdo.
# main mide cuántos ticks y segundos tarda en ordenar el campo.

# Planta la granja columna a columna y mide cada cactus nada más plantarlo.
# Al acabar cada columna la imprime: cada línea es una columna, de abajo arriba.
def plantar_campo():
	n = get_world_size()
	for x in range(n):
		columna = []
		for y in range(n):
			# till() en tierra ya labrada la vuelve a dejar en hierba.
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			columna.append(measure())
			move(North)
		quick_print(columna)
		move(East)

# Lleva al dron a la casilla `destino` de la línea por el lado más corto, dando
# la vuelta por el borde si hace falta (la de calabazas, pero en una dimensión).
# `adelante` es East para una fila y North para una columna.
def ir_a(destino, adelante, atras):
	n = get_world_size()
	# En qué casilla de la línea está: en una fila lo dice x; en una columna, y.
	if adelante == East:
		pos = get_pos_x()
	else:
		pos = get_pos_y()
	# Pasos hacia delante; si sale negativo, el destino está detrás y la vuelta
	# por el borde lo arregla sumando n.
	pasos = destino - pos
	if pasos < 0:
		pasos = pasos + n
	# La mitad o menos: hacia delante. Más: son n - pasos hacia atrás, menos.
	if pasos <= n // 2:
		for _ in range(pasos):
			move(adelante)
	else:
		for _ in range(n - pasos):
			move(atras)

# Mezcla las dos mitades ya ordenadas, la que va de ini a medio y la que va de
# medio a fin (sin incluir fin). Sin lista auxiliar: cada cactus de la derecha
# se lleva hacia atrás, cambiándolo con su vecino, como en insertion sort.
def mezclar(ini, medio, fin, adelante, atras):
	ir_a(medio, adelante, atras)
	# Si el último de la izquierda ya no es mayor que el primero de la derecha,
	# no hay nada que mezclar: una comparación se ahorra todo el trabajo.
	if measure(atras) > measure():
		for i in range(medio, fin):
			# Después de insertar, el dron se queda atrás: ir_a elige el camino
			# corto hasta el siguiente cactus de la derecha.
			ir_a(i, adelante, atras)
			j = i
			# Como en insertion sort, con if y break en vez de `and`, pero
			# hasta ini (el principio del trozo), no hasta 0.
			while j > ini:
				if measure(atras) > measure():
					swap(atras)
					move(atras)
					j -= 1
				else:
					break

# Ordena de ini a fin (sin incluir fin): un trozo de uno o cero cactus ya está
# ordenado (caso base); si no, ordena cada mitad con esta misma función y las
# mezcla. adelante y atras viajan de función en función.
def ordenar(ini, fin, adelante, atras):
	if fin - ini < 2:
		return
	medio = (ini + fin) // 2
	ordenar(ini, medio, adelante, atras)
	ordenar(medio, fin, adelante, atras)
	mezclar(ini, medio, fin, adelante, atras)

# Merge sort sobre la fila o la columna en la que está el dron. Acaba con el dron
# al principio de la línea, igual que las versiones de bubble e insertion sort,
# así que ordenar_campo no cambia.
def ordenar_linea(adelante):
	n = get_world_size()
	# Para retroceder hace falta la dirección contraria.
	if adelante == East:
		atras = West
	else:
		atras = South
	ordenar(0, n, adelante, atras)
	ir_a(0, adelante, atras)

# Ordena las seis filas hacia el este y luego las seis columnas hacia el norte
# (si las filas ya están ordenadas, ordenar las columnas no las desordena).
def ordenar_campo():
	n = get_world_size()
	for y in range(n):
		ordenar_linea(East)
		move(North)
	for x in range(n):
		ordenar_linea(North)
		move(East)

# Planta, ordena (midiendo ticks y segundos con get_tick_count y get_time),
# espera a que todos hayan crecido, cosecha el campo entero de una vez y
# escribe cuánto tardó.
def main():
	inicio_vuelta = get_time()
	plantar_campo()
	inicio = get_tick_count()
	t0 = get_time()
	ordenar_campo()
	ticks = get_tick_count() - inicio
	segundos = get_time() - t0
	while not can_harvest():
		pass
	harvest()
	quick_print("ordenar:", ticks, "ticks,", segundos, "s | vuelta:", get_time() - inicio_vuelta, "s")

if __name__ == "__main__":
	clear()
	while True:
		main()
