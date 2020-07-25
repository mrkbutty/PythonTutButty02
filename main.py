import sys
import mylib
import mysound
import mysound.manage
from mysound.formats import *
from mysound.effects import *
import mysound.effects.echo as ee
import mysound.effects.echo


print(f'Now initialising {__name__}')


def main():
    print(f'\nPython search path for library modules: {sys.path}\n')
    
    mainflag = True
    print(f'dir in main function: {dir()}')
    print(f'dir of mylib: {dir(mylib)}')
    mylib.sayhello(__name__)
    
    print(f'\ndir of mysound: {dir(mysound)}')
    print(f'dir of mysound.manage: {dir(mysound.manage)}')
    mysound.manage.sayhello(__name__)
    
    print(f'\ndir of wav: {dir(wav)}')
    wav.sayhello(__name__)
    
    print(f'\ndir of mp3: {dir(mp3)}')
    mp3.sayhello(__name__)
    
    print(f'\ndir of ee: {dir(ee)}')
    print(f'dir of mysound.effects.echo: {dir(mysound.effects.echo)}')
    print(f'ee is echo: {ee is mysound.effects.echo}')

    ee.sayhello(__name__)
    print(f'\nVolume is {ee.volume}')
    ee.volume = 11
    print(f'Volume is {mysound.effects.echo.volume}')

    def goodbye(s):
        print(f'\nGoodbye {s} from {__name__}')
    
    ee.sayhello = goodbye
    ee.sayhello(__name__)


if __name__ == '__main__':
    print(f'dir in {__name__}: {dir()}')
    sys.exit(main())