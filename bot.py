import discord
from discord.ext import commands

class Bot(commands.Bot):
  def __init__(self, prefix ):
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(command_prefix=prefix, intents=intents)

    self.add_commands()
    self.add_events()

  def add_commands(self):
      @self.command()
      async def ping(ctx):
          await ctx.send('pong')

      @self.command()
      async def hello(ctx):
          await ctx.send(f"Hello! I'm {self.user}. How can I assist you today?")

      @self.command()
      async def join(ctx):
          channel = ctx.author.voice.channel
          await channel.connect()

      @self.command()
      async def leave(ctx):
          await ctx.voice_client.disconnect()

  def add_events(self):
      @self.event
      async def on_ready():
          print(f"We have logged in as {self.user}")