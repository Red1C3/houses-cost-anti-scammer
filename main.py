#!.venv/bin/python
import sys
from model.model import Model
import matplotlib.pyplot as plt
from rules_makers.dummy import DummyRulesMaker
from rules_makers.rule_maker import RulesMaker
from test import test
import warnings

warnings.filterwarnings(action='ignore')

def main():
    # Run test if test was given in CLI
    if len(sys.argv)>1 and sys.argv[1]=='test':
        if len(sys.argv)>2:
            res=test.run(int(sys.argv[2]))
        else:
            res=test.run()
        print(res)
        return


    model=Model(RulesMaker(),1e4)
    print(model.predict({'sqft_living':0,'sqft_lot':0,'sqft_basement':0,'view':0,'bedrooms':0,'bathrooms':0,'floors':1,'condition':1,'lat':47.5112,'long':-122.257}))

if __name__=='__main__':
    main()