class Word:
    def __init__(self, start_pos: int, stop_pos: int, word: str, lexeme: str, basis: str, part_of_speech: str, ending: str, case: str,
                 gender: str, number: str) -> None:
        self.start_pos: int = start_pos
        self.stop_pos: int = stop_pos
        self.word: str = word
        self.lexeme: str = lexeme
        self.basis: str = basis
        self.part_of_speech: str = part_of_speech
        self.ending: str = ending
        self.case: str = case
        self.gender: str = gender
        self.number: str = number
