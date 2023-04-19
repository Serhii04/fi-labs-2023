from pprint import pprint

from lab_constants import __RU_ALPHABET_LETERS_PROBABILITY__ as probability
from lab_constants import __RU_ALPHABET__ as alphabet


def gcd(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Error: only integer values are allowed")
    
    if a < 0 or b < 0:
        raise ValueError("Error: only positive values are allowed")
    
    if a == 0:
        return b
    
    if b == 0:
        return a

    if a == 1 or b == 1:
        return 1
    
    if a == b:
        return a
    
    r_1, r_2 = max(a, b), min(a, b)

    r_3 = r_1 % r_2
    print(f"r_3 = {r_3}")
    r_1 = r_2
    r_2 = r_3

    while r_3 != 0:
        r_3 = r_1 % r_2
        print(f"r_3 = {r_3}")
        r_1 = r_2
        r_2 = r_3
    
    return r_1

def reverse(a: int, mod: int):
    if not isinstance(a, int) or not isinstance(mod, int):
        raise ValueError("Error: only integer values are allowed")
    
    while a < 0:
        a += mod

    if a >= mod:
        a = a % mod

    if a == 0:
        return

    if a == 1:
        return 1

    q_vals = []
    r_1 = mod
    r_2 = a
    r_3 = 1
    while r_3 != 0:
        q_vals.append(int(r_1 / r_2))
        r_3 = r_1 % r_2

        r_1 = r_2
        r_2 = r_3
    
    if r_1 != 1:
        return 
    
    q_vals.pop()
    
    u_vals = [1, 0]
    v_vals = [0, 1]
    for q in q_vals:
        u_vals.append(u_vals[-2] - u_vals[-1] * q)
        v_vals.append(v_vals[-2] - v_vals[-1] * q)
    
    print(f"q_vals: {q_vals}")
    print(f"u_vals: {u_vals}")
    print(f"v_vals: {v_vals}")
    
    return abs(v_vals[-1])


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
    print(reverse(123, 3452))

if __name__ == "__main__":
    main()