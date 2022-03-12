from ast import Pass
from tracemalloc import stop
import numpy as np
# from nonliving import Ground
# from ant import Ants
# from nonliving import Grass
# from ant_bear import Ant_Bear
# from living_things import creature
from random import choice
import threading as th


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = th.Timer(sec, func_wrapper)
    t.start()
    return t


class World:
    def __init__(self, x, y, time):
        self.grid: np.ndarray = self.fill_world(x, y)
        self.aux_grid: np.ndarray = self.fill_world(x, y)
        self.time = time
        self.interval = None

    def fill_world(self, x, y):
        #
        return np.zeros(shape=([y, x]))

    def get_max_y(self):
        return len(self.grid)

    def get_max_x(self):
        return len(self.grid[0])

    def printworld(self):
        print(self.grid)

    def run(self):

        print(len(self.get_vecinos(0, 0)))
        print(self.get_vecinos(0, 0))
        self.interval = set_interval(self.loop, self.time)

    def stop(self):
        if(self.interval):
            self.interval.cancel()

    def get_vecinos(self, i, j):
        list = []
        for ii in range(max(0, i-1), min(i+2, self.get_max_y())):
            for jj in range(max(0, j-1), min(j+2, self.get_max_x())):
                iii = i + ii - 1
                jjj = j + jj - 1
                if not (iii == i and jjj == j):
                    list.append({
                        'i': iii,
                        'j': jjj,
                        "cell": self.grid[ii][jj]
                    })
        return list

    def update_aux(self, cell, vecinos):
        for vecino in vecinos:
          print(cell, vecinos)
          # Depending on instances modify aux

    def loop(self):
        print('loop')
        self.printworld()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                cell = self.grid[i, j]
                vecinos = self.get_vecinos(i, j)
                self.update_aux(cell, vecinos)
        self.grid = self.aux_grid


myWorld = World(10, 10, 1)

myWorld.run()
