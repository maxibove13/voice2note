from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import INTENT
from rasa.shared.nlu.training_data.training_data import TrainingData


@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True
)
class MonoIntentClassifier(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        pass

    def train(self, training_data: TrainingData) -> Resource:
        pass

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            intent = {"name": "user_message", "confidence": 1.0}
            intent_ranking = [{"confidence": 1.0, "name": "general_search"}]

            message.set(INTENT, intent, add_to_output=True)
            message.set("intent_ranking", intent_ranking)
        return messages
