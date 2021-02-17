import options

print(f'Now initialising {__name__}')

def sayhello(s):
    print(f'Hello {s} from {__name__}')
    print(f'{__name__}: {options.NAME} Version:{options.VERSION}')

def set_vol(s, vol):
    print(f'Hello {s} setting vol to {vol}')
    options.volume = vol

