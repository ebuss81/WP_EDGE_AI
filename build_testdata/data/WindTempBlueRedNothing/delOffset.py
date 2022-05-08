import pandas as pd
import os

for file in sorted(os.listdir()):
	if file.endswith(".tsv"):
	    df = pd.read_csv(file, sep='\t', header=None)
	    df.loc[ : , df.columns != 0] = df.loc[ : , df.columns != 0] - 512000
	    df.to_csv(file, sep="\t", header=None, index=False)
	    #print(df.head())
