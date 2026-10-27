# Bubble sort con cactus: 36 de una sola cosecha (The Farmer Was Replaced)
# Con un solo dron y una granja de 6x6: planta cactus, los ordena con el
# método de la burbuja (primero las filas, luego las columnas) y cosecha uno.
# Si el campo entero está ordenado, la cosecha se extiende en cadena y da
# tantos cactus como el número cosechado al cuadrado: 36 x 36 = 1296.
# Un cactus está ordenado si los de su norte y su este son igual de grandes o
# más, y los de su sur y su oeste, igual de grandes o más pequeños.

# Planta la granja columna a columna y mide cada cactus nada más plantarlo.
# Al acabar cada columna la imprime: así queda en la salida cómo era el campo
# antes de ordenarlo (cada línea es una columna, de abajo arriba).
def plantar_campo():
	n = get_world_size()
	for x in range(n):
		columna = []
		for y in range(n):
			# till() en tierra ya labrada la vuelve a dejar en hierba: por eso
			# solo se labra si hace falta.
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			columna.append(measure())
			move(North)
		quick_print(columna)
		move(East)

# La burbuja sobre la fila o la columna en la que está el dron. `adelante` es
# la dirección: East para una fila, North para una columna, así que la misma
# función sirve para las dos cosas.
def ordenar_linea(adelante):
	n = get_world_size()
	# True para entrar en el while; cada pasada lo pone en False y solo vuelve
	# a True si hay algún cambio. Una pasada sin cambios = línea ordenada.
	cambiado = True
	while cambiado:
		cambiado = False
		# Seis cactus forman cinco parejas: n - 1 comparaciones por pasada.
		for i in range(n - 1):
			# swap solo cambia con la casilla de al lado: si el de debajo es
			# más grande que el siguiente, se cambian.
			if measure() > measure(adelante):
				swap(adelante)
				cambiado = True
			move(adelante)
		# Un paso más: la granja da la vuelta por los bordes y el dron vuelve
		# al principio de la línea con un solo move, en vez de andar hacia atrás.
		move(adelante)

# Ordena las seis filas hacia el este y luego las seis columnas hacia el norte.
# Si las filas ya están ordenadas, ordenar las columnas no las desordena.
# Cada pasada acaba donde empezó, así que el dron siempre está en su sitio para
# la siguiente línea y al final vuelve a la esquina (0, 0).
def ordenar_campo():
	n = get_world_size()
	for y in range(n):
		ordenar_linea(East)
		move(North)
	for x in range(n):
		ordenar_linea(North)
		move(East)

# Planta, ordena, espera a que el cactus de debajo haya crecido y cosecha solo
# ese: el resto del campo, ya ordenado, cae en cadena.
def main():
	plantar_campo()
	ordenar_campo()
	while not can_harvest():
		pass
	harvest()

# clear() limpia la granja y deja el dron en (0, 0); después, una vuelta detrás
# de otra.
if __name__ == "__main__":
	clear()
	while True:
		main()
