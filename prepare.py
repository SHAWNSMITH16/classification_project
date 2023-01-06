
import pandas as pd
from env import get_connection
import os

import numpy as np
import matplotlib.pyplot as plt

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


def train_val_test(df, col):
    '''This function takes in a dataframe that has been prepared and splits it into train, validate, and test
    sections so it can be run through algorithms and tested for accuracy'''
    
    seed = 42
    
    train, val_test = train_test_split(df, train_size = 0.7, random_state = seed, stratify = df[col]) 
        
    validate, test = train_test_split(val_test, train_size = 0.6, random_state = seed, stratify = val_test[col])
    
    return train, validate, test #these will be returned in the order in which they are sequenced