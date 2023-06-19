

import numpy as np
import math as ma
def payoff(bool, so, k):
     if (bool==True):
         return np.max(so-k,0)

         
     return np.max(k-so,0)
 
        

    
    
