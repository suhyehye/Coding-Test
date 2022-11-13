import numpy as np
def solution(n):
    if np.sqrt(n).is_integer():
        return (np.sqrt(n)+1)**2
    else:
        return -1
