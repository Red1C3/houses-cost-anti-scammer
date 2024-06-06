#!/usr/bin/python
from model.model import Model
import matplotlib.pyplot as plt


def main():
    model=Model()
    model.input_vars['bathrooms'].view()
    plt.waitforbuttonpress()

if __name__=='__main__':
    main()