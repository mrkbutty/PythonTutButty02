import sys
import opt
from mylib import *

if 'opt' in sys.modules:
    DEBUG = opt.DEBUG
else:
    DEBUG = 0

if __name__=='__main__':
    DEBUG = opt.DEBUG = 2
    print(f'{__name__} DEBUG LEVEL:', DEBUG)
    print(f'{__name__} DEBUG ADDR:', hex(id(DEBUG)))
    print(f'{__name__} opt.DEBUG ADDR:', hex(id(opt.DEBUG)))
    dosomething()