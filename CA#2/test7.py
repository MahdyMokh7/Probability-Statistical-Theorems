#part3
import sympy
from scipy.stats import geom

s = sympy.symbols('s')

n = 10
p = (1/2)**n

mgf_Xi = p * sympy.exp(s) / 1 - ((1 - p) * sympy.exp(s))
print(mgf_Xi.subs({s:10}))
