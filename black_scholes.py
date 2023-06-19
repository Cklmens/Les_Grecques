import numpy as np
import math as ma



from scipy.stats import norm

def black_scholes(S,K,T,r,sigma, style):
    d1 = (np.log(S/K) + (r  + sigma**2/2)*T) / sigma*np.sqrt(T)
    d2 = d1 - sigma* np.sqrt(T)
    if (style=='call'):
        return S * norm.cdf(d1)  - K * np.exp(-r*T)*norm.cdf(d2)
    if(style=='put'):
        return K * np.exp(-r*T)*norm.cdf(-d2)-S * norm.cdf(-d1)

     

S=100       # So le prix du sous-jacent a t=0
sigma= 0.25  # sigma: la volatilité constante
K=110        # Strike
r=0.05
T=1

print(black_scholes(S,K,T,r,sigma,"call"))

