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




ru_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
def main():
    John = WienerCryptographer(ru_alpha)

    with open("cp_2/volynets_fi-03_cp2/example_text.txt", "r") as file:
        text = file.read()
        cipher = John.cipher(key="аааааааааааааааая", text=text)
        print(cipher)

if __name__ == "__main__":
    main()