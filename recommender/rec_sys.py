from sklearn.feature_extraction.text import TfidfVectorizer # vectorizes the data
from sklearn.metrics.pairwise import cosine_similarity # finds similarity between vectors

import pandas as pd # dataframe library

filename = "csv\shows.csv"

df = pd.read_csv(filename)
df = df[['Name', 'Rank', 'Synopsis']]

tfidf = TfidfVectorizer(stop_words='english')
df['Synopsis'] = df['Synopsis'].fillna('') # null synposis = ""

tfidf_matrix = tfidf.fit_transform(df['Synopsis'])
tfidf_matrix.shape # (100, 1853) means 100 movies, 1853 unique words

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix) # calculates similarity between each drama (?)
cosine_sim[0][1] # compares similarity between number 1 movie with number 2 movie

indices = pd.Series(df.index, index=df['Name'])
indices = indices[~indices.index.duplicated(keep='last')]

def search_kdrama(kdrama_name, kdrama_indices):
    return kdrama_indices[kdrama_indices.index.str.contains(kdrama_name, na=False)]

def get_recommended_kdramas(target_kdrama_index, kdrama_similarities, kdramas_df):
    similarity_scores = pd.DataFrame(kdrama_similarities[target_kdrama_index], columns=["score"])
    kdrama_indices = similarity_scores.sort_values("score", ascending=False)[0:11].index
    return df['Name'].iloc[kdrama_indices]