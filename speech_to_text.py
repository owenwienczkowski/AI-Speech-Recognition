# this program transcribes an audio file into text

from openai import OpenAI
from keys import key

client = OpenAI(
    api_key=key
)

audio_file = open("my_audio.m4a", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)