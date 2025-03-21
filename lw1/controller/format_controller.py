import os
import re

from exception.empty_file_exception import EmptyFileExpection


class FormatController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def _is_file_valid(file_name: str) -> bool:
        if not os.path.exists(file_name):
            raise FileNotFoundError
        if os.path.getsize(file_name) == 0:
            raise EmptyFileExpection
        return True

    @staticmethod
    def _clean_text(text: str) -> str:
        text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text

    def file_parse(self, file_name: str) -> str:
        pass

