
import asyncio
from email.mime import audio
import os
import edge_tts
import json


async def text_to_speech():
    json_file = "Json/output.json"

    with open(json_file, "r") as f:
        data = json.load(f)
    

    text = data['reasoning']
    voice = "en-GB-RyanNeural"
    output = "audio_files/output.mp3"

   
    tts = edge_tts.Communicate(text, voice)
    await tts.save(output)

        

asyncio.run(text_to_speech())
