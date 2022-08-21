import pandas as pd

maxdat = pd.read_csv('Max.dat',sep='\t',skiprows=[0,1],header=)
#mindat = pd.read_csv('Min.dat')

print(maxdat)
