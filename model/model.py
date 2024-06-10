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
        self.price_var['cheap']=fuzz.trapmf(self.price_var.universe,[0,0,370000,378552])
        self.price_var['affordable']=fuzz.trapmf(self.price_var.universe,[370000, 378552, 701624, 801624])
        self.price_var['expensive']=fuzz.trapmf(self.price_var.universe,[721624, 751624, 7700000,7700000])

        self.rules=rules_maker.get_rules(self.input_vars,self.price_var)
        
        self.fuzzy_system=ctrl.ControlSystemSimulation(ctrl.ControlSystem(self.rules))

    def predict(self,input_dict:dict,mode:str='centroid'):
        self.fuzzy_system.reset()

        
        dis=distance(input_dict['long'],input_dict['lat'])

        input_dict['location']=input_dict['location_rating'] + (1/dis)

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
        sqft_living=ctrl.Antecedent(np.arange(1,13540),'sqft_living')
        sqft_living['small']=fuzz.trimf(sqft_living.universe,[1,1,1675])
        sqft_living['med']=fuzz.trimf(sqft_living.universe,[1500,2000,2484])
        sqft_living['large']=fuzz.trapmf(sqft_living.universe,[2200,2700,13540,13540])

        amenities=ctrl.Antecedent(np.arange(0,3525,25),'amenities')
        amenities['poor']=fuzz.gaussmf(amenities.universe,0,250)
        amenities['acceptable']=fuzz.gaussmf(amenities.universe,851,200)
        amenities['good']=fuzz.trapmf(amenities.universe,[983,1600,3500,3500])

        location=ctrl.Antecedent(np.arange(1,11,0.01),'location')
        location['close']=fuzz.trapmf(location.universe,[1,1,3,6.5])
        location['med']=fuzz.trimf(location.universe,[6,6.5,7])
        location['far']=fuzz.trapmf(location.universe,[6.3,6.5,11,11])

        return {'sqft_living':sqft_living,'amenities':amenities,'location':location}