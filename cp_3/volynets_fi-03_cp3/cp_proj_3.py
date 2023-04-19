from pprint import pprint

from lab_constants import __RU_ALPHABET_LETERS_PROBABILITY__ as probability
from lab_constants import __RU_ALPHABET__ as alphabet


def gcd(a: int, b: int) -> int:
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
    # print(f"r_3 = {r_3}")
    r_1 = r_2
    r_2 = r_3

    while r_3 != 0:
        r_3 = r_1 % r_2
        # print(f"r_3 = {r_3}")
        r_1 = r_2
        r_2 = r_3
    
    return r_1

def reverse(a: int, M: int) -> int:
    if not isinstance(a, int) or not isinstance(M, int):
        raise ValueError("Error: only integer values are allowed")
    
    while a < 0:
        a += M

    if a >= M:
        a = a % M

    if a == 0:
        return

    if a == 1:
        return 1

    q_vals = []
    r_1 = M
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
    
    # print(f"q_vals: {q_vals}")
    # print(f"u_vals: {u_vals}")
    # print(f"v_vals: {v_vals}")
    
    if v_vals[-1] >= 0:
        return v_vals[-1]
    
    return v_vals[-1] + M

def solve_dif_system(a_1: int, mod_1: int, a_2: int, mod_2: int) -> int:
    d = gcd(mod_1, mod_2)

    if d != 1:
        return

    N = mod_1 * mod_2

    N_1 = mod_2
    N_2 = mod_1

    M_1 = reverse(a=N_1, M=mod_1)
    M_2 = reverse(a=N_2, M=mod_2)

    print(f"answ = ({a_1} * {N_1} * {M_1} + {a_2} * {N_2} * {M_2}) % {N}")

    X_0 = (a_1 * N_1 * M_1 + a_2 * N_2 * M_2) % N

    return X_0


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



def main():
    print(reverse(2, 13))

if __name__ == "__main__":
    main()