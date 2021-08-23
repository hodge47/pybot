import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='?')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name='pong')
async def _pong(ctx):
    await ctx.send(f'pong')


bot.run(config.discord_token)