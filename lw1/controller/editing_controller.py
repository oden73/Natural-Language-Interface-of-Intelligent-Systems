from pymorphy2 import MorphAnalyzer

from model.Word import Word
from helper.reverse_replace_helper import ReverseReplaceHelper


class EditingController:
    def __init__(self) -> None:
        self.__helper: ReverseReplaceHelper = ReverseReplaceHelper()
        self.__morph_analyzer: MorphAnalyzer = MorphAnalyzer()

    def edit_word(self, word: Word, params: dict) -> Word:
        new_word_object: Word = word

        new_case: str = params['Падеж']
        new_number: str = params['Число']

        parsed_lexeme = self.__morph_analyzer.parse(word.lexeme)[0]
        new_word_form = parsed_lexeme.inflect({
            self.__helper.case_dict[new_case],
            self.__helper.gender_dict[word.gender],
            self.__helper.number_dict[new_number]
        })

        new_word_object.word = new_word_form.word if new_word_form else word.lexeme
        new_word_object.case = new_case
        new_word_object.number = new_number

        return new_word_object
