from sklearn.feature_extraction.text import TfidfVectorizer # vectorizes the data
from sklearn.metrics.pairwise import cosine_similarity # finds similarity between vectors

import pandas as pd # dataframe library

filename = r"csv\kdrama_data.csv"

df = pd.read_csv(filename)

df = df[['title', 'description', 'keywords', 'genres', 'actors', 'director', 'screenwriter']]

def fill_na():
    """replaces all na values with an empty string to prevent error"""
    df.replace("N/A", "")
    for label in df.columns:
        df[label] = df[label].fillna('') # fills N/A values with ""

fill_na()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['keywords'] + " " + df['genres']
 + " " + df['actors'] + " " + df['director'] + " " + df['screenwriter'])

# uses cosine to find the angle between the vector to find level of similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# indices of kdramas (e.g. top rank = 0 = move to heaven)
indices = pd.Series(df.index, index=df['title'])
indices = indices[~indices.index.duplicated(keep='last')]

def search_kdrama(kdrama_name, kdrama_indices):
    """searches kdrama for matching names """
    return kdrama_indices[kdrama_indices.index.str.contains(kdrama_name, na=False)]

def get_recommended_kdramas(target_kdrama_index, kdrama_similarities, kdramas_df):
    similarity_scores = pd.DataFrame(kdrama_similarities[target_kdrama_index], columns=["score"])
    kdrama_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return pd.concat([kdramas_df['title'].iloc[kdrama_indices], similarity_scores.iloc[kdrama_indices]], axis = 1)

get_recommended_kdramas(1, cosine_sim, df)
search_kdrama("Move", indices)
