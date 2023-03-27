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

    def set_alpha(self, alpha: list) -> None:
        # In case if you are lasy and want to define alpha as string
        if isinstance(alpha, str):
            alpha = list(alpha)

        self.alpha = alpha
        self.alpha_size = len(alpha)

        self.__id_to_letter = dict()
        for id, leter in zip(range(len(alpha)), alpha):
            self.__id_to_letter[id] = leter

        self.__letter_to_id = dict()
        for id, leter in zip(range(len(alpha)), alpha):
            self.__letter_to_id[leter] = id


ru_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
def main():
    John = WienerCryptographer(ru_alpha)

if __name__ == "__main__":
    main()