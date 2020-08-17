# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


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

    # Método que descreve de onde as entidades devem ser extraídas
    # Nesse caso, será extraída uma mensagem completa do usuário caso solicite o slote use_case
    # não precisaremos usar a entidade use_case definida antes
    # permite que seja digitado qualquer coisa pelo usuário para atribuir a valor do slot
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
            "use_case": self.from_text(intent="inform"),
            "person_name": self.from_text(intent="inform")
            }

# lidar com respostas genéricas do usuário
class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    # ação que será disparada como resposta à saudação do usuário
    def name(self):
        return "action_greet"

    # a story utter_greet foi removida do stories.md e será tratada aqui, por action
    # UserUtteranceReverted() é um evento que remove a interação do histórico de diálogo
    # dessa forma, a pessoa pode saudar em qualquer parte da conversa
    # sem afetar a estória de diálogo
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]