from controller.format_controller import FormatController


class DOCXController(FormatController):
    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)

    def file_parse(self) -> str:
        pass
