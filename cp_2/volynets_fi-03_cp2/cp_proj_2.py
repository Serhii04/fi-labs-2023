import math

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
    def __init__(self, alpha) -> None:
        self.set_alpha(alpha=alpha)

    def set_alpha(self, alpha: str) -> None:
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

    def count_occurrences(self, text: str) -> dict:
        occurrences = dict()
        for c in text:
            if c not in occurrences:
                occurrences[c] = 1
            else:
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
        for r in range(2, 33):
            print(r)
            blocks = self.divide_text(text=text, r=r)
            accordances = self.blocks_accordance_index(blocks=blocks)

            # I_0 = 1 / self.size
            # I = 0.055
            I = self.accordance_index(text=text)
            
            pprint(f"{r}: {accordances} - {I}")
            size_is_r = True
            for accordance in accordances:
                if abs(accordance - I) < e:
                    size_is_r = False
                    break
            
            if size_is_r:
                return r

            


ru_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

from pprint import pprint
def main():
    John = WienerCryptographer(ru_alpha)

    with open("cp_2/volynets_fi-03_cp2/example_text.txt", "r") as file:
        text = file.read()
        cipher = John.cipher(key="абвгдежзийклааа", text=text)
        
        pprint(John.calculate_key_size(text=cipher))

if __name__ == "__main__":
    main()