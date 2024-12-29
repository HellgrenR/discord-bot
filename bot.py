import discord
from discord.ext import commands
import yt_dlp
import src.audio_finder as AudioFinder
import src.url_check as UrlCheck

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
      async def play(ctx, *, url: str):
        if UrlCheck.url_check(url) == False:
          await ctx.send("Invalid URL")
          return

        try:
          voice_channel = ctx.author.voice.channel
          await voice_channel.connect()
        except AttributeError:
          await ctx.send("User not in voice channel")
          return

        try:
          audio_url = AudioFinder.get_audio_url(url=url)
        except yt_dlp.DownloadError:
          await ctx.send("Could not find audio")
          await ctx.voice_client.disconnect()
          return

        source = discord.FFmpegPCMAudio(audio_url)
        voice_client = ctx.voice_client
        voice_client.play(source)

        # Disconnect bot if no longer playing

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