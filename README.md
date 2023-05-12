# 🚧 voice2note (Under Construction) 🚧

Welcome to voice2note. We are developing a user-friendly chatbot that transcribes voice messages into text, making communication more efficient.

- **Transcription:** Simply send a voice message and voice2note transcribes it into text, eliminating the need for manual note-taking.

- **Grammar Correction:** voice2note incorporates the power of OpenAI's ChatGPT to not just transcribe, but also correct grammatical inaccuracies, resulting in clean, accurate text.

- **Customizable Style:** voice2note offers the flexibility to meet your unique needs. You can specify the style of the corrected transcription, personalizing the output to your preferences.

- **Available on Telegram:** For a start, voice2note will be accessible on Telegram, providing a convenient platform for transforming your spoken words into polished text.

voice2note is designed to streamline your communication process by converting voice messages into grammatically correct, stylistically tailored text. We look forward to sharing more updates soon.


## Tools

- RASA
- google-cloud-speech
- OpenAI chatGPT
- Telegram


## Run

0. Create `credentials.yml`

```bash
python3 utils/create_credentials.py
```

1. Run RASA server:

```bash
 rasa run -m models --enable-api --cors "*" --port 5005
```

2. Run RASA actions:

```bash
rasa run actions --port 5055
```

3. Setup telegram webhook:

```bash
curl -F "url=<RASA_SERVER_URL>/webhooks/telegram/webhook" https://api.telegram.org/bot<TELEGRAM_ACCESS_TOKEN>/setWebhook
```