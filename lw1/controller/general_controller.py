from controller.docx_controller import DOCXController
from controller.doc_controller import DOCController
from controller.save_controller import SaveController
from controller.format_controller import FormatController
from controller.morphology_controller import MorphologyController
from controller.file_controller import FileController
from controller.word_form_generation_controller import WordFormGenerationController

from view.main_window import MainWindow
from view.word_form_generation_window import WordFormGenerationWindow
from view.about_program_window import AboutProgramWindow

from model.Word import Word

from exception.file_format_exception import FileFormatException
from exception.part_of_speech_exception import PartOfSpeechException


class GeneralController:
    def __init__(self) -> None:
        self.__file_controller: FileController | None = None
        self.__format_controller: FormatController | None = None
        self.__morphology_controller: MorphologyController | None = None
        self.__save_controller: SaveController | None = None
        self.__word_form_generation_controller: WordFormGenerationController | None = None

        self.__main_window: MainWindow = MainWindow()
        self.__about_program_window: AboutProgramWindow = AboutProgramWindow()
        self.__word_form_generation_window: WordFormGenerationWindow = WordFormGenerationWindow()

    def word_list_generation(self, text_file_name: str) -> list[Word]:
        try:
            self.__file_controller = FileController(text_file_name)
            file_format: str = self.__file_controller.file_format_definition()

            if file_format == 'DOC':
                self.__format_controller = DOCController(text_file_name)
            else:
                self.__format_controller = DOCXController(text_file_name)

            text: str = self.__format_controller.file_parse()

            self.__morphology_controller = MorphologyController(text)
            word_list: list[Word] = self.__morphology_controller.word_objects_creation()
            return word_list
        except FileFormatException as e:
            print(e)
        except PartOfSpeechException as e:
            print(e)
