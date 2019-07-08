import os
import pandas as pd

file_names = pd.read_csv("names.txt",header = None)
file_names = file_names.iloc[:,0].tolist()

for name in file_names:
	name_ = name.split(".")[0]
	os.system("mv {}/{}.csv {}/counts.csv".format(name_, name_, name_))
