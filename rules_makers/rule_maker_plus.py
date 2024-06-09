from skfuzzy import control as ctrl

from . import and_rule

class RulesMakerPlus:
    def get_rules(self,input_vars,output_var):
        return [
            ctrl.Rule( 
                input_vars['sqft_living']['large'] 
            &(input_vars['distance']['far'] | input_vars['sqft_living']['med'])
            &(input_vars['amenities']['poor'] | input_vars['amenities']['acceptable'] | input_vars['amenities']['good'])
            ,output_var['affordable']),



            ctrl.Rule(
                input_vars['sqft_living']['large'] 
                & input_vars['distance']['far']  
                & (input_vars['amenities']['good'] | input_vars['amenities']['acceptable'])  
                ,output_var['affordable']
                ),



            ctrl.Rule(
                input_vars['sqft_living']['large'] 
                & (input_vars['distance']['close'] | input_vars['distance']['med'] )  
                & (input_vars['amenities']['good'] | input_vars['amenities']['acceptable'])  
                ,output_var['expensive']  ),



            ctrl.Rule(
                (input_vars['sqft_living']['small'] | input_vars['sqft_living']['med'])
                & (input_vars['distance']['close'] | input_vars['distance']['med'] | input_vars['distance']['far'] )  
                & (input_vars['amenities']['poor'] | input_vars['amenities']['acceptable']) 
                ,output_var['cheap']),



            ctrl.Rule(
                (input_vars['sqft_living']['small'] | input_vars['sqft_living']['med'])
                & (input_vars['distance']['close'] | input_vars['distance']['med'] | input_vars['distance']['far'] )
                & input_vars['amenities']['good'] 
                ,output_var['expensive'])
        ]