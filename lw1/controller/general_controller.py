from controller.docx_controller import DOCXController
from controller.doc_controller import DOCController
from controller.save_controller import SaveController
from controller.format_controller import FormatController
from controller.morphology_controller import MorphologyController
from controller.file_controller import FileController
from controller.word_form_generation_controller import WordFormGenerationController
from controller.editing_controller import EditingController
from controller.search_controller import SearchController
from controller.documentation_controller import DocumentationController

from model.Word import Word

from exception.file_format_exception import FileFormatException
from exception.part_of_speech_exception import PartOfSpeechException


class GeneralController:
    def __init__(self) -> None:
        self.__cur_word_list: list[Word] = []

        self.__file_controller: FileController = FileController()
        self.__format_controller: FormatController | None = None
        self.__morphology_controller: MorphologyController = MorphologyController()
        self.__save_controller: SaveController = SaveController()
        self.__word_form_generation_controller: WordFormGenerationController = WordFormGenerationController()
        self.__editing_controller: EditingController = EditingController()
        self.__search_controller: SearchController = SearchController()
        self.__documentation_controller: DocumentationController = DocumentationController()

    def word_list_generation(self, text_file_name: str) -> list[Word]:
        try:
            file_format: str = self.__file_controller.file_format_definition(text_file_name)

            if file_format == 'DOC':
                self.__format_controller = DOCController()
            else:
                self.__format_controller = DOCXController()

            text: str = self.__format_controller.file_parse(text_file_name)

            self.__cur_word_list: list[Word] = self.__morphology_controller.word_objects_creation(text)

            return self.__cur_word_list
        except FileFormatException as e:
            print(e)
        except PartOfSpeechException as e:
            print(e)

    def save_configuration(self, save_file_path: str) -> None:
        self.__save_controller = SaveController()
        self.__save_controller.save_file(save_file_path, self.__cur_word_list)

        # affirmation_window

    def generate_word_form(self, params: dict) -> None:
        word_form: str = self.__word_form_generation_controller.word_form_generation(params)

        # word form display

    def edit_word(self, word: Word, params: dict) -> None:
        new_word: Word = self.__editing_controller.edit_word(word, params)
        self.__cur_word_list = [new_word] + self.__cur_word_list

        # tree_view update

    def search(self, params: dict) -> None:
        search_result: list[Word] = self.__search_controller.search(self.__cur_word_list, params)

        # search result display

    def filter(self, params: dict) -> None:
        filter_result: list[Word] = self.__search_controller.filter(self.__cur_word_list, params)

        # filter result display

    def document(self, word_list_boundaries: tuple, documentation_file_save_path: str) -> None:
        self.__documentation_controller.documentation(
            documentation_file_save_path,
            self.__cur_word_list[word_list_boundaries[0] - 1: word_list_boundaries[1]],
            (word_list_boundaries[0] == 1 and word_list_boundaries[1] == len(self.__cur_word_list))
        )

        # affirmation_window
