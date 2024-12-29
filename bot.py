import discord
from discord.ext import commands
import asyncio
import src.audio_handler as AudioHandler
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
        # Check if URL is valid
        if UrlCheck.url_check(url) == False:
          await ctx.send("Invalid URL")
          return

        # Check if bot is in voice channel
        if not self.is_connected(ctx=ctx):
          await self.join_vc(ctx=ctx)

        # Add audio URL to queue
        self.music_queue.append(url)
        await ctx.send("Added to queue")
        await ctx.send(f"Amount of songs: {len(self.music_queue)}")

        # Play audio
        if not ctx.voice_client.is_playing():
          await self.play_audio(ctx=ctx)

      @self.command()
      async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

      @self.command()
      async def stop(ctx):
        await ctx.voice_client.disconnect()
        self.music_queue = []

      @self.command()
      async def queue(ctx):
        await ctx.send(len(self.music_queue))

  def add_events(self):
      @self.event
      async def on_ready():
        print(f"We have logged in as {self.user}")
  

  def is_connected(self, ctx) -> bool:
    return ctx.voice_client is not None and ctx.voice_client.is_connected()

  async def join_vc(self, ctx):
    try:
      voice_channel = ctx.author.voice.channel
      await voice_channel.connect()
    except AttributeError:
      await ctx.send("User not in voice channel")
      return None
  
  async def play_audio(self, ctx):
    if len(self.music_queue) == 0:
      await ctx.voice_client.disconnect()

    audio_url = await AudioHandler.find_audio(ctx=ctx, url=self.music_queue[0])

    if audio_url:
      source = discord.FFmpegPCMAudio(audio_url)
      self.music_queue.pop(0)

      def after_play(error):
        if error:
            print(f"Error in playback: {error}")
        asyncio.run_coroutine_threadsafe(self.play_audio(ctx), self.loop)

      ctx.voice_client.play(source, after=after_play)
    else:
      self.music_queue.pop(0)
      self.play_audio(ctx)