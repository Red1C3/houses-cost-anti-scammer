from skfuzzy import control as ctrl

from . import and_rule,and_rule2

SMALL='small'
MED='med'
LARGE='large'
POOR='poor'
ACCEPTABLE='acceptable'
GOOD='GOOD'
CLOSE='CLOSE'
FAR='far'
CHEAP='cheap'
AFFORDABLE='affordable'
EXPENSIVE='expensive'


class RulesMakerExplicit:


    def r(self,sqft_living,amenities,distance,price):
        return and_rule2(sqft_living,amenities,distance,price,self.input_vars,self.output_var)


    def get_rules(self,input_vars,output_var):
        self.input_vars=input_vars
        self.output_var=output_var
        #TODO fill PRICE correctly
        return [
            r(SMALL,POOR,FAR,CHEAP),
            r(SMALL,POOR,MED,CHEAP),
            r(SMALL,POOR,CLOSE,CHEAP),
            r(SMALL,ACCEPTABLE,FAR,CHEAP),
            r(SMALL,ACCEPTABLE,MED,CHEAP),
            r(SMALL,ACCEPTABLE,CLOSE,CHEAP),
            r(SMALL,GOOD,FAR,CHEAP),
            r(SMALL,GOOD,MED,CHEAP),
            r(SMALL,GOOD,CLOSE,CHEAP),
            r(MED,POOR,FAR,CHEAP),
            r(MED,POOR,MED,CHEAP),
            r(MED,POOR,CLOSE,CHEAP),
            r(MED,ACCEPTABLE,FAR,CHEAP),
            r(MED,ACCEPTABLE,MED,CHEAP),
            r(MED,ACCEPTABLE,CLOSE,CHEAP),
            r(MED,GOOD,FAR,CHEAP),
            r(MED,GOOD,MED,CHEAP),
            r(MED,GOOD,CLOSE,CHEAP),
            r(LARGE,POOR,FAR,CHEAP),
            r(LARGE,POOR,MED,CHEAP),
            r(LARGE,POOR,CLOSE,CHEAP),
            r(LARGE,ACCEPTABLE,FAR,CHEAP),
            r(LARGE,ACCEPTABLE,MED,CHEAP),
            r(LARGE,ACCEPTABLE,CLOSE,CHEAP),
            r(LARGE,GOOD,FAR,CHEAP),
            r(LARGE,GOOD,MED,CHEAP),
            r(LARGE,GOOD,CLOSE,CHEAP),
        ]