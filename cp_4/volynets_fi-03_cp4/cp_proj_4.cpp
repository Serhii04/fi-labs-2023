#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

// ************************************
//           Generator functions
// ************************************

// LFSRs for main variant
bool L_1_main(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(1 + i) ^ state->at(4 + i) ^ state->at(6 + i);
}

bool L_2_main(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(3 + i);
}

bool L_3_main(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(1 + i) ^ state->at(2 + i) ^ state->at(3 + i) ^ state->at(5 + i) ^ state->at(7 + i);
}

// LFSRs, variant for me
bool L_1_dummie(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(3 + i);
}

bool L_2_dummie(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(1 + i) ^ state->at(2 + i) ^ state->at(6 + i);
}

bool L_3_dummie(vector<bool> *state, int i){
    return state->at(0 + i) ^ state->at(1 + i) ^ state->at(2 + i) ^ state->at(5 + i);
}

// LFSRs that will be using. They are pseudonyms
bool L_1(vector<bool> *state, int i){
    // return L_1_main(state=state, i=i);
    return L_1_dummie(state=state, i=i);
}

bool L_2(vector<bool> *state, int i){
    // return L_2_main(state=state, i=i);
    return L_2_dummie(state=state, i=i);
}

bool L_3(vector<bool> *state, int i){
    // return L_3_main(state=state, i=i);
    return L_3_dummie(state=state, i=i);
}

// Geffe generator
bool Geffe(vector<bool> *state, int i){
    bool x = L_1(state=state, i=i);
    bool y = L_2(state=state, i=i);
    bool s = L_3(state=state, i=i);
    
    return (s & x) ^ ((1 ^ s) & y);
}

bool Geffe_val(bool x, bool y, bool s){
    return (s & x) ^ ((1 ^ s) & y);
}

// ************************************
//      GeffeCryptographer class
// ************************************

class GeffeCryptographer{
public:
    int calculate_statistic(vector<bool> *a, vector<bool> *b, int N){
        int R = 0;

        for(int i = 0; i < N; ++i){
            R += int(a->at(i) ^ b->at(i));
        }

        return R;
    }

    vector<bool>* get_bool_vector(string s){
        vector<bool> *v = new vector<bool>(s.length());

        int l = s.length();
        for(int i = 0; i < l; ++i){
            if(s[i] == '1'){
                (*v)[i] = true;
            }else{
                (*v)[i] = false;
            }
        }

        return v;
    }

    void print_bool_vector(vector<bool> *v){
        cout << "[";

        int l = v->size() - 1;
        for(int i = 0; i < l; ++i){
            cout << v->at(i);
        }

        cout << v->at(l) << "]" << endl;
    }

    string string_vector(vector<bool> *v){
        string s = "[";

        int l = v->size() - 1;
        for(int i = 0; i < l; ++i){
            s += v->at(i);
        }

        s += v->at(l) + "]";

        return s;
    }

    bool next_vector(vector<bool> *v){
        int i = v->size() - 1;

        while(i > -1 && v->at(i) == true){
            (*v)[i] = false;
            i -= 1;
        }

        if(i == -1){
            return false;
        }

        (*v)[i] = true;

        return true;
    }

    vector<vector<bool>> get_key_of(string z_val){
        int n_1 = 25;
        int n_2 = 26;
        int n_3 = 27;

        int N_1 = 226;
        int N_2 = 233;
        int C_1 = 71;
        int C_2 = 73;

        vector<vector<bool>> candidats_for_L_1 = get_candidats_for_L_1(z_val, n_1, N_1, C_1);
        vector<vector<bool>> candidats_for_L_2 = get_candidats_for_L_2(z_val, n_2, N_2, C_2);

        vector<vector<bool>> solution = get_solution_from_L_3(
            z_val, n_3, candidats_for_L_1, candidats_for_L_2
        );

        for(auto key: solution){
            print_bool_vector(&key);
        }

        return solution;
    }

    vector<vector<bool>> get_candidats_for_L_1(string z_val, int n_1, int N_1, int C_1){
        vector<bool> *z = get_bool_vector(z_val);
        vector<vector<bool>> candidats(0);
        vector<bool> *key_iterator = new vector<bool>(n_1);
        for(int i = 0; i < n_1; ++i){
            (*key_iterator)[i] = false;
        }
        vector<bool> *temp_x = new vector<bool>(N_1);

        int k = 0;
        while(next_vector(key_iterator)){
            for(int i = 0; i < n_1; ++i){
                (*temp_x)[i] = (*key_iterator)[i];
            }

            for(int i = n_1; i < N_1; ++i){
                (*temp_x)[i] = L_1(temp_x, i - n_1);
            }

            int R = calculate_statistic(z, temp_x, N_1);

            if(R < C_1){
                vector<bool> for_save(n_1);
                
                for(int i = 0; i < n_1; ++i){
                    for_save[i] = key_iterator->at(i);
                }

                candidats.push_back(for_save);
                cout << "There: R = " << R << ", key = ";
                print_bool_vector(&for_save);
            }
        }

        return candidats;
    }

