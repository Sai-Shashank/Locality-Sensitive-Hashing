import pandas as pd
import numpy as np
from shingling import shingling

def map_shingles(fname,n_gram):
    data=pd.read_csv(fname,delimiter=('\t'))
    documents=data['sequence']
    shingle_codes={}
    all_shingles=set()
    shingle_set=[set() for _ in range(0,len(documents))]
    doc_count=0
    for doc in documents:
        shingles=shingling(doc,n_gram)
        shingle_set[doc_count].update(shingles)
        all_shingles.update(shingles)
        doc_count=doc_count+1
    count=0
    for shingle in all_shingles:
        shingle_codes[shingle]=count
        count=count+1
    return (shingle_codes,count,shingle_set)

def gen_matrix(shingle_codes,count,shingle_set):
    sparse_matrix=np.zeros((count+1,len(shingle_set)))
    for i in range(0,len(shingle_set)):
        for shingles in shingle_set[i]:
            sparse_matrix[shingle_codes[shingles]][i]=1
    return sparse_matrix

   
    
            
        
        

