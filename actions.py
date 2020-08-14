# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    # Método que retorna o nome que será usado nas stories
    def name(self):
        return "sales_form"

    # Método que especifica quais informações solicitar, ou seja, quais slots devem ser preenchidos
    @staticmethod
    def required_slots(tracker):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
            ]

    # Método que "faz algo" com as informações que o usuário forneceu
    # quando o formulário estiver completo
    # Nesse caso é informado ao usuário que entraremos em contato com ele
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []