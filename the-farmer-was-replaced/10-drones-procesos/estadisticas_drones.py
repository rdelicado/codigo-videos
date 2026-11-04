# Mide el policultivo con drones: lo que saca y lo que tarda cada vuelta.
import policultivo_drones

# El recurso que da cada planta principal.
recurso = {
	Entities.Tree: Items.Wood,
	Entities.Carrot: Items.Carrot,
	Entities.Grass: Items.Hay
}
vueltas = 10
tamano = 0	# 0 = la granja entera; 12 o 16 la recorta (en Estudio)
item = recurso[policultivo_drones.principal]

# set_world_size limpia la granja: la primera vuelta sale a 0.
if tamano >= 3:
	set_world_size(tamano)
clear()
for i in range(vueltas):
	antes = num_items(item)
	sustancia = num_items(Items.Weird_Substance)
	t0 = get_time()
	policultivo_drones.main()
	quick_print("vuelta", i + 1, "| drones:", max_drones(),
		"| granja:", get_world_size(),
		"| recurso:", num_items(item) - antes,
		"| sustancia:", num_items(Items.Weird_Substance) - sustancia,
		"| s:", get_time() - t0,
		"| energia:", num_items(Items.Power))
