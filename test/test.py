import pandas as pd
from tqdm import tqdm
from model.model import Model
from rules_makers.dummy import DummyRulesMaker
from sklearn.preprocessing import MinMaxScaler
import numpy as np

tqdm.pandas()

error=0

def run(samples_cap=None):

    minmaxscaler=MinMaxScaler()


    model=Model(DummyRulesMaker(),10000)    

    data=pd.read_csv('kc_house_data.csv')

    minmaxscaler=minmaxscaler.fit([[75000.0],[7700000.0]])

    data=data[['sqft_living','sqft_lot','sqft_basement','view','bedrooms','bathrooms','floors','condition','lat','long','price']]

    def ae(x):
        global error
        error+=abs( minmaxscaler.transform( np.array( model.predict(x[:-1].to_dict())).reshape(-1,1))[0][0]- minmaxscaler.transform( np.array([x[-1]]).reshape(-1,1))[0][0])
    
    if samples_cap is not None:
        data=data[:samples_cap]

    data.progress_apply(ae,axis=1)

    return error/data.shape[0]