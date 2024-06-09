from skfuzzy import control as ctrl

from . import and_rule,and_rule2

SMALL='small'
MED='med'
LARGE='large'
POOR='poor'
ACCEPTABLE='acceptable'
GOOD='good'
CLOSE='close'
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
        r=self.r
        return [
            r(SMALL,POOR,FAR,CHEAP),
            r(SMALL,POOR,MED,CHEAP),
            r(SMALL,POOR,CLOSE,AFFORDABLE),
            r(SMALL,ACCEPTABLE,FAR,CHEAP),
            r(SMALL,ACCEPTABLE,MED,AFFORDABLE),
            r(SMALL,ACCEPTABLE,CLOSE,AFFORDABLE),
            r(SMALL,GOOD,FAR,EXPENSIVE),
            r(SMALL,GOOD,MED,EXPENSIVE),
            r(SMALL,GOOD,CLOSE,EXPENSIVE),
            r(MED,POOR,FAR,CHEAP),
            r(MED,POOR,MED,CHEAP),
            r(MED,POOR,CLOSE,AFFORDABLE),
            r(MED,ACCEPTABLE,FAR,AFFORDABLE),
            r(MED,ACCEPTABLE,MED,AFFORDABLE),
            r(MED,ACCEPTABLE,CLOSE,EXPENSIVE),
            r(MED,GOOD,FAR,EXPENSIVE),
            r(MED,GOOD,MED,EXPENSIVE),
            r(MED,GOOD,CLOSE,EXPENSIVE),
            r(LARGE,POOR,FAR,AFFORDABLE),
            r(LARGE,POOR,MED,AFFORDABLE),
            r(LARGE,POOR,CLOSE,AFFORDABLE),
            r(LARGE,ACCEPTABLE,FAR,AFFORDABLE),
            r(LARGE,ACCEPTABLE,MED,EXPENSIVE),
            r(LARGE,ACCEPTABLE,CLOSE,EXPENSIVE),
            r(LARGE,GOOD,FAR,AFFORDABLE),
            r(LARGE,GOOD,MED,EXPENSIVE),
            r(LARGE,GOOD,CLOSE,EXPENSIVE),
        ]