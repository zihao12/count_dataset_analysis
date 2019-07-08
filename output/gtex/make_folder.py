import os
import pandas as pd

file_names = pd.read_csv("names.txt",header = None)
file_names = file_names.iloc[:,0].tolist()

for name in file_names:
	folder_name = name.split(".")[0]
	os.system("mkdir {}".format(folder_name))
	os.system("mv {} {}".format(name, folder_name))
