# La serpiente con atajos (The Farmer Was Replaced)
# Sigue el mismo ciclo que el zigzag, pero si una casilla de al lado está más adelante en el
# camino, salta a ella. Sin pasarse de la manzana y sin adelantar a la cola, así nunca se encierra.
# Cuando ocupa un tercio de la granja pasa al zigzag: con la serpiente larga, los atajos dejan
# huecos detrás de ella y calcular el atajo cuesta más ticks que el propio paso.

from camino import hacer_camino

# Cuánto cambian x e y al moverse en cada dirección: así sé qué casilla hay al lado.
vecino = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0)
}

# Recorre el camino una vez y apunta el puesto (el número de paso) de cada casilla.
# Es un diccionario porque luego pregunto al revés: estoy en (x, y), ¿qué número tiene?
def numerar(camino, N):
	puesto = {}
	x = 0
	y = 0
	for i in range(N):
		puesto[(x, y)] = i
		dx, dy = vecino[camino[i]]
		x += dx
		y += dy
	return puesto

# h, manzana y cola son puestos del camino. Devuelve la dirección y cuántos pasos avanza.
def atajo(puesto, camino, N, h, manzana, cola):
	# Pasos de camino hasta la manzana y hasta la cola (el resto de dividir da la vuelta).
	a = (manzana - h) % N
	t = (cola - h) % N
	# 0 = la cola está en la cabeza: aún no hay cola y todo el camino está libre.
	if t == 0:
		t = N
	# Si no hay nada mejor, el siguiente paso del camino.
	mejor = camino[h]
	salto = 1
	x = get_pos_x()
	y = get_pos_y()
	for d in vecino:
		dx, dy = vecino[d]
		v = (x + dx, y + dy)
		# Si no tiene puesto, está fuera de la granja.
		if v in puesto:
			p = (puesto[v] - h) % N
			# Que avance más, que no pase la manzana y que quede por delante de la cola.
			# El - 1 deja una casilla libre delante de la cola: si en este paso come una
			# manzana, la cola no se mueve, y sin esa casilla el siguiente paso chocaría.
			if p > salto and p <= a and p < t - 1:
				salto = p
				mejor = d
	return mejor, salto

def serpiente():
	clear()
	N = get_world_size() ** 2
	camino = hacer_camino(get_world_size())
	puesto = numerar(camino, N)
	change_hat(Hats.Dinosaur_Hat)
	# La cabeza y la manzana empiezan en el puesto 0: la primera manzana sale debajo del dron.
	h = 0
	manzana = 0
	# Los puestos que va ocupando la serpiente, de la cola a la cabeza. No se borra nada:
	# pop(0) cuesta tantos ticks como elementos tiene la lista, así que cola dice dónde
	# empieza la cola dentro de la lista y avanzar es sumar uno.
	cuerpo = [0]
	cola = 0
	# Atajos mientras ocupe menos de un tercio de la granja (el largo es len(cuerpo) - cola).
	while len(cuerpo) - cola < N // 3:
		# Lo guardo antes de moverme: después ya no estaré en la manzana.
		comiendo = h == manzana
		if comiendo:
			# measure, encima de la manzana, dice dónde sale la siguiente.
			manzana = puesto[measure()]
		d, salto = atajo(puesto, camino, N, h, manzana, cuerpo[cola])
		move(d)
		h = (h + salto) % N
		cuerpo.append(h)
		# Si come, la cola crece: no se mueve.
		if not comiendo:
			cola += 1
	# El resto, en zigzag desde donde está, hasta llenar la granja.
	while move(camino[h]):
		h = (h + 1) % N
	change_hat(Hats.Straw_Hat)

if __name__ == "__main__":
	serpiente()
