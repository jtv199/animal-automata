from abc import ABCMeta, abstractmethod
from random import randrange



class Animal(metaclass=ABCMeta):
    """docstring for animal."""

    bounds = None
    position = None
    LOWER_BOUNDS = (0,0)
    DIRECTIONS = {
    #represents c,n,e,s,w
        0:(0,0),
        1:(0,1),
        2:(1,0),
        3:(0,-1),
        4:(-1,0)

        }
    grid = None

    def __init__(self, bounds= (5,5),position = (0,0)):
        super(Animal, self).__init__()
        self.bounds = bounds
        self.position = position
        self.spawn_actions()

    def spawn_actions(self):
        print('animal has been spawned')
        pass

    def in_bounds(self,newpos):
        if all(list(map(lambda x, y,z : x<=y<=z,self.LOWER_BOUNDS,newpos,self.bounds ))) :
            return True
        return False


    def move_in( self, moves):
        print('moves',moves)
        #check if able to move, if not, return none
        try:
            newpos = tuple(map(lambda x, y : x+y,self.position ,moves ))
            if self.in_bounds(newpos) and not self._collision(newpos) :
                self.position = newpos
                return newpos
            else:
                return None
        except Exception as e:
            print('move_in error, are you using tuples as moves??')
            raise e

    def move(self, speed =1, direction = randrange(0,5)):
        # checks if able to move, if not call move_in again
        dir = self.DIRECTIONS[direction]
        while not self.move_in(dir):
            dir = self.DIRECTIONS[randrange(0,5)]
            # print(dir)
            pass

    def _collision(self,newpos):
        """ takes newpos, is called every move_in to see what it collides with,
        then calls the add function"""
        if self.grid[newpos[0]][newpose[1]] == ' ':

            return False
            pass

        self+self.grid[newpos[0]][newpose[1]]
        return self.grid[newpos[0]][newpose[1]]


    def step(self):
        """ either move or stay"""
        self.move()
        pass


    def __add__(self,other):
        if type(self) is type(other):
            print('we ar both', type(self))
        else:
            print ('i am ', type(self), 'other is ', type(other))

    def __str__(self):
        return '<' +  self.__class__.__name__ + ' , Location: ' + str(self.position) + '>'
        pass

    def _move_around(self,time=50):
        for i in range(time):
            self.step()
            print(self)
        pass


if __name__ == '__main__' :
    testAnimal = Animal()
    print(testAnimal)
    testAnimal.step()
    print('should have moved in a direction', testAnimal)
    print('testing moving a lot')
    testAnimal._move_around()
    print('------testing colision -----')
    testAnimal2 = Animal((5,5),(testAnimal.position[0]+1,testAnimal.position[1]))
    print(f'spawned testAnimal2{testAnimal2.position} right of testAnimal1{testAnimal1.position}, now moving to collide')
    testAnimal2.move(1,(-1,0))
    print(f'{testAnimal}, {testAnimal2}, they should have moved appart and print collision message')
