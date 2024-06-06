import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class Model:
    def __init__(self):
        self.input_vars=self.model_input_vars()

    def model_input_vars(self):
        #sqft living
        sqft_living=ctrl.Antecedent(np.arange(0,15000),'sqft_living')
        sqft_living['small']=fuzz.trimf(sqft_living.universe,[0,0,3000])
        sqft_living['med']=fuzz.trimf(sqft_living.universe,[2000,4000,6000])
        sqft_living['large']=fuzz.trapmf(sqft_living.universe,[5000,6000,15000,15000])

        sqft_lot=ctrl.Antecedent(np.arange(0,2e6),'sqft_lot')
        sqft_lot['small']=fuzz.trimf(sqft_lot.universe,[0,0,0.25e6])
        sqft_lot['med']=fuzz.trimf(sqft_lot.universe,[0.15e6,0.25e6,0.3e6])
        sqft_lot['large']=fuzz.trapmf(sqft_lot.universe,[0.25e6,0.3e6,2e6,2e6])

        sqft_basement=ctrl.Antecedent(np.arange(0,6000),'sqft_basement')
        sqft_basement['small']=fuzz.trimf(sqft_basement.universe,[0,0,1000])
        sqft_basement['med']=fuzz.trimf(sqft_basement.universe,[500,1000,1500])
        sqft_basement['large']=fuzz.trapmf(sqft_basement.universe,[1000,2000,6000,6000])

        view=ctrl.Antecedent(np.arange(0,4.5,0.5),'view')
        view['bad']=fuzz.gaussmf(view.universe,0,0.4)
        view['acceptable']=fuzz.gaussmf(view.universe,2,0.6)
        view['good']=fuzz.gaussmf(view.universe,4,0.7)

        bedrooms=ctrl.Antecedent(np.arange(0,40),'bedrooms')
        bedrooms['few']=fuzz.trimf(bedrooms.universe,[0,0,2])
        bedrooms['enough']=fuzz.trimf(bedrooms.universe,[1,3,7])
        bedrooms['lot']=fuzz.trapmf(bedrooms.universe,[5,9,40,40])

        bathrooms=ctrl.Antecedent(np.arange(0,9.25,0.25),'bathrooms')
        bathrooms['few']=fuzz.trimf(bathrooms.universe,[0,0,2])
        bathrooms['enough']=fuzz.trimf(bathrooms.universe,[1,2,4])
        bathrooms['lot']=fuzz.trapmf(bathrooms.universe,[2,4,9,9])

        return {'sqft_living':sqft_living,'sqft_lot':sqft_lot,'sqft_basement':sqft_basement,'view':view,'bedrooms':bedrooms,
        'bathrooms':bathrooms}