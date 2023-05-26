import math
import collections


# ************************************
#               Classes
# ************************************

class Binary_vector:
    def __init__(self, start_state: str, ) -> None:
        self.state = list()
        for c in start_state:
            if c == "1":
                self.state.append(True)
            else:
                self.state.append(False)

        self._curent_state_id = 0
        self.length = None
    
    def __getitem__(self, key) -> bool:
        return self.state[key + self._curent_state_id]
    
    def __str__(self):
        s = ""
        for i in range(self._curent_state_id, len(self.state)):
            if self.state[i]:
                s += "1"
            else:
                s += "0"
        
        return f"[{s}]"


    def append(self, value) -> None:
        self.state.append(value)
        self._curent_state_id += 1

    

# ************************************
#           Generator functions
# ************************************

# LFSRs for main variant
def L_1_main(state: Binary_vector) -> bool:
    return state[0] ^ state[1] ^ state[4] ^ state[6]

def L_2_main(state: Binary_vector) -> bool:
    return state[0] ^ state[3]

def L_3_main(state: Binary_vector) -> bool:
    return state[0] ^ state[1] ^ state[2] ^ state[3] ^ state[5] ^ state[7]

# LFSRs that will be using. They are pseudonyms
def L_1(state: Binary_vector) -> bool:
    return L_1_main(state=state)

def L_2(state: Binary_vector) -> bool:
    return L_2_main(state=state)

def L_3(state: Binary_vector) -> bool:
    return L_3_main(state=state)

# Geffe generator
def Geffe(state: Binary_vector) -> bool:
    x = L_1(state=state)
    y = L_2(state=state)
    s = L_3(state=state)
    
    print(x, y, s)
    return s*x ^ (1 ^ s)*y

# ************************************
#               Example
# ************************************

def main():
    start_state = "11100000000000000000000000000"
    v = Binary_vector(start_state=start_state)

    for i in range(20):
        r = Geffe(state=v)
        print(r)
        v.append(r)
        print(v)

if __name__ == "__main__":
    main()