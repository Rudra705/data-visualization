import plotly.express as px
import pandas as pd 

data = pd.read_csv("data.csv")
figure = px.scatter(data, x = "date", y = "cases" , color= "country")
figure.show()
