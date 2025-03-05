class Word:
    def __init__(self, position_in_text: int, lexeme: str, basis: str, part_of_speech: str, ending: str, case: str,
                 gender: str, number: str) -> None:
        self.position_in_text: int = position_in_text
        self.lexeme: str = lexeme
        self.basis: str = basis
        self.part_of_speech: str = part_of_speech
        self.ending: str = ending
        self.case: str = case
        self.gender: str = gender
        self.number: str = number
