import discord, random, asyncio, logging, colorama
import files.log
import files.information
import files.functions as func
import files.commands as cmd
from files.information import token, prefix
from colorama import init, Fore, Back, Style
init(autoreset=True)

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as '+Fore.GREEN+bot.user.name+Fore.RESET+', id: '+Fore.YELLOW+bot.user.id+Fore.RESET)
    print(Fore.GREEN+bot.user.name+Fore.RESET+' is listening..')
    await bot.change_presence(game=discord.Game(name='say #help'))

@bot.event
async def on_message(message):
    author = message.author
    channel = message.channel
    server = message.server

    # logs
    await cmd.log(message, author, channel, server, bot)
    await cmd.message_limit(message, author, bot)

    # command calls
    if message.author.bot: return
    await cmd.help(message, author, bot)
    await cmd.invite(message, author, server, bot)
    await cmd.kick(message, author, server, bot)
    await cmd.ban(message, author, server, bot)
    await cmd.suspend(message, author, server, bot)

if __name__ == '__main__':
    bot.run(token)
