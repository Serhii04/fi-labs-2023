import math

def create_text(sourse: str, dest: str):
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
        
ru_alpha = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
    'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'х', 'ц',
    'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'
]

def main():
    # create_text(sourse="cp_2/volynets_fi-03_cp2/example_pre_text.txt",
    #             dest="cp_2/volynets_fi-03_cp2/example_text.txt")
    
    with open("cp_2/volynets_fi-03_cp2/example_text.txt", "r") as file:
        pass

if __name__ == "__main__":
    main()