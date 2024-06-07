import pandas as pd
from tqdm import tqdm
from model.model import Model
from rules_makers.dummy import DummyRulesMaker

tqdm.pandas()

error=0

def run(samples_cap=None):

    model=Model(DummyRulesMaker(),10000)    

    data=pd.read_csv('kc_house_data.csv')
    
    data=data[['sqft_living','sqft_lot','sqft_basement','view','bedrooms','bathrooms','floors','condition','lat','long','price']]

    def se(x):
        global error
        error+=(model.predict(x[:-1].to_dict())-x[-1])**2
    
    if samples_cap is not None:
        data=data[:samples_cap]

    data.progress_apply(se,axis=1)

    return error/data.shape[0]