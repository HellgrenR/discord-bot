import yt_dlp

def get_audio_url(url: str) -> str:
  ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    audio_url = info['url']

  return audio_url