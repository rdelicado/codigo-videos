# Bubble sort contra insertion sort (The Farmer Was Replaced)
# El mismo programa que el de bubble sort (04-cactus-bubble-sort), cambiando
# solo ordenar_linea: ahora es insertion sort. Planta una granja de 6x6, ordena
# las filas y luego las columnas, y cosecha un cactus: el campo entero,
# ordenado, cae en cadena (36 x 36 = 1296 cactus). main mide cuántos ticks y
# segundos tarda en ordenar el campo, para compararlo con bubble sort.

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

# Insertion sort sobre la fila o la columna en la que está el dron, como al
# ordenar las cartas en la mano: la parte de atrás siempre está ordenada, y cada
# cactus nuevo se lleva hacia atrás hasta su sitio. `adelante` es East para una
# fila y North para una columna; acaba con el dron al principio de la línea,
# igual que la versión de bubble sort, así que ordenar_campo no cambia.
def ordenar_linea(adelante):
	n = get_world_size()
	# Para retroceder hace falta la dirección contraria.
	if adelante == East:
		atras = West
	else:
		atras = South
	# Desde el segundo cactus (i = 1) hasta el último.
	for i in range(1, n):
		move(adelante)
		j = i
		# Lo lleva hacia atrás mientras el de atrás sea más grande. En C o Python
		# se escribe `while j > 0 and a[j - 1] > a[j]`; aquí, con if y break,
		# porque la ayuda del juego no dice si `and` deja de mirar la segunda
		# condición cuando la primera es falsa.
		while j > 0:
			if measure(atras) > measure():
				swap(atras)
				move(atras)
				j -= 1
			else:
				break
		# Vuelve a la casilla i para coger el siguiente: retrocedió i - j pasos.
		for _ in range(i - j):
			move(adelante)
	# Un paso más: la granja da la vuelta por los bordes y el dron vuelve al
	# principio de la línea.
	move(adelante)

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

# Planta, ordena midiendo los ticks (no dependen de la velocidad ni de la
# energía) y los segundos, espera a que el cactus de debajo haya crecido y lo
# cosecha: el resto cae en cadena. Al final imprime lo que tardó en ordenar y
# la vuelta entera, de plantar a cosechar.
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
