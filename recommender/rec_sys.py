import pandas as pd  # dataframe library
from sklearn.feature_extraction.text import \
    TfidfVectorizer  # vectorizes the data
from sklearn.metrics.pairwise import \
    cosine_similarity  # finds similarity between vectors

# filename = "csv\shows.csv"
filename = r"C:\Users\John Kim\Desktop\kdrama_data.csv"

<<<<<<< HEAD
label_weights = {
        "keywords": 0.4,
        "genres": 0.3,
        "actors": 0.2,
        "director": 0.05,
        "screenwriter": 0.05,
    }

df = pd.read_csv(filename)
df = df[['title', 'description', 'keywords', 'genres', 'actors', 'director', 'screenwriter']]

def fill_na():
    """replaces na values with an empty string"""
    df.replace("N/A", "")
    for label in df.columns:
        df[label] = df[label].fillna('') # fills N/A values with ""

fill_na()

def get_indices():
    indices = pd.Series(df.index, index=df['title'])
    return indices[~indices.index.duplicated(keep='last')]

def og_cos_sim():
    """the similarity scores used to get the initial top x kdramas"""
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['keywords'] + " " + df['genres']
    + " " + df['actors'] + " " + df['director'] + " " + df['screenwriter'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def search_kdrama(kdrama_name, kdrama_indices):
    """searches for kdrama with matching name and returns top result"""
    return kdrama_indices[kdrama_indices.index.str.contains(kdrama_name, regex=False, na=False)][0] 
=======
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
>>>>>>> beac7f0646d462dbf85aa5b2b152214c58812699

def get_recommended_kdramas(target_kdrama_index, kdrama_similarities, kdramas_df, rec_num):
    """returns the top (rec_num) recommended kdramas based on keywords, genres, actors, director, director
    and screenwriter (we recalculate their similarity score by using our own 'weights' :omg:)"""
    if rec_num <= 1:
        # return no kdramas
        return False

    # should set a max on how many recommended kdrama you can get (maybe like 25 or 50?)
    similarity_scores = pd.DataFrame(kdrama_similarities[target_kdrama_index], columns=["score"])
<<<<<<< HEAD
    kdrama_indices = similarity_scores.sort_values("score", ascending=False)[1:rec_num].index # gets top 10 (we can change this)
    return kdramas_df['title'].iloc[kdrama_indices].values # converts to array

def get_score(og_name, rec_name, indices, sim):
    """gets the similarity score of a kdrama based on ONE aspect (e.g. only keywords)"""
    rec_index = search_kdrama(rec_name, indices)
    scores = sim[search_kdrama(og_name, indices)]
    return scores[rec_index]

def vectorize_kdrama(col_name):
    """vectorizes the kdrama based on ONE aspect (e.g. only keywords)"""
    tfidf = TfidfVectorizer(stop_words='english')
    return tfidf.fit_transform(df[col_name])

def find_similarity(matrix):
    """finds the similarity between this matrix's kdrama and everything else"""
    return cosine_similarity(matrix, matrix)

def create_similarity_data(name):
    """creates a dictionary of arrays with the top 10 similar kdramas"""
    similarity_data = {
        "titles": [],
        "keywords": [],
        "genres": [],
        "actors": [],
        "director": [],
        "screenwriter": [],
    }

    target_index = search_kdrama(name, get_indices())
    top_ten = get_recommended_kdramas(target_index, og_cos_sim(), df, 10)

    for kdrama in top_ten:
        # adds this title to dictionary
        similarity_data["titles"].append(kdrama)
        for label in label_weights.keys():
            vec = vectorize_kdrama(label)
            sim = find_similarity(vec)
            label_score = get_score(name, kdrama, get_indices(), sim) * label_weights[label]
            # print(label_score)
            similarity_data[label].append(label_score)
    
    return similarity_data

def get_top_rec_kdrama(name):
    """reorders the top recommended kdramas and converts to a dataframe"""
    data = create_similarity_data(name)
    new_df = pd.DataFrame(data)
    new_df['score'] = new_df.sum(axis=1, numeric_only=True)
    new_df = new_df.sort_values("score", ascending=False)
    print(new_df)

get_top_rec_kdrama("Move to Heaven")
=======
    kdrama_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return pd.concat([kdramas_df['title'].iloc[kdrama_indices], similarity_scores.iloc[kdrama_indices]], axis = 1)

get_recommended_kdramas(1, cosine_sim, df)
search_kdrama("Move", indices)
>>>>>>> beac7f0646d462dbf85aa5b2b152214c58812699
