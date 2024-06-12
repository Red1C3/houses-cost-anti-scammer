from skfuzzy import control as ctrl

from . import and_rule

class RulesMaker2:
    def get_rules(self,input_vars,output_var):
        return [
            ctrl.Rule(input_vars['location']['poor'],output_var['cheap']),
            ctrl.Rule(input_vars['location']['acceptable'] & input_vars['amenities']['poor'],output_var['cheap']),
            ctrl.Rule(input_vars['location']['acceptable'] & input_vars['amenities']['acceptable'] & (input_vars['size']['small'] | input_vars['size']['med']),output_var['affordable']),
            ctrl.Rule(input_vars['location']['acceptable'] & input_vars['amenities']['acceptable'] & input_vars['size']['large'],output_var['expensive']),
            ctrl.Rule(input_vars['location']['acceptable'] & input_vars['amenities']['good'],output_var['expensive']),
            ctrl.Rule(input_vars['location']['good'] & input_vars['amenities']['poor'] & input_vars['size']['small'],output_var['cheap']),
            ctrl.Rule(input_vars['location']['good'] & input_vars['amenities']['acceptable'] & (input_vars['size']['med'] | input_vars['size']['small']),output_var['affordable']),
            ctrl.Rule(input_vars['location']['good'] & input_vars['amenities']['good'],output_var['expensive'])
        ]