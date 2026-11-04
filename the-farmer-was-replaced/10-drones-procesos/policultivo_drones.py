# Policultivo con drones (The Farmer Was Replaced)
# El policultivo del vídeo 7 repartido entre todos los drones, para cualquier granja y cualquier
# número de drones sin tocar el código. Cada dron es como un proceso: tiene su propia memoria y lo
# que le pasas se copia. Por eso cada vuelta tiene dos fases (principales y compañeras) y entre
# ellas el primer dron junta los pedidos de todos.

# La planta principal: basta con cambiar esta línea (Entities.Carrot, Entities.Grass...).
principal = Entities.Tree
fertilizar = True

# El suelo que necesita cada planta.
suelo = {
	Entities.Tree: Grounds.Grassland,
	Entities.Bush: Grounds.Grassland,
	Entities.Grass: Grounds.Grassland,
	Entities.Carrot: Grounds.Soil
}

# Va a una casilla por el camino más corto, dando la vuelta por el borde si es más cerca
# (la del vídeo de las calabazas).
def ir_a(posicion):
	tx, ty = posicion
	x, y = get_pos_x(), get_pos_y()
	n = get_world_size()
	mitad = get_world_size() // 2
	oeste = x - tx
	sur = y - ty
	# Para la X
	if oeste < 0:
		oeste = oeste + n
	if oeste <= mitad:
		for _ in range(oeste):
			move(West)
	else:
		for _ in range(n - oeste):
			move(East)
	# Para la y
	if sur < 0:
		sur = sur + n
	if sur <= mitad:
		for _ in range(sur):
			move(South)
	else:
		for _ in range(n - sur):
			move(North)

# Labra solo si el suelo no es el que necesita la planta.
def preparar_suelo(planta):
	if get_ground_type() != suelo[planta]:
		till()

# Apunta la compañera que pide la planta de esta casilla, si cae en una casilla impar
# y nadie la ha pedido antes (gana el primero).
def apuntar_compi(pedidos):
	compi = get_companion()
	if compi != None:
		tipo, (x, y) = compi
		if (x + y) % 2 == 1 and (x, y) not in pedidos:
			pedidos[(x, y)] = tipo

# Fase 1: planta las principales de su trozo de la cinta (casillas desde..hasta, columna tras
# columna) y apunta los pedidos en SU copia del diccionario, que devuelve al acabar.
def plantar_principales(desde, hasta, pedidos):
	n = get_world_size()
	# La casilla i de la cinta está en la columna i // n y en la fila i % n.
	ir_a((desde // n, desde % n))
	for i in range(desde, hasta):
		x = i // n
		y = i % n
		# Casillas pares: la planta principal (tablero de ajedrez).
		if (x + y) % 2 == 0:
			if get_entity_type() == principal:
				while not can_harvest():
					pass
				harvest()
			preparar_suelo(principal)
			plant(principal)
			if get_water() < 0.75:
				use_item(Items.Water)
			if fertilizar:
				use_item(Items.Fertilizer)
			apuntar_compi(pedidos)
		# Siguiente casilla de la cinta: al norte y, tras la última fila, a la columna siguiente.
		move(North)
		if y == n - 1:
			move(East)
	# Sin devolverlos, sus pedidos se perderían: no comparte memoria con los demás.
	return pedidos

# Fase 2: planta solo las compañeras pedidas que caen en su trozo. Cada casilla tiene un
# solo dueño en cada fase, así que no hay carreras.
def plantar_compis(desde, hasta, pedidos):
	n = get_world_size()
	ir_a((desde // n, desde % n))
	for i in range(desde, hasta):
		x = i // n
		y = i % n
		if (x, y) in pedidos:
			harvest()
			preparar_suelo(pedidos[(x, y)])
			plant(pedidos[(x, y)])
		move(North)
		if y == n - 1:
			move(East)

# Reparte la tarea entre todos los drones y devuelve lo que devuelve cada uno.
def en_paralelo(tarea, pedidos):
	n = get_world_size()
	total = n * n
	# Nunca más drones que casillas: ninguno se queda sin trabajo.
	trozos = min(max_drones(), total)
	drones = []
	resultados = []
	# Se reparten casillas, no columnas: todos trabajan lo mismo.
	for k in range(1, trozos):
		desde = k * total // trozos
		hasta = (k + 1) * total // trozos
		dron = spawn_drone(tarea, desde, hasta, pedidos)
		# None: no queda ningún dron libre, así que ese trozo lo hago yo.
		if dron == None:
			resultados.append(tarea(desde, hasta, pedidos))
		else:
			drones.append(dron)
	# El trozo 0 me lo quedo yo: el primer dron también trabaja.
	resultados.append(tarea(0, total // trozos, pedidos))
	# Barrera: espero a todos y recojo lo que devuelven (la única vía de vuelta).
	for dron in drones:
		resultados.append(wait_for(dron))
	return resultados

# Una vuelta: plantar principales, juntar los pedidos de todos y plantar compañeras.
def main():
	pedidos = {}
	for parte in en_paralelo(plantar_principales, {}):
		for casilla in parte:
			if casilla not in pedidos:
				pedidos[casilla] = parte[casilla]
	en_paralelo(plantar_compis, pedidos)

if __name__ == "__main__":
	clear()
	while True:
		main()
