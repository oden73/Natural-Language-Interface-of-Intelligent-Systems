from model.Word import Word


class SearchController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def search(word_list: list[Word], params: dict) -> list[Word]:
        search_result: list[Word] = []

        for word in word_list:
            if word.part_of_speech == params['Часть речи'] and \
                    word.case == params['Падеж'] and \
                    word.gender == params['Род'] and \
                    word.number == params['Число']:
                search_result.append(word)

        return search_result

    @staticmethod
    def filter(word_list: list[Word], params: dict) -> list[Word]:
        filter_result: list[Word] = []

        for word in word_list:
            if word.part_of_speech in params['Часть речи'] or\
                    word.case in params['Падеж'] or\
                    word.gender in params['Род'] or\
                    word.number in params['Число']:
                filter_result.append(word)

        return filter_result
