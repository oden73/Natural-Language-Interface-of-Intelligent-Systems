from pymorphy2 import MorphAnalyzer

from helper.reverse_replace_helper import ReverseReplaceHelper


class WordFormGenerationController:
    def __init__(self) -> None:
        self.__morph_analyzer: MorphAnalyzer = MorphAnalyzer()
        self.__helper: ReverseReplaceHelper = ReverseReplaceHelper()

    def word_form_generation(self, params: dict) -> str:
        parsed_lexeme = self.__morph_analyzer.parse(params['Лексема'])[0]

        word_form = parsed_lexeme.inflect({
            params['Падеж'],
            params['Род'],
            params['Число']
        })

        return word_form.word if word_form else params['Лексема']
