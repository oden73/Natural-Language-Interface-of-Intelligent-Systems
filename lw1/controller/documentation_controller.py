from model.Word import Word


class DocumentationController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def __generate_documentation_text(word_list: list[Word]) -> str:
        info_dict: dict = {
            'именительный': 0,
            'родительный': 0,
            'дательный': 0,
            'винительный': 0,
            'творительный': 0,
            'предложный': 0,
            '-падеж': 0,
            'единственное': 0,
            'множественное': 0,
            '-число': 0,
            'мужской': 0,
            'женский': 0,
            'средний': 0,
            '-род': 0
        }

        for word in word_list:
            info_dict[word.case] += 1
            info_dict[word.number] += 1
            info_dict[word.gender] += 1

        documentation_text: str = f"""
        Всего слов в документе: {len(word_list)}\n\n
        Слов в документе в Именительном падеже: {info_dict['именительный']}\n
        Слов в документе в Родительном падеже: {info_dict['родительный']}\n
        Слов в документе в Дательном падеже: {info_dict['дательный']}\n
        Слов в документе в Винительном падеже: {info_dict['винительный']}\n
        Слов в документе в Творительном падеже: {info_dict['творительный']}\n
        Слов в документе в Предложном падеже: {info_dict['предложный']}\n
        Слов в документе без падежа: {info_dict['-падеж']}\n\n
        Слов в документе в единственном числе: {info_dict['единственное']}\n
        Слов в документе в множественном числе: {info_dict['множественное']}\n
        Слов в документе без числа: {info_dict['-число']}\n\n
        Слов мужского рода в документе: {info_dict['мужской']}\n
        Слов женского рода в документе: {info_dict['женский']}\n
        Слов среднего рода в документе: {info_dict['средний']}\n
        Слов без рода в документе: {info_dict['-род']}
        """

        return documentation_text

    def documentation(self, documentation_file_save_path, word_list: list[Word]) -> None:
        documentation_text: str = self.__generate_documentation_text(word_list)

        with open(documentation_file_save_path, 'w') as save_file:
            save_file.write(documentation_text)
