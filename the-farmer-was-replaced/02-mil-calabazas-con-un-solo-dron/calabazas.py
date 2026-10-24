# Mil calabazas con un solo dron (The Farmer Was Replaced)
# Planta toda la granja de calabazas, vuelve solo a las casillas que faltan
# (las muertas y las que aún crecen) por el camino más corto, y cuando todas
# han crecido cosecha la calabaza gigante.

# Planta la granja columna a columna y apunta cada casilla en `pendientes`.
# Una sola vuelta no basta: una de cada cinco calabazas muere al crecer, así
# que luego hay que revisarlas todas. Apuntarlas aquí no cuesta ni un paso,
# porque el dron ya está encima de cada casilla al plantarla.
# Como la granja da la vuelta por los bordes, funciona empiece donde empiece.
def plantar_campo(pendientes):
	for _ in range(get_world_size()):		# cada columna
		for _ in range(get_world_size()):	# cada casilla de la columna, subiendo
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			pendientes.append((get_pos_x(), get_pos_y()))
			move(North)
		move(East)
	return pendientes

# Lleva al dron a `posicion` por el camino más corto.
# La granja da la vuelta: si el dron sale por un borde, aparece por el de
# enfrente. Así que en cada eje se puede ir por los dos lados, y se elige el
# que tenga menos pasos. Cruzar el borde es un solo paso, aunque la animación
# del juego dibuje al dron cruzando todo el campo.
def ir_a(posicion):
	tx, ty = posicion
	x, y = get_pos_x(), get_pos_y()
	n = get_world_size()
	mitad = get_world_size() // 2
	oeste = x - tx		# pasos hacia el oeste: dónde estoy menos adónde voy
	sur = y - ty		# pasos hacia el sur, igual
	# Para la X
	if oeste < 0:		# negativo: el destino está detrás; la vuelta lo arregla sumando n
		oeste = oeste + n
	if oeste <= mitad:	# la mitad o menos: se va por el oeste
		for _ in range(oeste):
			move(West)
	else:				# más de la mitad: por el este son n - oeste pasos, menos
		for _ in range(n - oeste):
			move(East)
	# Para la y (lo mismo, con sur y norte)
	if sur < 0:
		sur = sur + n
	if sur <= mitad:
		for _ in range(sur):
			move(South)
	else:
		for _ in range(n - sur):
			move(North)

# Revisa las casillas pendientes hasta que todas hayan crecido.
# - pendientes: las que hay que mirar en esta vuelta (al principio, todas).
# - siguen: las que habrá que volver a mirar; empieza vacía en cada vuelta.
# Al acabar la vuelta, pendientes pasa a ser siguen, así que cada vuelta la
# lista es más corta. Cuando se queda vacía, el campo entero ha crecido.
# El dron solo sabe cómo está una casilla cuando está encima, por eso vuelve
# a mirarlas aunque tú ya las veas crecidas.
def revisar_campo(pendientes):
	while len(pendientes) > 0:
		quick_print(pendientes)		# la lista de cada vuelta, en la ventana de salida
		quick_print(" ")
		siguen = []
		for pos in pendientes:
			ir_a(pos)
			if not can_harvest():
				# Muerta: plantar pone una nueva en su lugar.
				# Aún creciendo: plantar no hace nada.
				# En los dos casos hay que volver a mirarla.
				plant(Entities.Pumpkin)
				siguen.append(pos)
		pendientes = siguen

clear()		# granja vacía y dron en (0, 0)
pendientes = []
pendientes = plantar_campo(pendientes)
revisar_campo(pendientes)
do_a_flip()		# el juego ya ha unido la gigante, pero tarda un momento en dibujarla
harvest()		# cosecha la calabaza gigante entera
