from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

from google import genai
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

client = genai.Client()
def transcribe_audio(file_path):
    started = perf_counter()
    print(f"Uploading {file_path} for transcription...", flush=True)
    audio_file = client.files.upload(file=file_path)

    print(f"Transcribing {file_path}...", flush=True)
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
    
    print(f"Finished {file_path} in {perf_counter() - started:.1f}s.", flush=True)
    return interaction.output_text
def transcribe_both(audio_a, audio_b):
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_a = executor.submit(transcribe_audio, audio_a)
        future_b = executor.submit(transcribe_audio, audio_b)

        transcript_a = future_a.result()
        transcript_b = future_b.result()

    return transcript_a, transcript_b

# def determine_topic(transcription_a, transcription_b):
#     prompt = f"""You are an impartial debate topic generator.

# Given two speech transcripts, identify their central subject and any disagreement
# between the speakers. Create one concise, neutral debate question that captures
# the issue they are discussing.

# Rules:
# - Use both transcripts to determine the topic.
# - Do not invent positions or claims that the speakers did not express.
# - Phrase the topic as a clear question that could reasonably have opposing answers.
# - Do not favor either participant.
# - If the transcripts do not contain a meaningful disagreement or enough information
#   to establish a topic, say so rather than inventing one.

# Person A's transcript:
# {transcription_a}

# Person B's transcript:
# {transcription_b}

# Return only valid JSON. Do not include Markdown, code fences, or any other text.
# Use exactly this format:
# {{
#   "topic": "Should public transit be free for everyone?",
#   "sufficient_disagreement": true
# }}

# When sufficient_disagreement is false, set topic to a concise explanation that
# there is not enough meaningful disagreement or information to establish a debate
# topic."""

#     interaction = client.interactions.create(
#         model="gemini-3.5-flash",
#         input=prompt
#     )

#     return interaction.output_text


def judge_debate(transcription_a, transcription_b):
    started = perf_counter()
    prompt = f"""You are an impartial AI judge evaluating a debate between two participants.

Evaluate both participants' arguments on the given debate topic and determine a
winner based on the quality of their arguments, not on which side you personally
agree with.

Tasks:
    1. Identify the central disagreement.
    2. Formulate a neutral debate question.
    3. Evaluate both arguments on reasoning, evidence,
       relevance, and clarity.
    4. Determine the winner.
    5. Provide a concise, entertaining verdict for text-to-speech output.


Person A's argument:
{transcription_a}

Person B's argument:
{transcription_b}

Score each participant from 0 to 10 in each category:
- Reasoning (45%): logical soundness, coherence, and support.
- Evidence and examples (5%): relevant evidence, facts, or examples.
- Relevance (25%): addressing the topic and opposing position.
- Clarity (15%): clear and effective communication.

Rules:
- Judge both arguments fairly using the same standards.
- The debate is a casual argument, not a formal debate. Focus on the quality of reasoning.
- Do not favor a participant based on speaking style, accent, confidence, or length.
- Do not invent evidence or claims.
- If a transcript is incomplete or unintelligible, acknowledge that limitation.
- The winner must be "A", "B", or "TIE".
- Ensure the weighted totals and winner are consistent.

Return only valid JSON. Do not include Markdown, code fences, or any other text.
Use exactly this structure:
{{
  "winner": "A",
  "scores": {{
    "A": {{
      "reasoning": 8,
      "evidence": 7,
      "relevance_rebuttal": 9,
      "clarity": 8,
      "total": 8.0
    }},
    "B": {{
      "reasoning": 7,
      "evidence": 8,
      "relevance_rebuttal": 6,
      "clarity": 9,
      "total": 7.35
    }}
  }},
  "reasoning": "A wins the debate. A won because... (make it witty while still being fair and impartial). Start by explicitly mentioning who the winner is, and keep it to 30-40 words",
  "strongest_point_A": "...",
  "strongest_point_B": "...",
  "verdict": "A wins this debate!",
  "judge_comment": "A short, fair, witty, and entertaining judicial remark, while still making it clear why they won."
}}"""

    print("Sending debate for judgment...", flush=True)
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )

    print(f"Judgment received in {perf_counter() - started:.1f}s.", flush=True)
    return interaction.output_text
