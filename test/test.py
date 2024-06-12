import pandas as pd
from tqdm import tqdm
from model.model import Model
from rules_makers.dummy import DummyRulesMaker
from rules_makers.rule_maker import RulesMaker
from rules_makers.rule_maker_plus import RulesMakerPlus
from rules_makers.rule_maker_explicit import RulesMakerExplicit
from rules_makers.rule_maker2 import RulesMaker2
import numpy as np
import math

tqdm.pandas()

error=0

def run(samples_cap=None):
    model=Model(RulesMaker2(),10000)    

    data=pd.read_csv('kc_house_data.csv')

    data=data[['sqft_living','sqft_lot','view','bedrooms','bathrooms','floors','condition','lat','long','location_rating','price']]

    def ae(x):
        global error
        error+= (model.predict(x[:-1].to_dict())- x[-1])**2
    
    if samples_cap is not None:
        data=data[:samples_cap]

    data.progress_apply(ae,axis=1)

    return math.log( error/data.shape[0]+1)