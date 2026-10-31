# Policultivo (The Farmer Was Replaced)
# Un solo programa para árboles, zanahorias y hierba. Tablero de ajedrez: las casillas
# pares llevan la planta principal y las impares, las compañeras que piden. Cada vuelta
# cosecha lo plantado en la anterior, así que la primera sale a cero.

# Solo se tocan estas tres líneas:
# - principal: Entities.Tree, Entities.Carrot o Entities.Grass.
# - companeros: False para comparar sin plantar compañeras.
# - fertilizar: True para sacar Sustancia Rara (la mitad de la cosecha sale en sustancia).
principal = Entities.Tree
companeros = True
fertilizar = False

# Qué objeto da cada planta, para contar lo que se gana.
recurso = {
	Entities.Tree: Items.Wood,
	Entities.Carrot: Items.Carrot,
	Entities.Grass: Items.Hay
}
# Qué terreno necesita cada planta.
suelo = {
	Entities.Tree: Grounds.Grassland,
	Entities.Bush: Grounds.Grassland,
	Entities.Grass: Grounds.Grassland,
	Entities.Carrot: Grounds.Soil
}

# Cambia el terreno si no es el que toca: no hace falta saber qué había antes.
def preparar_suelo(planta):
	if get_ground_type() != suelo[planta]:
		till()

# Apunta la compañera que pide la planta de debajo del dron. Los pedidos de casilla par
# (ahí ya hay una principal) o de una casilla ya pedida se pierden.
def apuntar_compi(pedidos):
	compi = get_companion()
	if compi != None:
		tipo, (x, y) = compi
		if (x + y) % 2 == 1 and (x, y) not in pedidos:
			pedidos[(x, y)] = tipo

# Primera pasada, por las casillas pares: cosecha la planta de la vuelta anterior (aquí se
# cobra el policultivo), planta otra, riega, fertiliza si toca y apunta su pedido.
def plantar_principales():
	pedidos = {}
	n = get_world_size()
	for x in range(n):
		for y in range(n):
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
				if companeros:
					apuntar_compi(pedidos)
			move(North)
		move(East)
	return pedidos

# Segunda pasada: solo se para en las casillas pedidas y planta lo que le han pedido.
def plantar_compis(pedidos):
	n = get_world_size()
	for x in range(n):
		for y in range(n):
			if (x, y) in pedidos:
				harvest()
				preparar_suelo(pedidos[(x, y)])
				plant(pedidos[(x, y)])
			move(North)
		move(East)

# Una vuelta completa, y escribe lo que ha ganado y lo que ha tardado.
def main():
	antes = num_items(recurso[principal])
	sustancia = num_items(Items.Weird_Substance)
	t0 = get_time()
	pedidos = plantar_principales()
	plantar_compis(pedidos)
	quick_print(
		"recurso:", num_items(recurso[principal]) - antes,
		"sustancia:", num_items(Items.Weird_Substance) - sustancia,
		"segundos:", get_time() - t0, "compis:", len(pedidos))

if __name__ == "__main__":
	clear()
	while True:
		main()
