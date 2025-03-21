from natasha import Doc, MorphVocab, NewsMorphTagger, Segmenter, NewsEmbedding

from model.Word import Word
from helper.replace_helper import ReplaceHelper
from exception.part_of_speech_exception import PartOfSpeechException


class MorphologyController:
    def __init__(self) -> None:
        self.__helper: ReplaceHelper = ReplaceHelper()

        self.__segmenter: Segmenter = Segmenter()
        self.__morph_vocab: MorphVocab = MorphVocab()
        self.__emb: NewsEmbedding = NewsEmbedding()
        self.__morph_tagger: NewsMorphTagger = NewsMorphTagger(self.__emb)

    def word_objects_creation(self, text: str) -> list[Word]:
        doc = Doc(text)

        doc.segment(self.__segmenter)
        doc.tag_morph(self.__morph_tagger)
        for token in doc.tokens:
            token.lemmatize(self.__morph_vocab)

        word_list: list[Word] = []

        for token in doc.tokens:
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
