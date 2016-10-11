import logging
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(__name__ + '.py ' + Fore.GREEN + 'loaded')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.logs', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
