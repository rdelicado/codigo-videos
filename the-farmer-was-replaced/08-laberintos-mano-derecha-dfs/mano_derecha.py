# Mano derecha (The Farmer Was Replaced)
# Crea un laberinto y lo resuelve con la regla de la mano derecha: ir siempre pegado a la
# pared de la derecha. En un laberinto recién creado todos los setos están unidos, así que
# siguiendo esa pared se llega a todas partes, también al tesoro.

# Las cuatro direcciones en el orden de las agujas del reloj: la derecha de cada una es la
# siguiente de la lista (del norte, el este) y la izquierda, la anterior.
direcciones = [North, East, South, West]

# Planta un arbusto y le echa Sustancia Rara: así nace el laberinto. La cantidad decide el
# tamaño (el lado de la granja) y cada mejora de los laberintos la duplica, igual que el oro.
def crear_laberinto():
	plant(Entities.Bush)
	nivel = num_unlocked(Unlocks.Mazes)
	sustancia = get_world_size() * 2 ** (nivel - 1)
	use_item(Items.Weird_Substance, sustancia)

# El dron no gira: solo se mueve al norte, este, sur u oeste. Hacia dónde "mira" lo llevamos
# nosotros en d, su posición en la lista (0 = norte).
def mano_derecha():
	d = 0
	# No se sabe cuántos pasos hacen falta: while, hasta estar encima del tesoro.
	while get_entity_type() != Entities.Treasure:
		# Girar a la derecha es sumar 1; % 4 hace que del oeste (3) se vuelva al norte (0).
		derecha = (d + 1) % 4
		# Primero la derecha, que es la mano pegada a la pared. can_move solo pregunta;
		# move se movería sin avisar.
		if can_move(direcciones[derecha]):
			d = derecha
			move(direcciones[d])
		# Pared a la derecha pero no delante: sigo recto.
		elif can_move(direcciones[d]):
			move(direcciones[d])
		# Pared a la derecha y delante: giro a la izquierda sin moverme. En un callejón, la
		# siguiente vuelta vuelve a girar: dos giros son media vuelta.
		else:
			d = (d - 1) % 4

# Solo se ejecuta si le das a ▶ en esta ventana, no cuando otro archivo hace import mano_derecha.
if __name__ == "__main__":
	clear()
	crear_laberinto()
	mano_derecha()
	harvest()
