from record_argument import record_argument
from gemini_ai import transcribe_both, determine_topic, judge_debate
import json

def main():
    # Record audio for Person A and Person B
    # record_argument("A", 30)
    # record_argument("B", 30)

    # Transcribe the recorded audio files
    transcription_a, transcription_b = transcribe_both("audio_files/person_a.wav", "audio_files/person_b.wav")

    print(f"Transcription for Person A: {transcription_a}")
    print(f"Transcription for Person B: {transcription_b}")

    topic = determine_topic(transcription_a, transcription_b)
    judgment = judge_debate(topic, transcription_a, transcription_b)
    print(f"Debate judgment: {judgment}")

    # The model returns JSON text; parse it so the file contains an object,
    # not one large string with escaped newlines and quotes.
    judgment_data = json.loads(judgment)

    with open("Json\\output.json", "w", encoding="utf-8") as f:
        json.dump(judgment_data, f, indent=4, ensure_ascii=False)
        f.write("\n")

main()
