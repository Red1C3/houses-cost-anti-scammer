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

        self.price_var=ctrl.Consequent(np.arange(0,9e5,output_precision),'price')
        self.price_var['cheap']=fuzz.gaussmf(self.price_var.universe,0,1e5)
        self.price_var['affordable']=fuzz.gaussmf(self.price_var.universe,3.7e5,1e5)
        self.price_var['expensive']=fuzz.gaussmf(self.price_var.universe,9e5,1.5e5)

        self.rules=rules_maker.get_rules(self.input_vars,self.price_var)
        
        self.fuzzy_system=ctrl.ControlSystemSimulation(ctrl.ControlSystem(self.rules))

    def predict(self,input_dict:dict,mode:str='centroid'):
        self.fuzzy_system.reset()

        if 'distance' not in input_dict.keys():
            dis=distance(input_dict['long'],input_dict['lat'])
            input_dict['distance']=dis

        input_dict['amenities']=input_dict['condition']

        input_dict['size']=input_dict['sqft_living']

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
        size=ctrl.Antecedent(np.arange(600,6001,1),'size')
        size['small']=fuzz.trimf(size.universe,[600,600,2500])
        size['med']=fuzz.trimf(size.universe,[1500,3000,4500])
        size['large']=fuzz.trimf(size.universe,[4000,6000,6000])

        amenities=ctrl.Antecedent(np.arange(0,5.5,0.5),'amenities')
        amenities['poor']=fuzz.gaussmf(amenities.universe,0,0.75)
        amenities['acceptable']=fuzz.gaussmf(amenities.universe,2.5,0.75)
        amenities['good']=fuzz.gaussmf(amenities.universe,5,0.75)

        distance=ctrl.Antecedent(np.arange(0,51,1),'distance')
        distance['close']=fuzz.gaussmf(distance.universe,0,7)
        distance['med']=fuzz.gaussmf(distance.universe,25,7)
        distance['far']=fuzz.gaussmf(distance.universe,50,7)

        return {'size':size,'amenities':amenities,'distance':distance}