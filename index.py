import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
pip install sklearn
from sklearn import datasets
df=pd.read_csv('Iris.csv')
df.head()
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')