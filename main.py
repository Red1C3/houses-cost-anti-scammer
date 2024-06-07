#!.venv/bin/python
import sys
from model.model import Model
import matplotlib.pyplot as plt
from rules_makers.dummy import DummyRulesMaker
from test import test

def main():
    # Run test if test was given in CLI
    if len(sys.argv)>1 and sys.argv[1]=='test':
        if len(sys.argv)>2:
            res=test.run(int(sys.argv[2]))
        else:
            res=test.run()
        print(res)
        return


    model=Model(DummyRulesMaker(),1e5)
    print(model.predict({'sqft_living':0,'sqft_lot':0,'sqft_basement':0,'view':0,'bedrooms':0,'bathrooms':0,'floors':1,'condition':1,'lat':47.548320,'long':122.229983}))

if __name__=='__main__':
    main()