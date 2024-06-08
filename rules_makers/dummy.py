from skfuzzy import control as ctrl

from . import and_rule

class DummyRulesMaker:
    def get_rules(self,input_vars,output_var):
        return [
            ctrl.Rule(input_vars['sqft_living']['small'] | input_vars['sqft_living']['med'] | input_vars['sqft_living']['large'] |
             input_vars['sqft_lot']['small'] | input_vars['sqft_lot']['med'] | input_vars['sqft_lot']['large'] |
             input_vars['sqft_basement']['small'] | input_vars['sqft_basement']['med'] | input_vars['sqft_basement']['large'] |
             input_vars['amenities']['poor'] | input_vars['amenities']['acceptable'] | input_vars['amenities']['good'] |
             input_vars['distance']['close'] | input_vars['distance']['med'] | input_vars['distance']['far']
            ,output_var['cheap'])
        ]