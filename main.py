#!.venv/bin/python
import sys
from model.model import Model
import matplotlib.pyplot as plt
import customtkinter as ctk
from rules_makers.rule_maker import RulesMaker
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


if __name__=='__main__':
    main()