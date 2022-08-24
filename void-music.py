import discord
from discord.ext import commands
from helpcog import HelpCog
from musiccog import MusicCog


TOKEN = None #bot token goes here
intents = discord.Intents.default()


bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)
bot.remove_command('help')
bot.add_cog(HelpCog(bot))
bot.add_cog(MusicCog(bot))
bot.run(TOKEN)
