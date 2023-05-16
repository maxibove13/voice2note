from dotenv import load_dotenv
from typing import Any, Text, Dict, List
import os


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")


class ActionUnderConstruction(Action):
    def name(self) -> Text:
        return "action_under_construction"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text")

        style = ""
        prompt = f"""
        You are style corrector assistant.
        Your task is to fix and improve grammatically the given user message.
        Correct punctuation, spelling, and grammar mistakes.
        Always Respond in the same language as the user message.
        Do not respond anything else but the corrected user message.
        User message: ```{user_message}```
        """

        openai.api_key = str(openai_api_key)
        messages = [{"role": "assistant", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1,  # this is the degree of randomness of the model's output
        )
        # answer = self._get_completion(prompt, temperature=0.1)

        dispatcher.utter_message(text=response.choices[0].message["content"])
        return []

    # def _get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
