from google import genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = genai.Client()
def transcribe_audio(file_path):
    audio_file = client.files.upload(file=file_path)

    interaction = client.interactions.create(
        model="gemini-3.5-transcribe",
        input=[
            {
                "type": "audio",
                "uri": audio_file.uri,
                "mime_type": audio_file.mime_type,
            }
        ],
    )

    return interaction.output_text

print(transcribe_audio("audio_files/person_a.wav"))