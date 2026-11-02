# DFS, búsqueda en profundidad (The Farmer Was Replaced)
# Crea un laberinto y lo resuelve probando un camino hasta el final: si no lleva al tesoro,
# vuelve atrás hasta el último cruce y prueba el siguiente. Apunta las casillas donde ya ha
# estado, así que nunca se queda dando vueltas, aunque el laberinto tenga caminos en círculo
# (como pasa al reutilizarlo).

# Para volver por donde he venido: la dirección contraria de cada una.
opuesta = {
	North: South,
	South: North,
	East: West,
	West: East
}

# Cuánto cambian x e y al moverse en cada dirección: así sé qué casilla hay al lado.
# Es un diccionario porque busco por dirección, no por posición.
vecino = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0)
}

# Planta un arbusto y le echa Sustancia Rara: así nace el laberinto. La cantidad decide el
# tamaño (el lado de la granja) y cada mejora de los laberintos la duplica, igual que el oro.
def crear_laberinto():
	plant(Entities.Bush)
	nivel = num_unlocked(Unlocks.Mazes)
	sustancia = get_world_size() * 2 ** (nivel - 1)
	use_item(Items.Weird_Substance, sustancia)

# visitadas es un set: una bolsa de casillas (x, y) donde solo importa si una está dentro o no.
# Sin repetidos y sin orden; preguntar con in es justo lo que hace falta aquí.
# Devuelve True si encuentra el tesoro (y el dron se queda encima) y False si por aquí no hay.
def dfs(visitadas):
	if get_entity_type() == Entities.Treasure:
		return True
	x = get_pos_x()
	y = get_pos_y()
	# Apunto esta casilla: desde aquí ya no vuelvo a entrar en ella.
	visitadas.add((x, y))
	for d in [North, East, South, West]:
		dx, dy = vecino[d]
		siguiente = (x + dx, y + dy)
		# Las dos cosas a la vez: no haber estado allí y que no haya pared.
		if siguiente not in visitadas and can_move(d):
			move(d)
			# dfs se llama a sí misma: un paso más hacia dentro del camino. Si esa llamada
			# encuentra el tesoro, el True sube por todas las llamadas.
			if dfs(visitadas):
				return True
			# Ese camino no llevaba a nada: vuelvo y el for prueba la siguiente dirección.
			move(opuesta[d])
	# Ninguna dirección sirve: la llamada de antes es la que vuelve atrás.
	return False

# Solo se ejecuta si le das a ▶ en esta ventana, no cuando otro archivo hace import dfs.
# Cada laberinto empieza con un set nuevo y vacío.
if __name__ == "__main__":
	clear()
	crear_laberinto()
	dfs(set())
	harvest()
