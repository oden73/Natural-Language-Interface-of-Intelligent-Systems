class FileParsingException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return 'Ошибка: Неудалось прочитать и/или обработать файл\n'
