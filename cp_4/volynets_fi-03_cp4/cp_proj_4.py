import math
import collections
import itertools


# ************************************
#               Classes
# ************************************

class BinaryVector:
    def __init__(self, state: str) -> None:
        self.state = list()
        if isinstance(state, str):
            self.set_str(values=state)
        elif isinstance(state, list):
            self.set_list(values=state)
        else:
            print("ERROR")

        # self.length = None
    
    def __getitem__(self, key) -> bool:
        return self.state[key + self.state_id]
    
    def __str__(self):
        s = ""
        for i in range(self.state_id, len(self.state)):
            if self.state[i]:
                s += "1"
            else:
                s += "0"
        
        return f"[{s}]"
    
    def __len__(self) -> int:
        return len(self.state)
    
    @property
    def state_id(self):
        return self._curent_state_id
    
    @state_id.setter
    def state_id(self, value: int):
        self._curent_state_id = value

    def set_list(self, values: list, state_id: int=0):
        self.state = values
        self.state_id = state_id
    
    def set_str(self, values: str, state_id: int=0):
        for c in values:
            if c == "1":
                self.state.append(True)
            else:
                self.state.append(False)
        
        self.state_id = state_id

    def append(self, value) -> None:
        self.state.append(value)
        # self.next_state()
    
    def next_state(self) -> None:
        self.state_id += 1

class GeffeCryptographer:
    def __init__(self):
        pass

    def calculate_statistic(self, state_1: BinaryVector, state_2: BinaryVector, N: int) -> int:
        R = 0
        for i in range(N):
            R += int(state_1[i] ^ state_2[i])
        
        return R


    def get_key_of(self, states: str) -> BinaryVector:
        N = 256
        C = 80

        N_1 = 226
        N_2 = 233
        C_1 = 71
        C_2 = 73

        n_1 = 25
        n_2 = 26

        z = BinaryVector(state=states)

        x_candidats = list()
        y_candidats = list()
        s_candidats = list()

        x = BinaryVector(state=states)
        i = 0
        for cur_state in itertools.product([False, True], repeat=n_1):
            print(i)
            i += 1
            # x.set_list(list(cur_state))
            
            # for i in range(N - len(x)):
            #     x.append(L_1(state=x))
            #     x.next_state()
            
            # x.state_id = 0
        
            # R = self.calculate_statistic(z, x, N=N)
            
            # if R < C:
            #     x_candidats.append(cur_state)
            #     print(f"finx candidate for x:\n{cur_state}")
            #     # return cur_state
            pass



# ************************************
#           Generator functions
# ************************************

# LFSRs for main variant
def L_1_main(state: BinaryVector) -> bool:
    return state[0] ^ state[1] ^ state[4] ^ state[6]

def L_2_main(state: BinaryVector) -> bool:
    return state[0] ^ state[3]

def L_3_main(state: BinaryVector) -> bool:
    return state[0] ^ state[1] ^ state[2] ^ state[3] ^ state[5] ^ state[7]

# LFSRs, variant for me
def L_1_dummie(state: BinaryVector) -> bool:
    return state[0] ^ state[3] ^ state[25]

def L_2_dummie(state: BinaryVector) -> bool:
    return state[0] ^ state[1] ^ state[2] ^ state[6]

def L_3_dummie(state: BinaryVector) -> bool:
    return state[0] ^ state[1] ^ state[2] ^ state[5]

# LFSRs that will be using. They are pseudonyms
def L_1(state: BinaryVector) -> bool:
    # return L_1_main(state=state)
    return L_1_dummie(state=state)

def L_2(state: BinaryVector) -> bool:
    # return L_2_main(state=state)
    return L_2_dummie(state=state)

def L_3(state: BinaryVector) -> bool:
    # return L_3_main(state=state)
    return L_3_dummie(state=state)

# Geffe generator
def Geffe(state: BinaryVector) -> bool:
    x = L_1(state=state)
    y = L_2(state=state)
    s = L_3(state=state)
    
    return s*x ^ (1 ^ s)*y

# ************************************
#               Example
# ************************************

def main():
    pass

if __name__ == "__main__":
    main()