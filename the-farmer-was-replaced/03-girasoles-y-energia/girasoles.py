# El triple de energía con los mismos girasoles (The Farmer Was Replaced)
# Con un solo dron y una granja de 6x6: planta los girasoles midiendo sus
# pétalos y los guarda en un diccionario; luego los cosecha del de más
# pétalos al de menos. Si hay al menos 10 girasoles y cosechas el de más
# pétalos, da 8 veces más energía; si cosechas otro, pierdes el bonus en ese
# y en el siguiente. Por eso importa tanto el orden.

# Lleva al dron a `posicion` por el camino más corto, aprovechando que la
# granja da la vuelta por los bordes. Es la misma función del vídeo de las
# calabazas (allí se explica paso a paso): se copia aquí tal cual, porque
# importar calabazas.py ejecutaría su programa entero.
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

# Primera vuelta: planta toda la granja y mide cada flor.
# measure() da los pétalos de la flor de debajo (de 7 a 15) aunque todavía no
# haya crecido, así que se puede apuntar todo mientras se planta.
# `petalos` es un diccionario, como una cajonera:
# - la clave (la etiqueta del cajón) es el número de pétalos;
# - el valor (lo que hay dentro) es la lista de posiciones con ese número.
def plantar_campo(petalos):
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			p = measure()
			if p not in petalos:		# primera flor con este número: el cajón aún no existe
				petalos[p] = []
			petalos[p].append((get_pos_x(), get_pos_y()))
			move(North)
		quick_print(petalos)		# el diccionario al acabar cada columna
		quick_print(" ")
		move(East)
	return petalos				# fuera de los dos bucles: si va dentro, solo planta una columna

# Segunda vuelta: abre los cajones del 15 al 7 (range para justo antes del 6)
# y cosecha todas las flores de cada uno. Si no ha salido ninguna flor con un
# número, ese cajón no existe y se salta. Antes de cosechar, espera a que la
# flor haya crecido.
def recoger_flores(petalos):
	for p in range(15, 6, -1):
		if p in petalos:
			for pos in petalos[p]:
				ir_a(pos)
				while not can_harvest():
					pass
				harvest()

# Una vuelta completa: plantar y medir, recoger en orden, y cuánta energía ha dado.
def main():
	petalos = {}
	start = num_items(Items.Power)
	petalos = plantar_campo(petalos)
	for p in range(15, 6, -1):
		if p in petalos:
			quick_print(p, "petalos:", len(petalos[p]))
	recoger_flores(petalos)
	quick_print(num_items(Items.Power) - start)

# En bucle: en el vídeo, unas 215 de energía por vuelta; con cinco vueltas,
# el logro de las mil de energía (Power Farmer).
if __name__=="__main__":
	clear()
	while True:
		main()
