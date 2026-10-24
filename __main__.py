print("Loaded __main__.py", flush=True)

import asyncio
import json

def main():
    print("Starting AI Judge...", flush=True)

    # Import the network/audio libraries after the startup message so a slow
    # import cannot make the Run button look like it did nothing.
    from gemini_ai import transcribe_both, judge_debate
    from text_to_speech import text_to_speech
    import playsound

    # Record audio for Person A and Person B
    # record_argument("A", 30)
    # record_argument("B", 30)

    # Transcribe the recorded audio files
    print("Transcribing audio files... this can take a while.", flush=True)
    transcription_a, transcription_b = transcribe_both("audio_files/person_a.wav", "audio_files/person_b.wav")

    print(f"Transcription for Person A: {transcription_a}", flush=True)
    print(f"Transcription for Person B: {transcription_b}", flush=True)

    print("Judging the debate...", flush=True)
    judgment = judge_debate(transcription_a, transcription_b)
    print(f"Debate judgment: {judgment}", flush=True)

    # The model returns JSON text; parse it so the file contains an object,
    # not one large string with escaped newlines and quotes.
    judgment_data = json.loads(judgment)

    with open("Json\\output.json", "w", encoding="utf-8") as f:
        json.dump(judgment_data, f, indent=4, ensure_ascii=False)
        f.write("\n")
    print("Generating spoken verdict...", flush=True)
    asyncio.run(text_to_speech(judgment_data["reasoning"]))
    
    playsound.playsound("audio_files/output.mp3")
   
    
    

if __name__ == "__main__":
    main()
