import sys
import mylib
import mysound
import mysound.manage
from mysound.formats import *
import mysound.effects.echo as eo
import mysound.effects.echo


print(f'Now initialising {__name__}')


def main():
    print(dir())
    print(dir(mylib))
    mylib.sayhello(__name__)
    print(dir(mysound))
    print(dir(mysound.manage))
    mysound.manage.sayhello(__name__)
    print(dir(wav))
    wav.sayhello(__name__)
    print(dir(mp3))
    mp3.sayhello(__name__)
    print(dir(eo))
    print(dir(mysound.effects.echo))
    print(f'eo is echo: {eo is mysound.effects.echo}')

    eo.sayhello(__name__)
    print(f'Volume is {eo.volume}')
    eo.volume = 11
    print(f'Volume is {mysound.effects.echo.volume}')

    def goodbye(s):
        print(f'Goodbye {s} from {__name__}')
    
    eo.sayhello = goodbye
    eo.sayhello(__name__)


if __name__ == '__main__':
    sys.exit(main())