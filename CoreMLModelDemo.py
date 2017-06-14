
from sklearn.linear_model import LinearRegression
import pandas as pd

full_data = pd.read_csv("Data.csv")
model = LinearRegression()
model.fit(full_data[['Gender', 'Height']], full_data["Weight"])

print model.predict([[1, 172]])