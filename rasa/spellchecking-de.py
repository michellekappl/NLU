from typing import Any, Text, Dict, List, Type

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.nlu.tokenizers.tokenizer import Tokenizer
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.constants import (
    TEXT,
    TEXT_TOKENS
)

import string
import nltk
from spellchecker import SpellChecker

nltk.download('omw-1.4')
nltk.download('punkt')

spell = SpellChecker(language="de")

from textblob_de import TextBlobDE

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.MESSAGE_FEATURIZER], is_trainable=False
)
class CorrectSpelling(GraphComponent):

    @classmethod
    def required_components(cls) -> List[Type]:
        """Tokenizer should be included in the pipeline before this component."""
        return [Tokenizer]

    @staticmethod
    def required_packages() -> List[Text]:
        """Required python dependencies"""
        return ["textblob_de", "nltk"]

    def train(self, training_data: TrainingData) -> Resource:
        pass

    @staticmethod
    def supported_languages() -> List[Text]:
        """Determines which languages this component can work with.
            Returns: A list of supported languages.
        """
        return ["de"]

    @classmethod
    def create(
            cls,
            config: Dict[Text, Any],
            model_storage: ModelStorage,
            resource: Resource,
            execution_context: ExecutionContext,
    ) -> GraphComponent:
        return cls()

        def __init__(
                self,
                config: Dict[Text, Any],
                name: Text,
                model_storage: ModelStorage,
                resource: Resource,
        ) -> None:
            super(CorrectSpelling, self).__init__(config)

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        self.process(training_data.training_examples)
        return training_data

    def process(self, messages: List[Message]) -> List[Message]:
        """Retrieve the tokens, do spelling correction and lemmatization,
                pass it to next component of pipeline
        """

        stop_words = set(nltk.corpus.stopwords.words('german'))
        for message in messages:
            tokens = message.get(TEXT_TOKENS)

            if not tokens:
                continue

            for t in tokens:
                new_message = t.text
                new_message = spell.correction(new_message)
                new_message2 = TextBlobDE(new_message)

                if not (new_message in stop_words or new_message2.words.lemmatize()[0] in string.ascii_lowercase):
                    t.text = new_message2.words.lemmatize()[0]
                else:
                    t.text = new_message

            message.set("tokens", tokens)

        return messages
