import colorama
import discord
import files.information
import files.functions as func
from colorama import init, Fore, Back, Style
from files.information import prefix, add_role, log_channel, character_limit
init(autoreset=True)
print(__name__ + '.py ' + Fore.GREEN + 'loaded')

# kick
async def kick(message, author, server, bot):
    """\n#kick [user, reason] : Kicks a user within the discord (Admin, Moderator Only)"""
    if func.message_sw(message, 'kick'):
        msg = message.content.split(' ',2)
        channel = discord.utils.get(message.server.channels, name=log_channel)
        try:
            if message.mentions[0] and msg[0] and msg[2]:
                if func.has_roles(message, 'Admin', 'Moderator'):
                    # pm user, modlog, kicks
                    await bot.send_message(message.mentions[0],'You have been **KICKED** from *'+server.name+'* by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"')
                    await bot.send_message(channel,'ID = '+str(mssage.mentions[0].id)+' <@'+str(message.mentions[0].id)+'> has been **KICKED** by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"')
                    await bot.kick(message.mentions[0])
                else:
                    await func.error_function(kick.__name__, 'Insufficent Permissions', message, author, bot)
        except:
            await func.error_function(kick.__name__, 'Invalid Syntax', message, author, bot)

# ban
async def ban(message, author, server, bot):
    """\n#ban [user, reason] : Bans a user within the discord (Admin Only)"""
    if func.message_sw(message, 'ban'):
        msg = message.content.split(' ',2)
        channel = discord.utils.get(message.server.channels, name=log_channel)
        try:
            if message.mentions[0] and msg[0] and msg[2]:
                if func.has_roles(message, 'Admin'):
                    # pm user, modlog, kicks
                    await bot.send_message(message.mentions[0],'You have been **BANNED** from *'+server.name+'* by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"\nYou may request an appeal here : https://goo.gl/trptWd')
                    await bot.send_message(channel,'ID = '+str(mssage.mentions[0].id)+' <@'+str(message.mentions[0].id)+'> has been **BANNED** by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"')
                    await bot.ban(message.mentions[0])
                else:
                    await func.error_function(ban.__name__, 'Insufficent Permissions', message, author, bot)
        except:
            await func.error_function(ban.__name__, 'Invalid Syntax', message, author, bot)

# suspend
async def suspend(message, author, server, bot):
    """\n#suspend [user, reason] : Suspends a user within the discord (Admin, Moderator Only)"""
    if func.message_sw(message, 'suspend'):
        msg = message.content.split(' ',2)
        channel = discord.utils.get(message.server.channels, name=log_channel)
        adding_role = discord.utils.get(message.server.roles, name=add_role)
        try:
            if message.mentions[0] and msg[0] and msg[2]:
                if func.has_roles(message, 'Admin'):
                    # pm user, modlog, removes roles, add roles
                    await bot.send_message(message.mentions[0],'You have been **SUSPENDED** from *'+server.name+'* by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"\nSuspension information can be found here : https://goo.gl/GzXRoI')
                    await bot.send_message(channel,'ID = '+str(mssage.mentions[0].id)+' <@'+str(message.mentions[0].id)+'> has been **SUSPENDED** by a staff member, issued at *'+str(message.timestamp)+'* for : \"'+msg[2]+'\"')
                    await bot.replace_roles(message.mentions[0],adding_role)
            else:
                await func.error_function(suspend.__name__, 'Insufficent Permissions', message, author, bot)
        except:
            await func.error_function(suspend.__name__, 'Invalid Syntax', message, author, bot)

# invite
async def invite(message, author, server, bot):
    """\n#invite, #inv : Creates a new invite link for the server"""
    if func.message_sw(message, 'invite', 'inv'):
        await bot.send_message(author,server.name+' Discord Invite : '+str(await bot.create_invite(server, temporary=True)))

# cmd_list, for help()
def cmd_list(bot):
    return bot.user.name+' command list\n```'+help.__doc__+invite.__doc__+kick.__doc__+ban.__doc__+suspend.__doc__+'```'

# help
async def help(message, author, bot):
        """#help : PM\'s list of commands"""
        if func.message_sw(message, 'help'):
            await bot.send_message(author,cmd_list(bot))

# logs
async def log(message, author, channel, server, bot):
    if message.content:
        try:
            if not channel.is_private:
                if author.id == bot.user.id:
                    print(Fore.YELLOW+author.name+Fore.RESET+' messaged '+Fore.YELLOW+'\"'+message.content+'\"'+Fore.RESET+' on server '+Fore.YELLOW+server.name+Fore.RESET+' on channel '+Fore.YELLOW+channel.name)
                else:
                    print(Fore.GREEN+author.name+Fore.RESET+' messaged '+Fore.YELLOW+'\"'+message.content+'\"'+Fore.RESET+' on server '+Fore.YELLOW+server.name+Fore.RESET+' on channel '+Fore.YELLOW+channel.name)
            if channel.is_private:
                print(Fore.GREEN+author.name+Fore.RESET+' PM\'ed '+Fore.YELLOW+'\"'+message.content+'\"')
        except:
            print(Force.RED+'Unkown Error')
            pass

# message limit
async def message_limit(message, author, bot):
    if len(message.content) >= character_limit:
        await bot.send_message(author, 'Your message exceeded the max character limit; your message has been deleted')
        await bot.delete_message(message)