    vector<vector<bool>> get_candidats_for_L_2(string z_val, int n_2, int N_2, int C_2){
        vector<bool> *z = get_bool_vector(z_val);
        vector<vector<bool>> candidats(0);
        vector<bool> *key_iterator = new vector<bool>(n_2);
        for(int i = 0; i < n_2; ++i){
            (*key_iterator)[i] = false;
        }
        vector<bool> *temp_x = new vector<bool>(N_2);

        while(next_vector(key_iterator)){
            for(int i = 0; i < n_2; ++i){
                (*temp_x)[i] = (*key_iterator)[i];
            }

            for(int i = n_2; i < N_2; ++i){
                (*temp_x)[i] = L_2(temp_x, i - n_2);
            }

            int R = calculate_statistic(z, temp_x, N_2);

            if(R < C_2){
                vector<bool> for_save(n_2);
                
                for(int i = 0; i < n_2; ++i){
                    for_save[i] = key_iterator->at(i);
                }

                candidats.push_back(for_save);
                cout << "There: R = " << R << ", key = ";
                print_bool_vector(&for_save);
            }
        }

        return candidats;
    }

    bool check_for_s(
        vector<bool> *z,
        vector<bool> *x,
        vector<bool> *y,
        vector<bool> *s
    ){
        x->push_back(L_1(x, 0));
        x->push_back(L_1(x, 1));

        y->push_back(L_2(y, 0));

        for(int i = 0; i < s->size(); ++i){
            if(s->at(i) == 1){
                if(z->at(i) != x->at(i)){
                    return false;
                }
            }else{
                if(z->at(i) != y->at(i)){
                    return false;
                }
            }
        }

        x->pop_back();
        x->pop_back();
        
        y->pop_back();

        return true;
    }

    bool check_answer_triplet(vector<bool> *z, vector<bool> *key_1, vector<bool> *key_2, vector<bool> *key_3){
        vector<bool> cur_key_1(key_1->size());
        vector<bool> cur_key_2(key_2->size());
        vector<bool> cur_key_3(key_3->size());

        for(int i = 0; i < key_1->size(); ++i){
            cur_key_1[i] = key_1->at(i);
        }
        
        for(int i = 0; i < key_2->size(); ++i){
            cur_key_2[i] = key_2->at(i);
        }
        
        for(int i = 0; i < key_3->size(); ++i){
            cur_key_3[i] = key_3->at(i);
        }

        int n = z->size();

        int len_key_1 = cur_key_1.size();
        int n_len_key_1 = n - len_key_1;
        for(int i = 0; i < n_len_key_1; ++i){
            cur_key_1.push_back(L_1(&cur_key_1, i));
        }

        int len_key_2 = cur_key_2.size();
        int n_len_key_2 = n - len_key_2;
        for(int i = 0; i < n_len_key_2; ++i){
            cur_key_2.push_back(L_2(&cur_key_2, i));
        }

        int len_key_3 = cur_key_3.size();
        int n_len_key_3 = n - len_key_3;
        for(int i = 0; i < n_len_key_3; ++i){
            cur_key_3.push_back(L_3(&cur_key_3, i));
        }

        for(int i = 0; i < n; ++i){
            if(z->at(i) != Geffe_val(cur_key_1.at(i), cur_key_2.at(i), cur_key_3.at(i))){
                return false;
            }
        }

        return true;
    }

