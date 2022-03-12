from nonliving import Ground
from living_things import creature
from random import randrange

class Ants (creature):

  def __init__(self):
    super().__init__(life_spawn=20, color='black')
    
    self.sex = self.sex[randrange(0,2)]
    self.reproduction = 0
    self.eat = 0


  def __repr__(self):
    return 'ant'
  
 
 


