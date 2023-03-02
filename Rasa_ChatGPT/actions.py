import openai
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionChatGPT(Action):
    def name(self) -> Text:
        return "action_chatgpt"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prompt = tracker.latest_message.get('text')
        model_engine = "text-davinci-003"
        openai.api_key = os.environ["OPENAI_API_KEY"]
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        chat_response = response.choices[0].text
        dispatcher.utter_message(chat_response)

        return []
