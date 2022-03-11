import threading as th 

def set_interval(func, sec):
  def func_wrapper():
      set_interval(func, sec)
      func()
  t = th.Timer(sec, func_wrapper)
  t.start()
  return t


