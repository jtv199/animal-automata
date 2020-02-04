from animals import Animal

class Fish(Animal):
    """docstring for Fish."""
    SYMBOL = '*'

    def __init__(self, bounds= (5,5),position = (0,0)):
        super(Fish, self).__init__(bounds,position)

    def spawn_actions(self):
        print('Fish has been spawned [*]')
        pass

if __name__ == '__main__':
    newFish = Fish()
    print(newFish)
    newFish.step()
    newFish._move_around()
