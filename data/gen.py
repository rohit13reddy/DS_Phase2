import random
from turtle import pd
a=[]
for i in range(999):
    b=[]
    for j in range(999):
        b.append(random.randint(0,10))
    a.append(b)


import pandas as pd
df=pd.DataFrame(a)
df.columns=range(0,999)
df.index=range(0,999)
df.to_csv("new1.csv")

