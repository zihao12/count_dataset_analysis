import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prefix = "gtex_fallopian_tube"
Y = np.genfromtxt("{}/Y.csv".format(prefix))
L = np.genfromtxt("{}/L_nmfkl_K{}.csv".format(prefix,2))
F = np.genfromtxt("{}/F_nmfkl_K{}.csv".format(prefix,2))

print(L.shape)
print(F.shape)
print(Y.shape)
pp = Y * np.log(L.dot(F.T))

print(np.isnan(pp).sum())
