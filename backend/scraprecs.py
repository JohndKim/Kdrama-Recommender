import copy

import colorama
import pandas as pd

from rec_sys import fill_na, get_titles, get_top

ktitles = get_titles()
filename = 'csv\kdrama_data.csv'

k_recs = {
    "title": "N/A",
    "recommendations": "N/A",
    "similarity": "N/A",
}

# list of dictionaries
kdata = []



# for each title, get top 20 recommended kdrama + similarity score
def store_data():
    # for every kdrama, get their recs + sim scores

    progress = 0
    total = len(ktitles)

    for title in ktitles:
        progress_bar(progress, total)

        # 20 kdrama recs + their sim score        
        recs_score = get_top(title)

        row = copy.copy(k_recs)
        
        row['title'] = title
        row['recommendations'] = recs_score[0]
        row["similarity"] = recs_score[1]

        kdata.append(row)

        progress += 1

def merge_data():
    store_data()
    # dataframe with all recs + sim score
    rec_df = pd.DataFrame(kdata)
    
    # dataframe with link, title, rank, score of all kdrama
    df = pd.read_csv(filename)
    fill_na()
    df = df[['link', 'title', 'rank', 'score']]

    # merged dataframe of the two
    merged_df = pd.merge(df, rec_df)
    merged_df.to_csv('recs.csv', encoding='utf-8', index=False)

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    '''just a progress bar'''
    percent = 100 * (progress / float(total))
    bar = ' ' * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")


merge_data()

# print(ktitles)

# convert array of dic to df
# get columns from this df and add to the kdrama df




