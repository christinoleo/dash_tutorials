import plotly.express as px
import pandas as pd

df = pd.read_csv("../2_LifeExpectancyTable/life_expectancy_years.csv")
print(df)

fig = px.bar(df, x='country', y='1800')
fig.show()