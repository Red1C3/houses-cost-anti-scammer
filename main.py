#!.venv/bin/python
import sys
from model.model import Model
import matplotlib.pyplot as plt
import customtkinter as ctk
from rules_makers.dummy import DummyRulesMaker
from rules_makers.rule_maker import RulesMaker
from rules_makers.rule_maker4 import RulesMaker4
from test import test
import warnings
from gui import GUI

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
    
    
    root = ctk.CTk()
    GUI(root)
    root.mainloop()


    model=Model(RulesMaker4(),1e4)
    print(model.predict({'sqft_living':0,'sqft_lot':0,'view':0,'bedrooms':0,'bathrooms':0,
    'floors':0,'condition':1,'lat':47.5112,'long':-122.257,'location_rating':1}))

    print(model.predict({'sqft_living':0,'sqft_lot':0,'view':3,'bedrooms':1,'bathrooms':1,
    'floors':2,'condition':5,'lat':46.5112,'long':-123.257,'location_rating':6}))


if __name__=='__main__':
    main()