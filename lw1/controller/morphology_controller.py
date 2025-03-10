from natasha import Doc, MorphVocab, NewsMorphTagger, Segmenter, NewsEmbedding

from model.Word import Word
from helper.replace_helper import ReplaceHelper


class MorphologyController:
    def __init__(self, text: str) -> None:
        self.__text: str = text
        self.__helper: ReplaceHelper = ReplaceHelper()

        self.__segmenter: Segmenter = Segmenter()
        self.__morph_vocab: MorphVocab = MorphVocab()
        self.__emb: NewsEmbedding = NewsEmbedding()
        self.__morph_tagger: NewsMorphTagger = NewsMorphTagger(self.__emb)

        self.__doc = Doc(self.__text)

    def word_objects_creation(self) -> list[Word]:
        self.__doc.segment(self.__segmenter)
        self.__doc.tag_morph(self.__morph_tagger)
        for token in self.__doc.tokens:
            token.lemmatize(self.__morph_vocab)

        word_list: list[Word] = []

        for token in self.__doc.tokens:
            basis: str = ''
            ending: str = ''

            if token.lemma != token.text:
                ending = token.text.replace(token.lemma, '', 1)
                basis = token.lemma
            else:
                ending = '-'
                basis = token.lemma

            if token.pos == 'X':
                raise PartOfSpeechException

            word_object: Word = Word(
                start_pos=token.start,
                stop_pos=token.stop,
                word=token.text,
                lexeme=token.lemma,
                basis=basis,
                part_of_speech=self.__helper.part_of_speech_dict[token.pos],
                ending=ending,
                case=self.__helper.case_dict[token.feats.get('Case', '-')],
                gender=self.__helper.gender_dict[token.feats.get('Gender', '-')],
                number=self.__helper.number_dict[token.feats.get('Number', '-')]
            )

            word_list.append(word_object)

        word_list = sorted(word_list, key=lambda w: w.lexeme)
        return word_list
