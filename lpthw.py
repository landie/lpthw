import os
class lpthw(object):
    from os import listdir
    from os.path import isfile, join
    files = [ f for f in listdir(os.curdir) if os.path.isfile(f)]
    for f in files:
      if f.startswith("ex"):
          __import__(f.strip(".py"))
          