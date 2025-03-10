from exception.file_format_exception import FileFormatException


class FileController:
    def __init__(self, file_name: str) -> None:
        self.__file_name: str = file_name

    def file_format_definition(self) -> str:
        if self.__file_name[-3:] == 'doc':
            return 'DOC'
        elif self.__file_name[-4:] == 'docx':
            return 'DOCX'
        else:
            raise FileFormatException
