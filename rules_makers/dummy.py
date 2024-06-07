from . import and_rule

class DummyRulesMaker:
    def get_rules(self,input_vars,output_var):
        return [and_rule('small','small','small','bad','few','few','few','poor','close','cheap',input_vars,output_var)]