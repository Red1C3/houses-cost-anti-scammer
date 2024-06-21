from skfuzzy import control as ctrl

from . import and_rule

class RulesMaker4:
    def get_rules(self,input_vars,output_var):
        return [
                ctrl.Rule(input_vars['distance']['far'],output_var['cheap']),
                ctrl.Rule(input_vars['amenities']['poor'],output_var['cheap']),
                ctrl.Rule(input_vars['size']['small'],output_var['cheap']),

                ctrl.Rule(input_vars['distance']['far'] & input_vars['amenities']['acceptable'] & input_vars['size']['med'],output_var['affordable']),
                ctrl.Rule(input_vars['distance']['med'] & input_vars['amenities']['poor'] & input_vars['size']['med'],output_var['affordable']),
                ctrl.Rule(input_vars['distance']['med'] & input_vars['amenities']['acceptable'] & input_vars['size']['small'],output_var['affordable']),

                ctrl.Rule(input_vars['distance']['med'] & input_vars['amenities']['acceptable'] & input_vars['size']['med'],output_var['affordable']),

                ctrl.Rule(input_vars['distance']['close'] & input_vars['amenities']['good'] & input_vars['size']['med'],output_var['expensive']),
                ctrl.Rule(input_vars['distance']['close'] & input_vars['amenities']['acceptable'] & input_vars['size']['large'],output_var['expensive']),
                ctrl.Rule(input_vars['distance']['med'] & input_vars['amenities']['good'] & input_vars['size']['large'],output_var['expensive']),


                ctrl.Rule(input_vars['distance']['close'] & input_vars['amenities']['good'] & input_vars['size']['large'],output_var['expensive']),

                ctrl.Rule(input_vars['distance']['close'],output_var['expensive']),
                ctrl.Rule(input_vars['amenities']['good'],output_var['expensive']),
                ctrl.Rule(input_vars['size']['large'],output_var['expensive']),
            ]