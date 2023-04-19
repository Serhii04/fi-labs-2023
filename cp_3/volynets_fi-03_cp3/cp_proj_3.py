from pprint import pprint

from lab_constants import __RU_ALPHABET_LETERS_PROBABILITY__ as probability
from lab_constants import __RU_ALPHABET__ as alphabet


class AffineCryptographer:
    def __init__(self, alphabet: str, leters_probability: list) -> None:
        self.leters_probability = leters_probability.copy()
        self.set_alphabet(alphabet=alphabet)

    def set_alphabet(self, alphabet: str) -> None:
        # self.most_frequent_leter = "о"

        self.alphabet = alphabet
        self.size = len(alphabet)

        self.__id_to_letter = dict()
        for id, leter in zip(range(len(alphabet)), alphabet):
            self.__id_to_letter[id] = leter

        self.__letter_to_id = dict()
        for id, leter in zip(range(len(alphabet)), alphabet):
            self.__letter_to_id[leter] = id


def main():
    pass

if __name__ == "__main__":
    main()