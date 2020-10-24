import pandas as pd
import numpy as np

def shingling(data,n_gram):
    shingles=set()
    for i in range(0,len(data)-n_gram):
        temp=data[i:i+n_gram]
        shingles.add(temp)
    return shingles



