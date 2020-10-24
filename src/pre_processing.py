import pandas as pd
import numpy as np
from shingling import shingling

def map_shingles(fname,n_gram):
    data=pd.read_csv(fname,delimiter=('\t'))
    documents=data['sequence']
    shingle_codes={}
    all_shingles=set()
    for doc in documents:
        shingles=shingling(doc,n_gram)
        all_shingles.update(shingles)
    count=0
    for shingle in all_shingles:
        shingle_codes[shingle]=count
        count=count+1
    return (shingle_codes,count)

            
        
        