    vector<vector<bool>> get_solution_from_L_3(
        string z_val,
        int n_3,
        vector<vector<bool>> candidats_for_L_1,
        vector<vector<bool>> candidats_for_L_2
    ){
        vector<bool> *z = get_bool_vector(z_val);

        vector<bool> key_iterator = vector<bool>(n_3);
        for(int i = 0; i < n_3; ++i){
            key_iterator[i] = false;
        }

        // ******shortcut******
        // key_iterator[3] = true;
        // key_iterator[4] = true; // 2nd
        // key_iterator[9] = true;
        // key_iterator[13] = true;
        // key_iterator[14] = true;

        vector<vector<vector<bool>>> triplets_of_candidats_for_keys(0);
        while(next_vector(&key_iterator)){
            try{ 
                for(vector<bool> key_x: candidats_for_L_1){
                    for(vector<bool> key_y: candidats_for_L_2){
                        if(check_for_s(z, &key_x, &key_y, &key_iterator)){
                            print_bool_vector(&key_iterator);

                            if(check_answer_triplet(z, &key_x, &key_y, &key_iterator)){
                                cout << "Answer:" << endl;
                                print_bool_vector(&key_x);
                                print_bool_vector(&key_y);
                                print_bool_vector(&key_iterator);
                                cout << endl;

                                vector<vector<bool>> rez{key_x, key_y, key_iterator};
                                return rez;
                            }
                        }
                    }
                }
            }catch(...){
                cout << "ERROR" << endl;
                print_bool_vector(&key_iterator);
            }
        }
    // return something
    }
};

// ************************************
//               Example
// ************************************

int main(){
    string z_str = "01110001010000000110101111110011010000101110011001001100100111001101101100110001001110101101100000011101001101000010101110110001011101011111011110111011011001000010100100110100010011111011100000100011101011111100010000111110101111000010111100100011101000100010111110110010100010111000111101001001011100011110100001100011001000100000010101010011110001000001100001011110101000011000110011010101010100111010111111011000011101100011000110100010100011001011111010100001011011100101100000000110001000000010110101101100101100100110010110000011110000100000110111100111111110001100000100001101001010010110111110000000111110111110000000101101000110010011100101010011001011101100100011100101001110101101001000001011101001110101101100010101110000000110111101101110011010011010110111011111011010110000100110001111111000000001100010101110100011010100110111101000100001111000011011101111111011011111001101110110111111110110000101010001001000101011101111000110101001100101010111001111111110011001110100001111011001101010101110010001001101101010101001110010101001000110110111010010000010000010100110110000010101001111101001010111010011110100001010001010101111011111111100010011001111011000000010100111110011101111001010110110111101111000100110011010100110010100011010101001111001000000010111101111110001010011101111100101100100110101100011110010001111001101010110001011111011100000110110011101010000111001111110000101010100001000100110010011011000001010011101010111000111010100110101011111100001010011100100101010010111110011011010001110101100000111111110110010101110010101001101001101100111110101111011001100101010100111111011111000010101010010110100110010110011010111111111110000011011011111110111110100110011100000110100110010100010000100110101101000011010000011101001000110011011100001011100111100001111010001100101001100011100010110011101101111011001001001101000011010100110001000000100101010101100101101100011000110110000101010110010000010100110000000100001000010001011110011000110000011100100100011100111111101101000000010111111000010011001000001111111111110";
    string z_dummie = "00010011110011101100000001111011100101001011110110011011100110010000001010100011101011001001101101011111100010010100000100011011011000100000110001100001000010100100100100110100010100000000000010010101010100111101101100100000101101100000100010110001010110100010000001111000111011001011001101011011010101000101111100100110101110100010100001101111101111111111100111101001000011011100101001001001101110111100010001000000000111011110110010111111011000001001110010110001101000111001101110011110100101010110111001110110010010010101111100000010100101001011110001101000001000001111101111010010100010111010000010101011111011111101001011101101100110101000000010001110011011110011101101110110101010000001000001110011111000100000110110110100001010111000001010111100111111111000100000010011111110110110011011111010011101101111001011111000011100001001011010011001001011101100011010101010100101110101100000011101111011101110110011001001101100100001000010101000110011000100101101101001111010111000111010011000011000100100011101000000111010011000100100111000010100111111110110111101010110101100000111101000000001010000011011001101010000001010100011010100101000001111110101100111011110000111111100000010111101110100100100111110011001001000011101100011100010011101000000101001010010101010100010101110110101100100011001000011100111110010101001011001101011101001101011111011011001010110011111000011101101111011100110110001010010111001111000000010011110000011011111000100100000110101111100100010111010011111011111101010110100001101001110011011110000011101101110000101000111100000001101000110111111000110111111100100101010111000010110011101111100110100000001100101110110101100011011110110010100101101101011110000010000011101000110110001110011111111100110001001001110011110100110000110101101100111011111101101110101000101100001000000010110000110110101101110011010010001100000111101101101001111110011101011100011110001110111011001111001010001010100110011000001010001000110111111000100010110001000001101101011011000100011111011110000101110111001011100011010001001010101011001";

    GeffeCryptographer Janet = GeffeCryptographer();

    Janet.get_key_of(z_dummie);

    return 0;
}

