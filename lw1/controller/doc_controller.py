import win32com.client

from controller.format_controller import FormatController


class DOCController(FormatController):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def file_parse(self) -> str:
        if not super()._is_file_valid():
            return ""

        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False

        doc = word.Documents.Open(self._file_name)

        text: str = doc.Content.Text
        text = super()._clean_text(text)

        return text
