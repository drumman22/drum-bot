import colorama
import discord
import files.information
from colorama import init, Fore, Back, Style
from files.information import prefix
init(autoreset=True)
print(__name__ + '.py ' + Fore.GREEN + 'loaded')

# error_function print format
async def error_function(function_name, error_type, message, author, bot):
    await bot.send_message(author,'Error : '+error_type+', '+function_name+' Function\n```Input : '+message.content+'```')
    print(Fore.RED+'Error : '+error_type+Fore.RESET+', '+Fore.YELLOW+function_name+Fore.RESET+' Function')

# bool, message_sw,
def message_sw(message, cmd_1, cmd_2 = None):
    if cmd_1 and cmd_2:
        if message.content.startswith(prefix+cmd_1) or message.content.startswith(prefix+cmd_2):
            return True
    elif cmd_1:
        if message.content.startswith(prefix+cmd_1):
            return True
    else:
        return False

# bool, checks for id
def is_owner(message):
    if message.author.id == message.server.owner.id:
        return True
    else:
        return False

# bool, checks for roles
def has_roles(message, role_1, role_2 = None):
    has_role_1 = discord.utils.get(message.server.roles, name=role_1)
    print(str(role_1))
    print(str(has_role_1))
    if role_1 and role_2:
        has_role_2 = discord.utils.get(message.server.roles, name=role_2)
        for i in message.author.roles:
            if i == has_role_1 or i == has_role_2:
                return True
    elif role_1:
        for i in message.author.roles:
            if i == has_role_1:
                return True
    else:
        return False
