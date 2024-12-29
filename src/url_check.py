import re

def url_check(url: str) -> bool:
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(m\.)?(youtube\.com|youtu\.?be)/.+$'
    )
    return bool(youtube_regex.match(url))