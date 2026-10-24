# 32 drones, 32 laberintos (The Farmer Was Replaced)
# Divide la granja en cuadrados de 5x5 y pone un laberinto y un dron en cada
# uno, todos trabajando a la vez (en el vídeo, granja de 32x32 y 32 drones).
# Cada dron busca su tesoro con BFS sobre su propio mapa, reutiliza el
# laberinto hasta 300 veces y luego crea otro en el mismo sitio.
# Sigue hasta tener el oro que cuesta el sombrero de copa (Unlocks.Top_Hat).
# Sin energía, para y planta girasoles con girasoles.py antes de seguir.
import girasoles

DIRS = [North, East, South, West]
L = 5                       # lado de cada laberinto (centrado en su arbusto)
DL = [1, L, -1, -L]         # cuánto cambia el número de casilla con cada dirección

# Va a (x, y) por el lado más corto, aprovechando que la granja da la vuelta.
# Solo se usa fuera de los laberintos, para llevar al dron a su cuadrado.
def ir_a(x, y):
	n = get_world_size()
	pasos_este = (x - get_pos_x() + n) % n
	if pasos_este <= n // 2:
		for _ in range(pasos_este):
			move(East)
	else:
		for _ in range(n - pasos_este):
			move(West)
	pasos_norte = (y - get_pos_y() + n) % n
	if pasos_norte <= n // 2:
		for _ in range(pasos_norte):
			move(North)
	else:
		for _ in range(n - pasos_norte):
			move(South)

# Casillas del laberinto numeradas 0..24: c = (x - x0) * L + (y - y0).
# vecinos[c * 4 + d] = casilla vecina en la dirección d (-1 = fuera del cuadrado).
# Se calcula una vez: así el BFS no tiene que hacer cuentas de coordenadas.
def calcular_vecinos():
	vecinos = []
	for x in range(L):
		for y in range(L):
			for d in range(4):
				v = x * L + y + DL[d]
				if d == 0 and y == L - 1:
					v = -1
				if d == 1 and x == L - 1:
					v = -1
				if d == 2 and y == 0:
					v = -1
				if d == 3 and x == 0:
					v = -1
				vecinos.append(v)
	return vecinos

# Mapa nuevo del dron, optimista: lo que aún no ha visto lo da por libre.
# abierto[c * 4 + d] = casilla a la que se llega desde c en la dirección d, o -1.
def mapa_nuevo(vecinos):
	abierto = []
	for v in vecinos:
		abierto.append(v)
	return abierto

# Mira las cuatro paredes de la casilla c y las apunta en el mapa por los dos
# lados (la pared entre c y su vecina vale para las dos).
def mirar(c, abierto, vecinos):
	b = c * 4
	for d in range(4):
		v = vecinos[b + d]
		if v >= 0:
			if can_move(DIRS[d]):
				abierto[b + d] = v
				abierto[v * 4 + (d + 2) % 4] = c
			else:
				abierto[b + d] = -1
				abierto[v * 4 + (d + 2) % 4] = -1

# BFS desde origen hasta destino sobre el mapa (para en cuanto lo encuentra).
# Devuelve las direcciones al revés (la primera, al final) o None si con lo
# que sabe el dron no hay camino.
def bfs(origen, destino, abierto):
	padre = []
	for _ in range(L * L):
		padre.append(-2)		# -2: casilla aún sin visitar
	padre[origen] = -1
	cola = [origen]
	i = 0
	while i < len(cola):
		c = cola[i]
		i += 1
		if c == destino:
			break
		b = c * 4
		for d in range(4):
			v = abierto[b + d]
			if v >= 0:
				if padre[v] == -2:
					padre[v] = d		# se llegó a v yendo en la dirección d
					cola.append(v)
	if padre[destino] == -2:
		return None
	ruta = []
	c = destino
	while padre[c] != -1:
		d = padre[c]
		ruta.append(d)
		c = c - DL[d]
	return ruta

# Camina hasta destino siguiendo el BFS. Mira las paredes en cada casilla y,
# si descubre un seto en el camino, recalcula la ruta con el mapa corregido.
# Devuelve False si con su mapa no hay camino.
def ir(c, destino, abierto, vecinos):
	while c != destino:
		mirar(c, abierto, vecinos)
		ruta = bfs(c, destino, abierto)
		if ruta == None:
			return False
		i = len(ruta) - 1
		while i >= 0:
			d = ruta[i]
			if abierto[c * 4 + d] < 0:
				break
			if not move(DIRS[d]):
				abierto[c * 4 + d] = -1
				break
			c = c + DL[d]
			mirar(c, abierto, vecinos)
			i -= 1
	return True

