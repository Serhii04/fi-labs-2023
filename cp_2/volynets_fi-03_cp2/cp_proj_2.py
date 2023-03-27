import math
from pprint import pprint

def create_text(sourse: str, dest: str) -> None:
    """Read from file sourse, convert to apropriate 
    form and write it to dest file

    Args:
        sourse (str): path to file that will be read  
        dest (str): path to file that will be written
    
    Returns:
        None
    """
    with open(sourse, "r") as file_read:
        text_read = file_read.read()
        with open(dest, "w") as file_write:
            for c in text_read:
                if c.isalpha():
                    file_write.write(c.lower())

class WienerCryptographer:
    def __init__(self, alpha: str, leters_probapility: list) -> None:
        self.leters_probapility = leters_probapility.copy()
        self.set_alpha(alpha=alpha)

    def set_alpha(self, alpha: str) -> None:
        self.most_frequent_leter = "о"

        self.alpha = alpha
        self.size = len(alpha)

        self.__id_to_letter = dict()
        for id, leter in zip(range(len(alpha)), alpha):
            self.__id_to_letter[id] = leter

        self.__letter_to_id = dict()
        for id, leter in zip(range(len(alpha)), alpha):
            self.__letter_to_id[leter] = id
    
    def get_id(self, leter: str):
        """
        Retruns:
            int: index of leter in alphabet, starting from 0
        """
        return self.__letter_to_id[leter]

    def get_leter(self, leter_id: int):
        """
        Retruns:
            str: char in alphabet at given index
        """
        while leter_id >= self.size:
            leter_id -= self.size
        
        while leter_id < 0:
            leter_id += self.size

        return self.__id_to_letter[leter_id]
    
    def cipher(self, key: str, text: str) -> str:
        """Wiener cipher

        Args:
            key (list): list of integer numbers
            text (str): text to ciphered
        
        Returns:
            str: cipher
        """
        key_values = list()
        for c in key:
            if c not in self.alpha:
                raise ValueError(f"ERROR: key '{c}' isn't in alphabet")
            key_values.append(self.get_id(leter=c))

        cipher = ""

        i = 0
        for c in text:
            cipher += self.get_leter(self.get_id(c) + key_values[i])
            i += 1

            if i >= len(key):
                i = 0

        return cipher

    def uncipher(self, key: str, text: str) -> str:
        """Wiener uncipher

        Args:
            key (list): list of integer numbers
            text (str): text to unciphered
        
        Returns:
            str: uncipher
        """
        key_values = list()
        for c in key:
            if c not in self.alpha:
                raise ValueError(f"ERROR: key '{c}' isn't in alphabet")
            key_values.append(self.get_id(leter=c))

        uncipher = ""

        i = 0
        for c in text:
            uncipher += self.get_leter(self.get_id(c) - key_values[i])
            i += 1

            if i >= len(key):
                i = 0

        return uncipher

    def count_occurrences(self, text: str) -> dict:
        occurrences = dict()
        for c in self.alpha:
            occurrences[c] = 0

        for c in text:
            occurrences[c] += 1
        
        return occurrences

    def accordance_index(self, text: str) -> float:
        index = 0

        occurrences = self.count_occurrences(text=text)
        for key in occurrences:
            index += occurrences[key] * (occurrences[key] - 1)

        n = len(text)
        index = (index / n) / (n-1)

        return index

    def blocks_accordance_index(self, blocks: list) -> list:
        accordances = list()
        for block in blocks:
            accordances.append(self.accordance_index(text=block))
        
        return accordances

    def divide_text(self, text: str, r: int) -> list:
        if len(text) < r:
            raise ValueError(f'ERROR: r: "{r}" must me less then text size: "{len(text)}")')

        blocks = list()
        for i in range(r):
            blocks.append("")
        
        i = 0
        for c in text:
            blocks[i] += c
            i += 1
            if i == r:
                i = 0 
        
        return blocks

    def calculate_key_size(self, text: str, e: int=0.01) -> int:
        for r in range(2, 100):
            blocks = self.divide_text(text=text, r=r)
            accordances = self.blocks_accordance_index(blocks=blocks)

            I_0 = 1 / self.size
            I = 0.055
            # I = self.accordance_index(text=text)

            diff = (I_0 + I) / 2

            pprint(f"{r}: {accordances} - {diff}")
            size_is_r = True
            for accordance in accordances:
                if accordance - I_0 < 0.02:
                    size_is_r = False
                    break
            
            if size_is_r:
                return r
        
        raise ValueError(f"ERROR: lenght of cipher can't be calculated")

    def decipher_key_element_by_letter(self, text: str):
        occurrences = self.count_occurrences(text=text)
        most_frequent_cipher_leter = max(occurrences, key=lambda key: occurrences[key])

        return self.get_leter(self.get_id(most_frequent_cipher_leter) - self.get_id(self.most_frequent_leter))

    def decipher_by_letter(self, text: str) -> str:
        key = ""

        r = self.calculate_key_size(text=text)
        print(f"r: {r}")
        
        blocks = self.divide_text(text=text, r=r)
        for block in blocks:
            key += self.decipher_key_element_by_letter(text=block)

        return key
    
    def decipher_key_element_by_M_func(self, text: str) -> str:
        M = dict()

        occurrences = self.count_occurrences(text=text)
        for g in self.alpha:
            M[g] = 0 
            for t in self.alpha:
                M[g] += self.leters_probapility[t] * occurrences[self.get_leter(self.get_id(g) + self.get_id(t))]
            
        return max(M, key=lambda key: occurrences[key])

    def decipher_by_M_func(self, text: str) -> str:
        key = ""

        r = self.calculate_key_size(text=text)
        print(f"r: {r}")
        
        blocks = self.divide_text(text=text, r=r)
        for block in blocks:
            key += self.decipher_key_element_by_M_func(text=block)

        return key


leters_probapility = {
    "а": 0.075,
    "б": 0.017,
    "в": 0.046,
    "г": 0.016,
    "д": 0.030,
    "е": 0.087,
    "ж": 0.009,
    "з": 0.018,
    "и": 0.075,
    "й": 0.012,
    "к": 0.034,
    "л": 0.042,
    "м": 0.031,
    "н": 0.065,
    "о": 0.11,
    "п": 0.028,
    "р": 0.048,
    "с": 0.055,
    "т": 0.065,
    "у": 0.025,
    "ф": 0.002,
    "х": 0.011,
    "ц": 0.005,
    "ч": 0.015,
    "ш": 0.007,
    "щ": 0.004,
    "ъ": 0.017,
    "ы": 0.019,
    "ь": 0.017,
    "э": 0.003,
    "ю": 0.022,
    "я": 0.022,
}
ru_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
def main():
    John = WienerCryptographer(alpha=ru_alpha,
                               leters_probapility=leters_probapility)

    with open("cp_2/volynets_fi-03_cp2/example_text.txt", "r") as file:
        text = file.read()
        
        cipher = John.cipher(key="абвабвабва", text=text)

        un_key = John.decipher_by_letter(text=cipher)
        deciper = John.uncipher(key=un_key, text=cipher)
        print(f"un_key 1: {un_key}")
        print(f"deciper 1: {deciper}")

        un_key = John.decipher_by_M_func(text=cipher)
        deciper = John.uncipher(key=un_key, text=cipher)
        print(f"un_key 2: {un_key}")
        print(f"deciper 2: {deciper}")

if __name__ == "__main__":
    main()