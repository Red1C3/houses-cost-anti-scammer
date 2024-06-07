#!/usr/bin/python
from model.model import Model
import matplotlib.pyplot as plt
from rules_makers.dummy import DummyRulesMaker

def main():
    model=Model(DummyRulesMaker())
    model.input_vars['bathrooms'].view()

if __name__=='__main__':
    main()