# Crea un laberinto en la casilla del dron: un arbusto y la sustancia encima.
def crear(sustancia):
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, sustancia)

# Vuelve al centro de su cuadrado sin salir de él (ya sin laberinto).
def volver(cx, cy):
	while get_pos_x() < cx:
		move(East)
	while get_pos_x() > cx:
		move(West)
	while get_pos_y() < cy:
		move(North)
	while get_pos_y() > cy:
		move(South)

# El trabajo de cada dron en su cuadrado de 5x5 con centro (cx, cy).
# Espera "esperar" ticks para que el dron principal salga antes de crearlo
# (si no, quedaría encerrado en el laberinto).
def minero(cx, cy, esperar, sustancia, meta):
	for _ in range(esperar):
		pass
	x0 = cx - L // 2
	y0 = cy - L // 2
	vecinos = calcular_vecinos()
	crear(sustancia)
	abierto = mapa_nuevo(vecinos)
	reutilizadas = 0
	tesoros = 0
	while num_items(Items.Gold) < meta and num_items(Items.Power) >= 1:
		pos = measure()			# measure() en un laberinto da la posición del tesoro
		if pos == None:
			break
		c = (get_pos_x() - x0) * L + get_pos_y() - y0
		t = (pos[0] - x0) * L + pos[1] - y0
		if not ir(c, t, abierto, vecinos):
			abierto = mapa_nuevo(vecinos)
		elif reutilizadas < 300:
			# misma sustancia sobre el tesoro: lo cobra y lo esconde en otro sitio
			if not use_item(Items.Weird_Substance, sustancia):
				break
			reutilizadas += 1
			tesoros += 1
		else:
			# ya no da más: cosechar y otro laberinto en el mismo sitio
			harvest()
			tesoros += 1
			volver(cx, cy)
			crear(sustancia)
			abierto = mapa_nuevo(vecinos)
			reutilizadas = 0
	# al parar (meta o sin energía) se cosecha el tesoro que quede,
	# para no perder nada al limpiar la granja
	pos = measure()
	if pos != None:
		c = (get_pos_x() - x0) * L + get_pos_y() - y0
		t = (pos[0] - x0) * L + pos[1] - y0
		if ir(c, t, abierto, vecinos):
			harvest()
	return tesoros

# Una ronda de laberintos: hasta la meta o hasta quedarse sin energía.
def ronda(sustancia, meta):
	n = get_world_size()
	# centros de los cuadrados de 5x5, en zigzag para no volver atrás
	centros = []
	for j in range(n // L):
		for k in range(n // L):
			i = k
			if j % 2 == 1:
				i = n // L - 1 - k
			centros.append((L // 2 + L * i, L // 2 + L * j))
	usar = min(len(centros), max_drones())
	# el principal deja un dron en cada centro y se queda el último
	drones = []
	for k in range(usar):
		cx, cy = centros[k]
		ir_a(cx, cy)
		if k < usar - 1:
			drones.append(spawn_drone(minero, cx, cy, 2000, sustancia, meta))
	tesoros = minero(cx, cy, 0, sustancia, meta)
	for dron in drones:
		tesoros += wait_for(dron)
	return tesoros

def main():
	# sustancia para un laberinto de LxL: L * 2^(nivel de Mazes - 1), según la ayuda del juego
	sustancia = L * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	meta = get_cost(Unlocks.Top_Hat)[Items.Gold]
	tesoros = 0
	while num_items(Items.Gold) < meta:
		if num_items(Items.Weird_Substance) < sustancia:
			quick_print("sin sustancia")
			break
		if num_items(Items.Power) < 1:
			# sin energía: una tanda de girasoles
			clear()
			girasoles.main()
			quick_print("energía recargada:", num_items(Items.Power))
			if num_items(Items.Power) < 1:
				quick_print("los girasoles no han dado energía")
				break
		clear()
		tesoros += ronda(sustancia, meta)
	return tesoros

if __name__=="__main__":
	inicio = get_time()
	oro = num_items(Items.Gold)
	tesoros = main()
	quick_print("tesoros:", tesoros)
	quick_print("oro:", num_items(Items.Gold) - oro)
	quick_print("tiempo:", get_time() - inicio)
