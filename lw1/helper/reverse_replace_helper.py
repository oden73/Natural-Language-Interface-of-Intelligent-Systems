class ReverseReplaceHelper:
    def __init__(self) -> None:
        self.case_dict: dict = {
            'именительный': 'nomn',
            'родительный': 'gent',
            'дательный': 'datv',
            'винительный': 'accs',
            'творительный': 'ablt',
            'предложный': 'loct'
        }

        self.gender_dict: dict = {
            'мужской': 'masc',
            'женский': 'femn',
            'средний': 'neut'
        }

        self.number_dict: dict = {
            'единственное': 'sing',
            'множественное': 'plur'
        }
