import win32com.client

from controller.format_controller import FormatController


class DOCController(FormatController):
    def __init__(self):
        super().__init__()

    def file_parse(self, file_name: str) -> str:
        if not super()._is_file_valid(file_name):
            return ""

        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False

        doc = word.Documents.Open(file_name)

        text: str = doc.Content.Text
        text = super()._clean_text(text)

        return text
