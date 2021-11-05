import GUI


class Scene:

    def __init__(self, name, links, items=None):
        self.name = name
        self.links = links
        self.items = items

    def decision(self):
        GUI.readroomdesc(self.name)
        dec = GUI.navigate(self.links)
        return dec
