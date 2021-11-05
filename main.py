import Entity
import Scenes

# Links. To which rooms each room links.
# Eventually this will be changed for a outside file.
links = {'Bed': ['Bedroom'], 'Bedroom': ['Corridor'], 'Corridor': ['Bedroom', 'Living Room']}
player = Entity.Player('Wren', 'Bed', 50, 100, 10, 10, 10, 10)
a_scene = Scenes.Scene(player.location, links[player.location])


def run():

    global a_scene

    while True:
        next_scene_name = a_scene.decision()
        if next_scene_name is not None:
            a_scene = Scenes.Scene(next_scene_name, links[next_scene_name])
        player.update()


run()
