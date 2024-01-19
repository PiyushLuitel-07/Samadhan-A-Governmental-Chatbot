# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions



from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHandleCitizenshipQuery(Action):
    def name(self) -> Text:
        return "action_handle_citizenship_query"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from the user's message
        entities = tracker.latest_message['entities']

        # Default value for citizenship type
        citizenship_type = "unspecified"

        # Check if there are entities
        if entities:
            entity_values = [entity['value'] for entity in entities]
            
            if 'new citizenship' in entity_values:
                citizenship_type = 'new citizenship'
                dispatcher.utter_message(response="utter_new_citizenship_eligibility_criteria")
                dispatcher.utter_message(response="utter_new_citizenship_documents_required")
                dispatcher.utter_message(response="utter_new_citizenship_steps")
            elif 'copy citizenship' in entity_values:
                citizenship_type = 'copy citizenship'
                dispatcher.utter_message(response="utter_copy_citizenship_eligibility_criteria")
                dispatcher.utter_message(response="utter_copy_citizenship_documents_required")
                dispatcher.utter_message(response="utter_copy_citizenship_steps")
            elif 'adopted citizenship' in entity_values:
                citizenship_type = 'adopted citizenship'
                dispatcher.utter_message(response="utter_adopted_citizenship_eligibility_criteria")
                dispatcher.utter_message(response="utter_adopted_citizenship_documents_required")
                dispatcher.utter_message(response="utter_adopted_citizenship_steps")
            else:
                citizenship_type = 'unspecified'
                dispatcher.utter_message(response="utter_citizenship") 

        # Set the slot value for 'citizenship_type'
        return [SlotSet("citizenship_type", citizenship_type)]
        

