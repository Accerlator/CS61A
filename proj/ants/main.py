import ants, importlib
importlib.reload(ants)
from ants import *

if __name__ == "__main__":
    beehive = ants.Hive(ants.AssaultPlan())
    dimensions = (2, 9)
    gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
    ants.bees_win = lambda: None
    # QueenAnt Placement
    queen = ants.QueenAnt()
    gamestate.places['tunnel_0_2'].add_insect(queen)
    queen.action(gamestate)
# Attack a bee
    bee = ants.Bee(3)
    gamestate.places['tunnel_0_4'].add_insect(bee)
    queen.action(gamestate)
    print(bee.armor) # Queen should still hit the bee