import numpy as np

def root_pehe(true_cate, estimated_cate):
    return np.sqrt(((estimated_cate - true_cate)**2).mean())