
import edge_tts


async def text_to_speech(text):
    voice = "en-GB-RyanNeural"
    output = "audio_files/output.mp3"

    tts = edge_tts.Communicate(text, voice)
    await tts.save(output)
