from ast import Pass
import numpy as np
from nonliving import Ground
from ant import Ants
from nonliving import Grass
from ant_bear import Ant_Bear
from living_things import creature
from random import choice

class World :
  def __init__(self,x,y, time):
      self.grid = np.zeros(shape=([y,x]))
      self.time = time

  def printworld (self):
    print(self.grid)

  def first_days (self,ants, antbears, grass):
    counter = 0
    for i in range(len(self.grid)):
      for j in range(len(self.grid[i])):
        counter += 1
    
    print (counter) 
  


  def set_of_actions (self, grid , i ,j):

    max_y = len(grid) 
    max_x = len(grid[0])
    empty__spaces = []
    grass_spaces = []
    ants_spaces = []
    actual_cell = grid [i][j]
    is_living = isinstance(actual_cell,creature)
    #flags
    flag_repro = False 
    done = False
    flag_eat = False
    flag_move = False
    #counter for actions and only act if is living
    
    if is_living:
      reproduction = getattr(grid[i],[j],'reproduction')
      eat = getattr(grid[i],[j],'eat')
      for ii in range(max(0, i-1), min(i+2, max_y)):
        for jj in range(max(0, j-1), min(j+2, max_x)):
          check_cell = grid[ii][jj]
          is_same_cell = (ii, jj) == (i, j)
          is_ant = isinstance(check_cell, Ants)
          is_ant_bear = isinstance(check_cell, Ant_Bear)
          is_grass = isinstance(check_cell, Grass)
        
        if (not is_same_cell and not done and not reproduction  and (is_ant or is_ant_bear) and actual_cell is check_cell and getattr(actual_cell,'sex') != getattr(check_cell,'sex')):
          flag_repro = True
          done = True
          setattr(actual_cell,'reproduction',10)
          if (not eat): setattr(actual_cell,'eat',eat - 1)
        
        if (not is_same_cell and not done and not eat and (  (isinstance(actual_cell, Ants) and is_grass) or (isinstance(actual_cell, Ant_Bear) and is_ant)  )  ):
          flag_eat = True
          done = True
          setattr(actual_cell,'eat',5)

        if (not is_same_cell and not done):
          flag_move = True
          done = True

        if isinstance(check_cell,Ants):ants_spaces.append(check_cell)
        if isinstance(check_cell,Ground):empty__spaces.append(check_cell)
        if isinstance(check_cell,Grass):grass_spaces.append(check_cell)
      
      
      if (flag_repro and len(empty__spaces) ):  
        if (actual_cell is isinstance(actual_cell, Ants)): grid[empty__spaces[0][0]][empty__spaces[0][1]]= Ants ()
        else: grid[empty__spaces[0][0]][empty__spaces[0][1]]= Ant_Bear ()
      if (flag_eat and (len(grass_spaces) or len(ants_spaces)) ):  
        if (actual_cell is isinstance(actual_cell, Ants)): grid[grass_spaces[0][0]][grass_spaces[0][1]]= Ground ()
        else: grid[ants_spaces[0][0]][ants_spaces[0][1]]= Ground ()
      if (flag_move and len(empty__spaces)):  
        aux = choice(empty__spaces)
        grid[aux[0]][aux[1]] = actual_cell
        grid [i][j] = Ground ()
    






#research nditer from numpy
# test = np.arange(4,16).reshape(4,3)
# print(test)
# for i in np.nditer (test, order='C'):
#   print (i, end=',')

# test = [[1,2,3],
#         [4,5,6]]
# print (test)
# for i in range(len(test)):
#   for j in range(len(test[i])):
#     print (test[i][j])