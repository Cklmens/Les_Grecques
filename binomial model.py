import numpy as np
import math as ma
def oneperiod(so,k,t,r,v):
    u= ma.exp(v* ma.sqrt(t))
    d= 1/u
    p=(ma.exp(r*t)-d)/(u-d)
    fu= so*u-k if (so*u-k) else 0
    fd= so*d-k if (so*d-k) else 0
    
    return ((1-p)*fd+p*fu)*ma.exp(-r*t)


   
    
print(oneperiod(30,32,0.25,0.5,0.3))