import logging
import os
import requests

import openai
from pydub import AudioSegment

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VoiceToText:
    def __init__(self, bot_token, openai_api_key):
        self.bot_token = bot_token
        self.api_key = openai_api_key

    def _download_file_from_telegram(self, file_id):
        logger.debug(f"Downloading file {file_id} from Telegram")
        url = f"https://api.telegram.org/bot{self.bot_token}/getFile?file_id={file_id}"
        response = requests.get(url).json()

        file_path = response["result"]["file_path"]
        download_url = f"https://api.telegram.org/file/bot{self.bot_token}/{file_path}"

        file_data = requests.get(download_url).content

        with open("voice.ogg", "wb") as file:
            file.write(file_data)

        sound = AudioSegment.from_ogg("voice.ogg")
        sound.export("voice.wav", format="wav")

    def speech_recognition(self, file_id):
        # Download the voice file from Telegram
        self._download_file_from_telegram(file_id)

        # Transcribe the audio file using OpenAI's Whisper ASR API
        openai.api_key = self.api_key
        with open("voice.wav", "rb") as audio_file:
            result = openai.Audio.transcribe("whisper-1", audio_file)

        return result["text"]
