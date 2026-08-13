import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

data={'First Score':[100,90,np.nan,95],
      'Second Score':[30,45,56,np.nan],
      'Third Score':[np.nan,40,70,60]}
print(data)
df=pd.DataFrame(data)
print(df)
missing_values=df.isnull()
print(missing_values)

non_missing_values=df.notnull()
print(non_missing_values)

df.fillna(0)
print(df.fillna(0))

df=pd.read_csv("/content/Iris.csv")
print(df)

print(df[['SepalLengthCm','SepalWidthCm']])

shape=df.shape
print("Shape = {}".format(shape))

size=df.size
print("Size = {}".format(size))