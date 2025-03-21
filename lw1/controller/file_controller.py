from exception.file_format_exception import FileFormatException


class FileController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def file_format_definition(file_name: str) -> str:
        if file_name[-3:] == 'doc':
            return 'DOC'
        elif file_name[-4:] == 'docx':
            return 'DOCX'
        else:
            raise FileFormatException
