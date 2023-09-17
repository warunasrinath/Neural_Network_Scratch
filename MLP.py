#finsh following method
import numpy as np

def set_weight(self, w_init):
    #set the weight. w_init is a python list with the weights
    self.weight = np.array(w_init)

def sigmoid(self, x):
    #Evaluate the sigmoid function for the floating point input x.
    return 1/(1+np.exp(-x))


    