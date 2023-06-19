import numpy as np
import math as ma
import matplotlib.pyplot as plt

# Sinmulation de la loi uniforme : unif
const=3000 # const nombre de simulation
N=1000    # N subdivision de la période
unif=np.random.uniform(low=0.0, high=1.0, size=const)

# Simulation de la loi normale centré reduite : norm
norm=np.ones((const,const))

unif1=np.random.uniform(low=0.0, high=1.0, size=(const,const))
unif2=np.random.uniform(low=0.0, high=1.0, size=(const,const))
for j in range(const):
      for i in range(0,const):
        norm[i]=(ma.sqrt(-ma.log2(unif1[i]))*ma.cos(2*ma.pi*unif2[i]) + ma.sqrt(-ma.log2((1-unif1[i])))*ma.cos(2*ma.pi*(1-unif2[i])))/2
