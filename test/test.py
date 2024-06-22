import pandas as pd
from tqdm import tqdm
from sklearn.metrics import r2_score
from model.model import Model
from rules_makers.rule_maker import RulesMaker
import numpy as np
import math

tqdm.pandas()

error=0

def run(samples_cap=None):
    model=Model(RulesMaker(),10000)    

    data=pd.read_csv('kc_house_data.csv')

    data=data[['sqft_living','condition','lat','long','price']]

    def ae(x):
        global error
        error+= (model.predict(x[:-1].to_dict())- x[-1])**2
    
    if samples_cap is not None:
        data=data[:samples_cap]


    data.progress_apply(ae,axis=1)
    

    return math.log(error)