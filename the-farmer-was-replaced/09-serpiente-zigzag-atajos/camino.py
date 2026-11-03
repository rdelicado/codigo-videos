# El camino de la serpiente (The Farmer Was Replaced)
# Un ciclo hamiltoniano en zigzag: pasa por todas las casillas una sola vez y acaba al lado de
# donde empezó. Si la serpiente lo sigue siempre, la cola va detrás y nunca choca con ella.
# Sube por la primera columna, cruza por arriba, baja haciendo eses y vuelve por la fila de abajo.
# Solo funciona con un lado par (6, 12...): las filas de las eses van de dos en dos.

# n es el lado de la granja. Devuelve una lista de direcciones, una por paso: se recorre en
# orden, vuelta tras vuelta, y con el número de un paso sé en qué punto del camino estoy.
def hacer_camino(n):
	camino = []
	# Subir la primera columna: de la casilla 0 a la n - 1 hay n - 1 pasos.
	for i in range(n - 1):
		camino.append(North)
	# Cruzar por arriba.
	for i in range(n - 1):
		camino.append(East)
	# Las eses: cada vuelta hace dos filas (al oeste y al este). Van n - 2 pasos porque la
	# primera columna queda libre para subir. Quedan n - 2 filas, dos por vuelta.
	for i in range((n - 2) // 2):
		camino.append(South)
		for j in range(n - 2):
			camino.append(West)
		camino.append(South)
		for j in range(n - 2):
			camino.append(East)
	# Bajar a la fila de abajo y volver al oeste hasta la esquina de salida.
	camino.append(South)
	for i in range(n - 1):
		camino.append(West)
	return camino
