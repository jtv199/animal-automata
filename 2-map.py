from animals import Animal
from fish import Fish
from bear import Bear

class Map(object):
    """docstring for Map."""
    bounds = (0,0)
    creatures = []
    grid = None

    def __init__(self, bounds = (5,5)):
        super(Map, self).__init__()
        self.bounds = bounds
        self.grid = [[' ' for x in range(bounds[0]+1)] for y in range(bounds[1]+1)]

    def show(self):
        self._draw_creatures()
        for i in range(self.bounds[0]+1):
            print('|', end = '')
            for j in range(self.bounds[1]+1):
                print(self.grid[i][j], end = '')
            pass
            print('|')
        pass

    def spawn(self, animal, pos = (0,0)):
        newAnimal = animal(self.bounds,pos)
        self.creatures.append(newAnimal)
        (x,y) = newAnimal.position
        self.grid[x][y] = newAnimal


        pass

    def _draw_creatures(self):
        self.grid = [[' ' for x in range(self.bounds[0]+1)] for y in range(self.bounds[1]+1)]
        for creature in self.creatures:
            (x,y) = creature.position
            self.grid[x][y] = creature.SYMBOL

    def step(self):
        for creature in self.creatures:

            creature.step()
            ## TODO: feed creatures the grid and record  each move after its made
            ## so that unique creature interactions stays in the animals class
        pass

    def elapse(self, time = 50):
        for i in range(time):
            self.step()
        pass
        for i in self.creatures:
            print(i)

        newMap.show()

if __name__ == '__main__':
    newMap = Map()
    # newMap.spawn(Fish)
    newMap.spawn(Bear)
    newMap.show()
    # newMap.elapse()
    print('checking animal in grid and database')
    print(f' creatures list {newMap.creatures}, grid {newMap.grid}' )
