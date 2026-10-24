import sounddevice as sd
import soundfile as sf
import os

def record_argument(person, duration=30, sample_rate=16000):
    input(f"Press Enter to record Person {person}...")

    print(f"Recording Person {person} for {duration} seconds...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    audio *= 2

    filename = f"audio_files/person_{person.lower()}.wav"
    os.makedirs("audio_files", exist_ok=True)
    sf.write(filename, audio, sample_rate)

    print(f"Saved {filename}")

record_argument("A", 5)
record_argument("B", 5)
