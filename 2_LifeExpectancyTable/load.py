import pandas as pd

csv = pd.read_csv("life_expectancy_years.csv")

print(csv.head().columns)