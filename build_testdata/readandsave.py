import numpy as np
import pandas as pd

data_df = pd.read_csv('data/WindTempBlueRedNothing/WindTempBlueRedNothing_TEST.tsv', sep='\t', header=None,)


x_test = data_df.drop(columns=[0])
x_test.columns = range(x_test.shape[1])
x_test = x_test.values

# znorm
std_ = x_test.std(axis=1, keepdims=True)
std_[std_ == 0] = 1.0
x_test = (x_test - x_test.mean(axis=1, keepdims=True)) / std_

x_test = x_test[539,:] # get data at row
np.savetxt('c1_norm.txt', x_test.reshape(1,x_test.shape[0]),delimiter=',')