import sys
import opt

if 'opt' in sys.modules:
    DEBUG = opt.DEBUG
else:
    DEBUG = 1

print(f'{__name__} Import DEBUG ADDR:', hex(id(DEBUG)))
print(f'{__name__} Import opt.DEBUG ADDR:', hex(id(opt.DEBUG)))

def dosomething():
    print(f'{__name__} dosomething DEBUG LEVEL:', DEBUG)
    print(f'{__name__} dosomething DEBUG ADDR:', hex(id(DEBUG)))
    print(f'{__name__} dosomething opt.DEBUG ADDR:', hex(id(opt.DEBUG)))
    
    