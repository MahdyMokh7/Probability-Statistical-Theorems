import random


def avg_num_of_tries_to_get_all_coupons(n: int, k: int) -> float:
    num_of_tries = []
    for i in range(k):
        main_list = [0 for _ in range(n)]
        while 0 < main_list.count(0):
            temp = random.randint(0, n - 1)
            main_list[temp] += 1
        num_of_tries.append(sum(main_list))
    avg = sum(num_of_tries) / k
    return avg


print("n=10, k=10:  ", avg_num_of_tries_to_get_all_coupons(n=10, k=10))
print("n=10, k=100:  ", avg_num_of_tries_to_get_all_coupons(n=10, k=100))
print("n=10, k=1000:  ", avg_num_of_tries_to_get_all_coupons(n=10, k=1000))


#part3
import sympy

s = sympy.symbols('s')

n = 10
p = [(n-i)/n for i in range(n)]

mgf_Xi = [((p[i] * sympy.exp(s)) / (1 - ((1 - p[i]) * sympy.exp(s)))) for i in range(n)]

# part4
mgf_X = 1
for i in range(n):
    mgf_X *= mgf_Xi[i]


# part5
deriv_mgf_x = mgf_X.diff(s)
print("MGF solution:  ", deriv_mgf_x.subs({s:0}))
print("Monte Carlo solution:  ", avg_num_of_tries_to_get_all_coupons(n=10, k=1000))
