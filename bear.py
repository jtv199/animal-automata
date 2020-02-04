from animals import Animal

class Bear(Animal):
    """docstring for Bear."""
    SYMBOL = '@'

    def __init__(self, bounds= (5,5),position = (0,0)):
        super(Bear, self).__init__( bounds,position)

    def spawn_actions(self):
        print(f'Bear has been spawned [@] at {self.position}, with bounds at {self.bounds}')
        pass

if __name__ == '__main__':
    newBear = Bear()
    print(newBear)
    newBear.step()
    newBear._move_around()
