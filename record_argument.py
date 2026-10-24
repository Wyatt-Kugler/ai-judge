import sounddevice as sd
import soundfile as sf
import os
import threading
import numpy as np

def record_argument(person, duration=30, sample_rate=16000):
    input(f"Press Enter to record Person {person}...")

    print(f"Recording Person {person} for {duration} seconds...")

    chunks = []
    stop_event = threading.Event()

    def capture():
        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
            callback=lambda indata, frames, time, status:
                chunks.append(indata.copy())
        ):
            stop_event.wait()

    thread = threading.Thread(target=capture)
    thread.start()

    input(f"Recording Person {person}. Press Enter to stop...")
    stop_event.set()
    thread.join()

    audio = np.concatenate(chunks, axis=0) 
    audio *= 2

    filename = f"audio_files/person_{person.lower()}.wav"
    os.makedirs("audio_files", exist_ok=True)
    sf.write(filename, audio, sample_rate)

    print(f"Saved {filename}")

