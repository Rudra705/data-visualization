import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")
figure = px.bar(data, x = "date" , y = "cases" , color = "country")
figure.show()