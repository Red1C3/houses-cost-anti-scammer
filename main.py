#!/usr/bin/python
from model.model import Model
import matplotlib.pyplot as plt
from rules_makers.dummy import DummyRulesMaker

def main():
    model=Model(DummyRulesMaker())
    print(model.predict({'sqft_living':0,'sqft_lot':0,'sqft_basement':0,'view':0,'bedrooms':0,'bathrooms':0,'floors':1,'condition':1,'lat':47.548320,'long':122.229983}))

if __name__=='__main__':
    main()