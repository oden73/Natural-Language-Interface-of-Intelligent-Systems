from pymorphy2 import MorphAnalyzer

from helper.reverse_replace_helper import ReverseReplaceHelper


class WordFormGenerationController:
    def __init__(self, lexeme: str, case: str, gender: str, number: str) -> None:
        self.__morph_analyzer: MorphAnalyzer = MorphAnalyzer()
        self.__helper: ReverseReplaceHelper = ReverseReplaceHelper()

        self.__lexeme: str = lexeme
        self.__case: str = self.__helper.case_dict[case]
        self.__gender: str = self.__helper.gender_dict[gender]
        self.__number: str = self.__helper.number_dict[number]

    def word_form_generation(self) -> str:
        parsed_lexeme = self.__morph_analyzer.parse(self.__lexeme)[0]

        word_form = parsed_lexeme.inflect({
            self.__case,
            self.__gender,
            self.__number
        })

        return word_form.word if word_form else self.__lexeme
