import copy

import pandas as pd

from rec_sys import get_titles, get_top

ktitles = get_titles()

k_recs = {
    "title": "N/A",
    "recommendations": "N/A",
    "similarity": "N/A",
}

# list of dictionaries
kdata = []

# for each title, get top 20 recommended kdrama + similarity score

def store_data():
    count = 0
    for title in ktitles:
        # 20 kdrama recs + their sim score
        if count == 5: break
        
        dicti = get_top(title)

        row = copy.copy(k_recs)
        
        row['title'] = title
        row['recommendations'] = dicti['titles']
        row["similarity"] = dicti['sim_score']

        kdata.append(row)
        count += 1

# store_data()
# print(kdata)

print(ktitles)
