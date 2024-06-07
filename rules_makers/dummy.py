from skfuzzy import control as ctrl

from . import and_rule

class DummyRulesMaker:
    def get_rules(self,input_vars,output_var):
        return [
            ctrl.Rule(input_vars['sqft_living']['small'] | input_vars['sqft_living']['med'] | input_vars['sqft_living']['large'] |
             input_vars['sqft_lot']['small'] | input_vars['sqft_lot']['med'] | input_vars['sqft_lot']['large'] |
             input_vars['sqft_basement']['small'] | input_vars['sqft_basement']['med'] | input_vars['sqft_basement']['large'] |
             input_vars['view']['bad'] | input_vars['view']['acceptable'] | input_vars['view']['good'] |
             input_vars['bedrooms']['few'] | input_vars['bedrooms']['enough'] | input_vars['bedrooms']['lot'] |
             input_vars['bathrooms']['few'] | input_vars['bathrooms']['enough'] | input_vars['bathrooms']['lot'] |
             input_vars['floors']['few'] | input_vars['floors']['med'] | input_vars['floors']['lot'] |
             input_vars['condition']['poor'] | input_vars['condition']['acceptable'] | input_vars['condition']['good'] |
             input_vars['distance']['close'] | input_vars['distance']['med'] | input_vars['distance']['far']
            ,output_var['cheap'])
        ]