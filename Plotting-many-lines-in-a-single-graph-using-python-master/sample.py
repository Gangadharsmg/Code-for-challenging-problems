import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


fig, ax = plt.subplots(figsize=(4,4))
sns.lineplot(x=['A','B','C','D'],
             y=[4,2,5,3],
             color='r',
             ax=ax)
sns.lineplot(x=['A','B','C','D'],
             y=[1,6,2,4],
             color='b',
             ax=ax)
sns.lineplot(x=['A','B','C','D'],
             y=[3,7,9,8],
             color='g',
             ax=ax)
ax.legend(['alpha', 'beta','gamma'], facecolor='w')
plt.show()