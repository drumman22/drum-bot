import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(__name__ + '.py ' + Fore.GREEN + 'loaded')

token = 'token_goes_here'
prefix = '#'

# character limit command
character_limit = 200

# suspend command
add_role = 'Suspended'

# log channel
log_channel = 'modlog'
