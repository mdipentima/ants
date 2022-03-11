from world import World
import living_things
from ant import Ants




def main():
  mundo = World(10,10,2000)
  mundo.printworld()
  mundo.first_days(1,1,1)

  anty = Ants ()



  print (mundo.__class__.__name__)
  print (anty.__class__.__name__)
  print (anty.__repr__())
  test = getattr(anty,'eat')
  sex = anty.sex
  test = 10
  print(anty.eat)
  # import importlib
  # my_module = importlib.import_module("ant")
  # MyClass = getattr(my_module, "Ants")
  # instance = MyClass()




  

if __name__ == "__main__":
    main()


