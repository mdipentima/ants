from living_things import creature
from random import randrange

class Ant_Bear (creature):

  def __init__(self, life_spawn, color):
      super().__init__(life_spawn= 40, color='brown')

      self.sex = self.sex[randrange(0,2)]
      self.reproduction = 0
      self.eat = 0