# Measures 3 rounds of each program: ticks, seconds and coal per round.
import coal_one
import coal_drones

rounds = 3


def measure(name, program):
	for i in range(rounds):
		coal = num_items(Items.Coal)
		t0 = get_tick_count()
		s0 = get_time()
		program()
		quick_print(name, i + 1,
			"| ticks:", get_tick_count() - t0,
			"| s:", get_time() - s0,
			"| coal:", num_items(Items.Coal) - coal,
			"| size:", get_world_size(),
			"| drones:", max_drones())

measure("one", coal_one.coal_round)
measure("drones", coal_drones.coal_round)
