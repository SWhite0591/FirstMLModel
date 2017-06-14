
from sklearn.linear_model import LinearRegression
import pandas as pd

full_data = pd.read_csv("Data.csv")
clf = LinearRegression()
clf.fit(full_data[['Gender', 'Height']], full_data["Weight"])

print clf.predict([[1, 172]])