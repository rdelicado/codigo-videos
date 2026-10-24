# Girasoles con todos los drones (The Farmer Was Replaced)
# Recarga energía: planta una granja de girasoles con un dron por columna,
# mide sus pétalos y los cosecha de mayor a menor número de pétalos.
# Si hay al menos 10 girasoles y cosechas el de más pétalos, da 8 veces más
# energía. Por eso nunca se cosecha uno mientras quede otro con más pétalos.
# laberintos.py lo usa cuando se queda sin energía.

# Cada dron planta su columna, mide los pétalos de cada girasol y devuelve
# SU diccionario: número de pétalos -> lista de posiciones con ese número.
def trabajar(planta):
	petalos = {}
	for y in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(planta)
		p = measure()		# pétalos del girasol de debajo (de 7 a 15)
		if p not in petalos:
			petalos[p] = []
		petalos[p].append((get_pos_x(), get_pos_y()))
		move(North)
	return petalos

# Cada dron recibe la lista entera, pero cosecha solo las posiciones de su
# columna. Si el girasol aún no ha crecido, espera encima hasta que crezca.
def cosechar(posiciones):
	x = get_pos_x()
	for pos in posiciones:
		if pos[0] == x:
			ir_a(pos[0], pos[1])
			while not can_harvest():
				pass
			harvest()

# Junta los diccionarios de todos los drones en uno solo con todas las posiciones.
def juntar(resultados):
	todos = {}
	for datos in resultados:
		for clave in datos:
			if clave not in todos:
				todos[clave] = []
			for pos in datos[clave]:
				todos[clave].append(pos)
	return todos

# Saca un dron por columna (tantas como drones haya) y les pone a todos a
# hacer `funcion(dato)`. El dron principal hace la última columna y luego
# espera a los demás con wait_for, que devuelve lo que ha devuelto cada uno.
def sacar_drones(funcion, dato):
	drones = []
	n = min(get_world_size(), max_drones())
	for i in range(1, n):
		drones.append(spawn_drone(funcion, dato))
		move(East)
	resultados = []
	resultados.append(funcion(dato))
	for dron in drones:
		resultados.append(wait_for(dron))
	return resultados

# Va a (x, y) por el lado más corto: la granja da la vuelta por los bordes.
# pasos_este es cuántos pasos hay hacia el este; si es más de la mitad de la
# granja, por el oeste son menos (n - pasos_este). Igual con norte y sur.
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

# Una tanda: todos plantan y miden, se juntan los resultados y se cosecha de
# 15 a 7 pétalos. Para cada número, todos los drones cosechan a la vez los
# girasoles de su columna con ese número, y hasta que no acaban todos
# (wait_for dentro de sacar_drones) no se pasa al número siguiente.
def main():
	resultados = sacar_drones(trabajar, Entities.Sunflower)
	todos = juntar(resultados)
	for p in range(15, 6, -1):
		if p in todos:
			sacar_drones(cosechar, todos[p])

# Ejecutado solo: 10 tandas seguidas, y cuánto tiempo y energía han dado.
if __name__=="__main__":
	clear()
	init = get_time()
	energia = num_items(Items.Power)
	for i in range(10):
		main()
	quick_print("tiempo:", get_time() - init)
	quick_print("energía:", num_items(Items.Power) - energia)
