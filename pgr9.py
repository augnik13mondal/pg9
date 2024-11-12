import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('C:/Users/M4PC-56/Desktop/car.csv')
data.plot(kind='bar', x='Car Brand', y='Number of Cars Sold', color='skyblue', figsize=(10, 6))
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
