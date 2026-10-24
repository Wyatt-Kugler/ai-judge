# AI Judge

AI Judge compares two recorded arguments, asks Gemini to transcribe and score them, saves the result as JSON, and reads the written verdict aloud.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- Two argument recordings saved as WAV files
- A working audio output device; microphone access is needed if you use the recording helper

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and add your API key:

```text
GEMINI_API_KEY=your_api_key_here
```

The Google Gen AI client reads `GEMINI_API_KEY` from the environment. Keep the key private; `.env` is excluded from Git.

## Prepare the audio

Place the recordings at these paths:

```text
audio_files/person_a.wav
audio_files/person_b.wav
```

The current app expects those files to exist before launch. `record_argument.py` contains a microphone recording helper, but its calls are commented out in `__main__.py`; recording does not start automatically.

## Run

From the project root, run either entry point:

```powershell
python __main__.py
```

or, for IDE configurations targeting `main.py`:

```powershell
python main.py
```

The app transcribes both recordings, evaluates the arguments, writes the structured judgment to `Json/output.json`, generates a spoken version of the reasoning, and plays it from `audio_files/output.mp3`. Gemini calls require an internet connection.

## Project files

- `__main__.py` — application workflow and output playback
- `gemini_ai.py` — Gemini transcription and debate evaluation
- `record_argument.py` — optional microphone recording helper
- `text_to_speech.py` — spoken verdict generation
- `Json/output.json` — generated judgment
- `audio_files/` — input recordings and generated speech
