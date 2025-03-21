import json

from model.Word import Word


class SaveController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def __form_json(word_list: list[Word]) -> str:
        word_dict_list: list[dict] = []

        for word in word_list:
            word_dict: dict = {
                'Word': word.word,
                'Start': word.start_pos,
                'Stop': word.stop_pos,
                'Morphology': {
                    'Lexeme': word.lexeme,
                    'Basis': word.basis,
                    'Part of speech': word.part_of_speech,
                    'Ending': word.ending,
                    'Case': word.case,
                    'Gender': word.gender,
                    'Number': word.number
                }
            }

            word_dict_list.append(word_dict)

        save_json: str = json.dumps(word_dict_list)
        return save_json

    def save_file(self, save_path: str, word_list: list[Word]) -> None:
        save_json: str = self.__form_json(word_list)

        with open(save_path) as outfile:
            outfile.write(save_json)
