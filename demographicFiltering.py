import pandas as pd
import numpy as np

df = pd.read_csv("flask1/final.csv")






C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)

print(C, m)

movies = df.copy().loc[df["vote_count"] >= m]

print(movies.shape)

def weighted(x, m=m, C=C):
  #x = int(x)
  v = x["vote_count"]
  r = x["vote_average"]
  return (v/(v+m) * r) + (m/(m+v) * C)

movies["score"] = movies.apply(weighted, axis = 1) # 1 removies columns, 0 removes rows 

movies = movies.sort_values("score", ascending = False)

movies[["original_title","vote_count","vote_average","score"]].head(15)

import plotly.express as px

fig = px.bar((movies.head(20).sort_values("score", 
                                          ascending = True, )), x = "score", y = "original_title", orientation = "h",)

fig.show()