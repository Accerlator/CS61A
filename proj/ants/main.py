from ants import *

if __name__ == "__main__":
    beehive, layout = Hive(AssaultPlan()), dry_layout
    dimensions = (1, 9)
    gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
    place = gamestate.places['tunnel_0_4']
    # fire = FireAnt(armor=1)
    # place.add_insect(fire)
    # place.add_insect(Bee(3))
    # place.add_insect(Bee(5))
    # print("It is running now")
    # place.bees[0].action(gamestate)

    place = gamestate.places["tunnel_0_0"]
    bee = Bee(3)
    ant = FireAnt()
    place.add_insect(bee)
    place.add_insect(ant)
    bee.action(gamestate)
    bee.action(gamestate)
    bee.action(gamestate)