import pandas as pd
from tqdm import tqdm
from sklearn.metrics import r2_score
from model.model import Model
from rules_makers.dummy import DummyRulesMaker
from rules_makers.rule_maker import RulesMaker
from rules_makers.rule_maker_plus import RulesMakerPlus
from rules_makers.rule_maker_explicit import RulesMakerExplicit
from rules_makers.rule_maker2 import RulesMaker2
from rules_makers.rule_maker3 import RulesMaker3
from rules_makers.rule_maker4 import RulesMaker4
import numpy as np
import math

tqdm.pandas()

error=0

def run(samples_cap=None):
    model=Model(RulesMaker4(),10000)    

    data=pd.read_csv('kc_house_data.csv')

    data=data[['sqft_living','sqft_lot','view','bedrooms','bathrooms','floors','condition','lat','long','location_rating','price']]

    def ae(x):
        global error
        error+= (model.predict(x[:-1].to_dict())- x[-1])**2
    
    if samples_cap is not None:
        data=data[:samples_cap]

    data['y_pred']=data.progress_apply(model.predict,axis=1)

    # data.progress_apply(ae,axis=1)
    

    return r2_score(data['price'],data['y_pred'])