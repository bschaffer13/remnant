
class Player(object):

    def __init__(self, comlink=None, m1=None, m2=None, m3=None, name='team'):
        self.remnants = list()

        self.enemy_player = None
        self.comlink = comlink
        if m1 is not None:
            self.remnants.append(m1)
        if m2 is not None:
            self.remnants.append(m2)
        if m3 is not None:
            self.remnants.append(m3)
        self.name = name
        for remnant in self.remnants:
            remnant.owner = self

    def __iter__(self):
        return self.remnants.__iter__()

    def __getitem__(self, item):
        return self.remnants[item]

    def remove(self, member):
        if member in self.remnants:
            self.remnants.remove(member)

    def __len__(self):
        return len(self.remnants)

    def get_commands(self, commands):
        pass