import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from math import radians, cos, sin, asin, sqrt
def distance(long,lat):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(long)
    lon2 = radians(-122.229983)
    lat1 = radians(lat)
    lat2 = radians(47.548320)
      
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a)) 
    
    # Radius of earth in kilometers.
    r = 6371
      
    # calculate the result
    return(c * r)

class Model:
    def __init__(self,rules_maker,output_precision=1):
        self.input_vars=self.model_input_vars()

        self.price_var=ctrl.Consequent(np.arange(0,8e6,output_precision),'price')
        self.price_var['cheap']=fuzz.gaussmf(self.price_var.universe,0,0.5e6)
        self.price_var['affordable']=fuzz.gaussmf(self.price_var.universe,1e6,0.25e6)
        self.price_var['expensive']=fuzz.trapmf(self.price_var.universe,[1e6,2e6,8e6,8e6])

        self.rules=rules_maker.get_rules(self.input_vars,self.price_var)
        
        self.fuzzy_system=ctrl.ControlSystemSimulation(ctrl.ControlSystem(self.rules))

    def predict(self,input_dict:dict,mode:str='centroid'):
        if 'distance' not in input_dict.keys():
            input_dict['distance']=distance(input_dict['long'],input_dict['lat'])

        input_dict['amenities']=(input_dict['bathrooms'] * 100) + (input_dict['condition'] * 75) + (input_dict['bedrooms'] * 75) + (input_dict['floors'] * 75) + (input_dict['view']*85)

        return self._predict(input_dict,mode)

    def _predict(self,input_dict:dict,mode:str):
        for k,v in input_dict.items():
            if k not in self.input_vars.keys():
                continue
            self.fuzzy_system.input[k]=v

        self.fuzzy_system.compute()

        memberships=ctrl.controlsystem.CrispValueCalculator(self.price_var,self.fuzzy_system).find_memberships()

        return fuzz.defuzz(memberships[0],memberships[1],mode)

    def model_input_vars(self):
        sqft_living=ctrl.Antecedent(np.arange(1,15000),'sqft_living')
        sqft_living['small']=fuzz.trimf(sqft_living.universe,[1,1,1675])
        sqft_living['med']=fuzz.trimf(sqft_living.universe,[1500,2000,2484])
        sqft_living['large']=fuzz.trapmf(sqft_living.universe,[2200,2700,13540,13540])

        sqft_lot=ctrl.Antecedent(np.arange(0,2e6),'sqft_lot')
        sqft_lot['small']=fuzz.trimf(sqft_lot.universe,[0,0,0.25e6])
        sqft_lot['med']=fuzz.trimf(sqft_lot.universe,[0.1e6,0.25e6,0.3e6])
        sqft_lot['large']=fuzz.trapmf(sqft_lot.universe,[0.25e6,0.3e6,2e6,2e6])

        sqft_basement=ctrl.Antecedent(np.arange(0,6000),'sqft_basement')
        sqft_basement['small']=fuzz.trimf(sqft_basement.universe,[0,0,1000])
        sqft_basement['med']=fuzz.trimf(sqft_basement.universe,[250,1000,1750])
        sqft_basement['large']=fuzz.trapmf(sqft_basement.universe,[1000,2000,6000,6000])

        amenities=ctrl.Antecedent(np.arange(0,3525,25),'amenities')
        amenities['poor']=fuzz.gaussmf(amenities.universe,0,250)
        amenities['acceptable']=fuzz.gaussmf(amenities.universe,851,200)
        amenities['good']=fuzz.trapmf(amenities.universe,[983,1600,3500,3500])

        distance=ctrl.Antecedent(np.arange(0,80,0.1),'distance')
        distance['close']=fuzz.trapmf(distance.universe,[0,0,10,13])
        distance['med']=fuzz.trimf(distance.universe,[12,15,18])
        distance['far']=fuzz.trapmf(distance.universe,[17,20,90,90])

        return {'sqft_living':sqft_living,'sqft_lot':sqft_lot,'sqft_basement':sqft_basement,'amenities':amenities,'distance':distance}