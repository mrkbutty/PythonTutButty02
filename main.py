import sys

import options
import tools
import sound
import sound.manage
from sound.formats import *
from sound.effects import *
print('Finished importing * from effects')
import sound.effects.echo as ee
import sound.effects.echo


print(f'Now initialising {__name__}: {options.NAME} ver {options.VERSION}')


def main():
    print(f'\nPython search path for library modules: {sys.path}\n')
    
    tools.sayhello(__name__)
    sound.manage.about()

    mp3.sayhello(__name__)
    
    sound.manage.sayhello(__name__)
    print(f'main now sees volume as {options.volume}')

    wav.sayhello(__name__)
    
    print(f'ee is echo: {ee is sound.effects.echo}')

    ee.sayhello(__name__)
    print(f'Decay is {ee.decay}')
    ee.decay = 1
    print(f'Decay is {sound.effects.echo.decay}')

    def goodbye(s):
        print(f'\nGoodbye {s} from {__name__}')
    
    ee.sayhello = goodbye
    ee.sayhello(__name__)


if __name__ == '__main__':
    sys.exit(main())