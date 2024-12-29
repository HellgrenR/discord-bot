import yt_dlp

class VideoTooLongError(Exception):
  pass

def get_audio_url(url: str) -> str:
  ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    audio_url = info['url']

  if info["duration"] > 3600:
    raise VideoTooLongError("Video exceeds 1 hour")

  return audio_url