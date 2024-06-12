from skfuzzy import control as ctrl

from . import and_rule

class RulesMaker:
    def get_rules(self,input_vars,output_var):
        return [
            ctrl.Rule(input_vars['amenities']['poor'] | input_vars['amenities']['acceptable'] ,output_var['cheap']),
            ctrl.Rule((input_vars['location']['far'] | input_vars['size']['med'])  & input_vars['size']['large'] ,output_var['affordable']),
            ctrl.Rule(input_vars['size']['large'] & input_vars['location']['far']  & (input_vars['amenities']['good'] | input_vars['amenities']['acceptable'])  ,output_var['affordable']),
            ctrl.Rule(input_vars['size']['large'] & (input_vars['location']['close'] | input_vars['location']['med'] )  & (input_vars['amenities']['good'] | input_vars['amenities']['acceptable'])  ,output_var['expensive']  ),
            ctrl.Rule(input_vars['amenities']['good'] ,output_var['expensive'])
  

        ]