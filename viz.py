#Visualize the battings.csv based on the frequency of player inclusion yearwise.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Batting.csv')
dataset.head(5)
df1 = dataset.groupby('yearID')['playerID'].count()
plt.figure(figsize=(15,10),dpi=100)
plt.plot(df1, linestyle='dotted', marker = '*', color = 'blue', label = 'Players')
plt.xlabel('Year')
plt.ylabel('Players Included')
plt.show()

