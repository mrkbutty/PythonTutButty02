import options, tools

print(f'Now initialising {__name__}')

def about():
    print(f'{__name__}: {options.NAME} Ver: {options.VERSION}')

def sayhello(s):
    print(f'Hello {s} from {__name__} VOL:{options.volume}')
    print('Changing volume...')
    tools.set_vol(__name__, 11)