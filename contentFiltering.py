import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

df = pd.read_csv("flask1/final.csv")

df = df[df['soup'].notna()]


from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df.reset_index()
indices = pd.Series(df2.index, index=df2['original_title'])

def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df2[["original_title","overview", "runtime"]].iloc[movie_indices].values.tolist()


get_recommendations('The Dark Knight')

