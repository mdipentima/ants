from ast import Pass
from multiprocessing.dummy import Array
from random import choice
from tkinter import Grid

class creature:
  
  def __init__(self, life_spawn, color):
 

    #attributes that define a creature
    self.sex = {
            0 : 'male',
            1 : 'female',
    }
    
    self.life_spwan = life_spawn
    # self.alive = 'yes'
    self.color = color
    self.flag_movement = False
    

    #possible movement of creatures in x-y
    self.direction = ([0,-1],[0,1], [1,0], [-1,0], [1,-1], [1,1], [-1,-1], [-1,1])
    

  # def movement(self, grid): 
    
  #   max_y = len(grid) - 1
  #   max_x = len(grid[0]) - 1
  #   aux_x = 0
  #   aux_y = 0

  #   move = choice(self.direction)
  #   if (self.y == 0 and move[1] == -1) :
  #     aux_y = 0
  #   elif (self.y == max_y and move[1] == 1):
  #     aux_y = 0
  #   else:
  #     aux_y += move[1]

  #   if (self.x == 0 and move[0] == -1) :
  #     aux_x = 0
  #   elif (self.x == max_x and move[0] == 1):
  #     aux_x =  0
  #   else:
  #     aux_x += move[0]

  #   if (grid[aux_x][aux_y].__class__.__name__ == 'Ground'):
  #       self.y = aux_y
  #       self.x = aux_x
    
  #   self.life_spwan -= 1
  
 
    