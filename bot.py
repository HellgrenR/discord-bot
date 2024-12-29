import discord
from discord.ext import commands
import yt_dlp

class Bot(commands.Bot):
  def __init__(self, prefix ):
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(command_prefix=prefix, intents=intents)

    self.music_queue = []

    self.add_commands()
    self.add_events()

  def add_commands(self):
      @self.command()
      async def play(ctx, *, url):
          try:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
          except AttributeError:
            await ctx.send("Join a voice channel first")
            return
              

          voice_client = ctx.voice_client

          # Add validation to check if the URL is valid

          # Add code to make the bot play the audio from the URL
          ydl = yt_dlp.YoutubeDL()

          with ydl:
              info = ydl.extract_info(url, download=False)
              await ctx.send(f"info title: {info['title']}")


          # Disconnect bot if no longer playing

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