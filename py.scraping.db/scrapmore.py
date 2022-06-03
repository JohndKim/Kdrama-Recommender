import csv
import re
from time import sleep

import requests
from bs4 import BeautifulSoup
from lxml import etree

filename = "csv\links.csv"

# details
titles = []
countries = []
episodes = []
aired = []
original_network = []
duration = []
content_rating = []

# stats
ranks = []
scores = []
scored_by = []
watchers = []

rank_num = 1

empty_string = ""
space_char = " "
num_separator = ","
drama_label = "Drama: "
country_label = "Country: "
episode_label = "Episodes: "
aired_label = "Aired: "
network_label = "Original Network: "
duration_label = "Duration: "
content_rating_label = "Content Rating: "

score_label = "Score: "
watchers_label = "Watchers: "

#loop through every show in r"csv\shows.csv"
def run():
    """reads every link from the csv file and scraps the details and statistics section
        into a new csv file
    """
    with open("csv\shows.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #scrap data from url
            data = get_data(row[0])
            #process data
            #write on csv
            pass
        print("done")
    
    
def get_data(link):
    """gets the details and statistics section from the link

    Args:
        link (string): link to mydramalist show
    """
    #scrap from mydramalist
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    
    #get details section
    details = soup.select(
        "div > div.container-fluid.title-container > div > div.col-lg-4.col-md-4 > div > div:nth-child(2) > div.box-body.light-b > ul > li"
        )
    process_details(details)

    #get statistics section
    statistics = soup.select(
        "div > div.container-fluid.title-container > div > div.col-lg-4.col-md-4 > div > div:nth-child(3) > div.box-body.light-b > ul > li"
    )
    for stat in statistics:
        print(stat.get("innerHTML"))
    
def replace_item(detail, label):
    """removes the label from the detail

    Args:
        detail (_type_): detail to remove label from
        label (_type_): label to remove

    Returns:
        _type_: detail
    """
    return detail.text.replace(label, empty_string)


# PROBLEM WITH THIS is that... the details are hard coded >.>;;; so that like if the details
# we get aren't exactly the same (e.g. we don't get exactly 8 details each kdrama, but 7)
# it screws up the whole thing so like i think im gonna needa loop each details with their label
# to find what detail is which T-T (i thought that they'd all be the same number of details but i guess not)
def process_details(details):
    """processes the details of the kdrama and adds it to their respective array

    Args:
        details (_type_): list of details to process
    """
    titles.append(replace_item(details[0], drama_label))
    countries.append(replace_item(details[1], country_label))
    episodes.append(replace_item(details[2], episode_label))
    aired.append(replace_item(details[3], aired_label))
    original_network.append(replace_item(details[5], network_label))
    duration.append(replace_item(details[6], duration_label))
    content_rating.append(replace_item(details[7], content_rating_label))

def process_stats(stats):
    """processes the stats of the kdrama and adds it to their respective array."

    Args:
        stats (_type_): list of stats to process
    """

    # e.g. 9.2 (scored by 23,610 users)
    unlabeled_scores = replace_item(stats[0], score_label)
    # 9.2 | (scored | by | 23,610 | users)
    scores_array = unlabeled_scores.split(space_char)
    
    ranks.append(rank_num)
    scores.append(scores_array[0])
    scored_by.append(scores_array[3].replace(num_separator, empty_string))
    watchers.append(replace_item(stats[3], watchers_label).replace(num_separator, empty_string))

    rank_num += 1

kdata = [] # 2d array

# uhhh we needa get the links over here :C
def create_data():
    for i in range(len(links)): # for every link, we get all this info
        row = [links[i], ranks[i], titles[i], countries[i], episodes[i], aired[i],
        original_network[i], duration[i], content_rating[i], scores[i], scored_by[i], watchers[i]]
        kdata.append(row) # add this info to kdata

create_data()


def create_csv_file():
    header = ["link", "rank", "title", "country", "episodes", "aired", "original_network", "duration", "content_rating", "score", "scored_by", "watchers"]

    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(header)

        writer.writerows(kdata) # basically add the entire 2d array in one go


get_data("https://mydramalist.com/49231-move-to-heaven")
