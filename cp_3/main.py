#НСД
def gcd_only(a, b):
    if b == 0:
        return a
    else:
        return gcd_only(b, a % b)
#Розширений АЕ
def bezout_coefficients(a, b):
    if b == 0:
        return a , 1, 0
    else:
        gcd,u_1, v_1 = bezout_coefficients(b, a % b)

        u = v_1
        v = u_1 - (a // b) * v_1
        return gcd , u , v




# Приклад використання 
#n=123
#m=12
#print(f"НСД: {gcd_only(n,m)}")
#result=bezout_coefficients(n,m)
#print(result[2])
#print(f"НСД: {result[0]}, Коефіціенти Безу: U={result[1]}, V={result[2]}")



#Лінійне порінвняння
def linear_solve(a, b, n):
    results = []
    gcd_ab, u, v = bezout_coefficients(a, n)
    if gcd_ab == 1:
        results.append((u * b) % n)
        return results
    elif gcd_ab > 1:
        if  b % gcd_ab == 0:
            a = a // gcd_ab
            b = b // gcd_ab
            n = n // gcd_ab
            x = (linear_solve(a,b,n)[0])
            results.append(x)
            for i in range(1, gcd_ab):
                results.append(results[-1] + i*n)
            return results
        else:
            return results


        

n=22123141241
a=1056
b=2612412
result=linear_solve(a,b,n)
print(f"{a}x={b}(mod{n})")
print(result)

def test_equal(a,b,n,result):
    for i in result:

        if (a * i) % n ==(b % n):
            print(f"{a}*{i}={b}mod({n}) \n Успех")
        else: 
            return "Не успех"


print(test_equal(a,b,n,result))

