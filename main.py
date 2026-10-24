from record_argument import record_argument
from gemini_ai import transcribe_audio, determine_topic, judge_debate

def main():
    # Record audio for Person A and Person B
    record_argument("A", 30)
    record_argument("B", 30)

    # Transcribe the recorded audio files
    transcription_a = transcribe_audio("audio_files/person_a.wav")
    transcription_b = transcribe_audio("audio_files/person_b.wav")

    print(f"Transcription for Person A: {transcription_a}")
    print(f"Transcription for Person B: {transcription_b}")

    topic = determine_topic(transcription_a, transcription_b)
    judgment = judge_debate(topic, transcription_a, transcription_b)
    print(f"Debate judgment: {judgment}")
