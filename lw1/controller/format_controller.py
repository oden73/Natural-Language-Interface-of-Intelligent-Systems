import os
import re

from exception.empty_file_exception import EmptyFileExpection


class FormatController:
    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def _is_file_valid(self) -> bool:
        if not os.path.exists(self._file_name):
            raise FileNotFoundError
        if os.path.getsize(self._file_name) == 0:
            raise EmptyFileExpection
        return True

    def _clean_text(self, text: str) -> str:
        text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text

    def file_parse(self) -> str:
        pass

