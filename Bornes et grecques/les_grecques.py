import numpy as np
import math as ma
import matplotlib.pyplot as plt

from scipy.stats import norm


def black_scholes(S,K,T,r,sigma, style):
    d1 = (np.log(S/K) + (r  + sigma**2/2)*T) / sigma*np.sqrt(T)
    d2 = d1 - sigma* np.sqrt(T)
    if (style=='call'):
        return S * norm.cdf(d1)  - K * np.exp(-r*T)*norm.cdf(d2)
    if(style=='put'):
        return K * np.exp(-r*T)*norm.cdf(-d2)-S * norm.cdf(-d1)

def delta(S,K,T,r,sigma, style):
    d1=(ma.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*ma.sqrt(T))
    if(style=='call'):
       return norm.cdf(d1)
    if(style=='put'):
       return norm.cdf(d1)-1

def gamma(S,K,T,r,sigma,style):
    d1=(ma.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*ma.sqrt(T))
    return (norm.pdf(d1)/(S*sigma*ma.sqrt(T)))

def theta(S,K,T,r,sigma,style):
    d1=(ma.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*ma.sqrt(T))
    d2=d1-sigma*ma.sqrt(T)
    if(style=='call'):
      return ((-(S*sigma*norm.pdf(d1))/(2*ma.sqrt(T)))-K*r*ma.exp(-r*T)*norm.cdf(d2))
    if(style=='put'):
      return (-(S*sigma*norm.pdf(d1))/(2*ma.sqrt(T))+K*r*ma.exp(-r*T)*norm.cdf(-d2))

def rho(S,K,T,r,sigma,style):
    d1=(ma.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*ma.sqrt(T))
    d2=d1-sigma*ma.sqrt(T)
    if(style=='call'):
        return K*T*ma.exp(-r*T)*norm.cdf(d2)
    if(style=='put'):
        return -K*r*ma.exp(-r*T)*norm.cdf(-d2)

def vega(S,K,T,r,sigma):
    d1=(ma.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*ma.sqrt(T))
    d2=d1-sigma*ma.sqrt(T)
    return S*norm.pdf(d1)*ma.sqrt(T)

S=100       # So le prix du sous-jacent a t=0
sigma= 0.05  # sigma: la volatilité constante
K=105        # Strike
r=0.05
T=1
style="call"
Si=np.arange(90,120,1)
delta_=np.ones(len(Si))

for i in range(len(Si)):
    delta_[i]=delta(Si[i],K,T,r,sigma,style)

gamma_=np.ones(len(Si))
for i in range(len(Si)):
    gamma_[i]=gamma(Si[i],K,T,r,sigma,style)

Ti=np.arange(0.1,2.5,0.1)
theta_=np.ones(len(Ti))

for i in range(len(Ti)):
    theta_[i]=black_scholes(S,K,Ti[i],r,sigma,style)
    
Sigma_i=np.arange(0,0.05,0.005)

vega_=np.ones(len(Sigma_i))

for i in range(len(Sigma_i)):
    
    vega_[i]=vega(S,K,T,r,Sigma_i[i])

rho_i=np.arange(0,1,0.01)
rho_=np.ones(len(rho_i))
delta_2=np.ones(len(rho_i))
for i in range(len(rho_i)):
    delta_2[i]=rho(S,K,T,rho_i[i],sigma,style)
    rho_[i]=black_scholes(S,K,T,rho_i[i],sigma,style)

#plt.plot(Ti,theta_)
#plt.show()
#plt.plot(Sigma_i,vega_)
#plt.show()
#plt.plot(Si, delta_)
plt.subplot(121)
plt.plot(rho_i,rho_)
plt.xlabel("Taux sans risque")
plt.ylabel("Rho")

plt.subplot(122)
plt.plot(rho_i,delta_2)
plt.xlabel("Taux sans risque")
plt.ylabel("Le call")

plt.show()
"""plt.plot(rho_i, rho_)
plt.show()
plt.plot(Si, gamma_)
plt.show()"""

      