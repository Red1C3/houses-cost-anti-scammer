import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class Model:
    def __init__(self,rules_maker,output_precision=1):
        self.input_vars=self.model_input_vars()

        self.price_var=ctrl.Consequent(np.arange(0,8e6,output_precision),'price')
        self.price_var['cheap']=fuzz.gaussmf(self.price_var.universe,0,0.5e6)
        self.price_var['affordable']=fuzz.gaussmf(self.price_var.universe,1e6,0.25e6)
        self.price_var['expensive']=fuzz.trapmf(self.price_var.universe,[1e6,2e6,8e6,8e6])

        self.rules=rules_maker.get_rules(self.input_vars,self.price_var)
        
        self.fuzzy_system=ctrl.ControlSystemSimulation(ctrl.ControlSystem(self.rules))

    def predict(self,input_dict:dict):
        if 'distance' not in input_dict.keys():
            input_dict['distance']=np.sqrt((input_dict['lat'] - 47.548320) ** 2 + (input_dict['long'] - 122.229983) ** 2)

        return self._predict(input_dict)

    def _predict(self,input_dict:dict):
        for k,v in input_dict.items():
            if k not in self.input_vars.keys():
                continue
            self.fuzzy_system.input[k]=v

        self.fuzzy_system.compute()

        return (self.fuzzy_system.output['price'],'cheap') #TODO second item must be infered by defuzzification

    def model_input_vars(self):
        sqft_living=ctrl.Antecedent(np.arange(0,15000),'sqft_living')
        sqft_living['small']=fuzz.trimf(sqft_living.universe,[0,0,3000])
        sqft_living['med']=fuzz.trimf(sqft_living.universe,[1000,3000,6000])
        sqft_living['large']=fuzz.trapmf(sqft_living.universe,[4500,5000,15000,15000])

        sqft_lot=ctrl.Antecedent(np.arange(0,2e6),'sqft_lot')
        sqft_lot['small']=fuzz.trimf(sqft_lot.universe,[0,0,0.25e6])
        sqft_lot['med']=fuzz.trimf(sqft_lot.universe,[0.1e6,0.25e6,0.3e6])
        sqft_lot['large']=fuzz.trapmf(sqft_lot.universe,[0.25e6,0.3e6,2e6,2e6])

        sqft_basement=ctrl.Antecedent(np.arange(0,6000),'sqft_basement')
        sqft_basement['small']=fuzz.trimf(sqft_basement.universe,[0,0,1000])
        sqft_basement['med']=fuzz.trimf(sqft_basement.universe,[250,1000,1750])
        sqft_basement['large']=fuzz.trapmf(sqft_basement.universe,[1000,2000,6000,6000])

        view=ctrl.Antecedent(np.arange(0,4.5,0.5),'view')
        view['bad']=fuzz.gaussmf(view.universe,0,0.7)
        view['acceptable']=fuzz.gaussmf(view.universe,2,0.6)
        view['good']=fuzz.gaussmf(view.universe,4,0.7)

        bedrooms=ctrl.Antecedent(np.arange(0,40),'bedrooms')
        bedrooms['few']=fuzz.trimf(bedrooms.universe,[0,0,3])
        bedrooms['enough']=fuzz.trimf(bedrooms.universe,[1,3,7])
        bedrooms['lot']=fuzz.trapmf(bedrooms.universe,[4,9,40,40])

        bathrooms=ctrl.Antecedent(np.arange(0,9.25,0.25),'bathrooms')
        bathrooms['few']=fuzz.trimf(bathrooms.universe,[0,0,2])
        bathrooms['enough']=fuzz.trimf(bathrooms.universe,[1,2,4])
        bathrooms['lot']=fuzz.trapmf(bathrooms.universe,[2,4,9,9])

        floors=ctrl.Antecedent(np.arange(1,4.5,0.5),'floors')
        floors['few']=fuzz.trimf(floors.universe,[1,1,2])
        floors['med']=fuzz.trimf(floors.universe,[1.5,2.5,3.5])
        floors['lot']=fuzz.trimf(floors.universe,[2.5,4,4])

        condition=ctrl.Antecedent(np.arange(1,5.5,0.5),'condition')
        condition['poor']=fuzz.gaussmf(condition.universe,1,0.4)
        condition['acceptable']=fuzz.gaussmf(condition.universe,3,0.8)
        condition['good']=fuzz.gaussmf(condition.universe,5,0.7)

        distance=ctrl.Antecedent(np.arange(0,250,0.1),'distance')
        distance['close']=fuzz.trapmf(distance.universe,[0,0,244,244.2])
        distance['med']=fuzz.trimf(distance.universe,[244,244.2,244.4])
        distance['far']=fuzz.trimf(distance.universe,[244.2,250,250])

        return {'sqft_living':sqft_living,'sqft_lot':sqft_lot,'sqft_basement':sqft_basement,'view':view,'bedrooms':bedrooms,
        'bathrooms':bathrooms,'floors':floors,'condition':condition,'distance':distance}