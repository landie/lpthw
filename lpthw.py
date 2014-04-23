import os
class lpthw(object):
    from os import listdir
    from os.path import isfile, join
    files = [ f for f in listdir(os.curdir) if os.path.isfile(f)]
    files.sort()
    for f in files:
      if f.startswith("ex0"):
          print("---------------------------------------")
          print(f)
          __import__(f.strip(".py"))
          print("---------------------------------------")  
          
#    import ex26 
#   commented since ex26 requires ex25 to run and i cant be bothered.