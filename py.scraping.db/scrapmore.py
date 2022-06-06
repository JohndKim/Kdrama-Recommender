import csv
import re
from time import sleep

import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import copy
import pandas as pd
import colorama

filename = "csv\links.csv"

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

<<<<<<< HEAD
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

def get_details(details):
    for detail in details:
        if (detail):
            pass


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


# an array OF array with dictionaries
=======
screenwriter_label = "Screenwriter: "
director_label = "Director: "

# the info of each kdrama
>>>>>>> 9121047af7cae0677e4f341fdf56823507cdb43c
dict_row = {
    "link": "N/A",
    "rank": "N/A",
    "title": "N/A",
    "country": "N/A",
    "description": "N/A",
    "ep": "N/A",
    "genres": "N/A",
    "keywords": "N/A",
    "aired": "N/A",
    "network": "N/A",
    "duration": "N/A",
    "content_rating": "N/A",
    "score": "N/A",
    "num_scored_by": "N/A",
    "num_watcher": "N/A",
    "actors": "N/A",
    "screenwriter": "N/A",
    "director": "N/A"
}

# the array thats gonna store multiple dict_rows
kdata = []


def keys_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True

def get_soup(link):
    '''gets the soup thing from the link
    '''
    response = requests.get(link)
    return BeautifulSoup(response.text, "html.parser")

def get_data(soup):
    '''gets data of kdrama from the json file
    '''
    # this is the json file with kdrama info
    return json.loads(soup.find('script', type='application/ld+json').text)


def get_details(soup):
    '''gets details of kdrama from soup
    '''
    return soup.select(
        "div > div.container-fluid.title-container > div > div.col-lg-4.col-md-4 > div > div:nth-child(2) > div.box-body.light-b > ul > li"
        )

def get_stats(soup):
    '''gets stats of kdrama from soup
    '''
    return soup.select(
        "div > div.container-fluid.title-container > div > div.col-lg-4.col-md-4 > div > div:nth-child(3) > div.box-body.light-b > ul > li"
    )

def get_detail(details, label):
    '''gets a specific detail from details or stats or anything
    '''
    for detail in details:
        if re.match(label, detail.text):
            return detail.text.replace(label, empty_string)

def get_director(soup):
    '''gets director
    '''
    director = soup.select('#show-detailsxx > div.show-detailsxss > ul:nth-child(1) > li')
    return get_detail(director, director_label)

def get_screenwriter(soup):
    ''' gets screenwriter
    '''
    screenwriter = soup.select('#show-detailsxx > div.show-detailsxss > ul:nth-child(1) > li')
    return get_detail(screenwriter, screenwriter_label)

def get_row(link, data, details, stats, soup):
    '''fills in a row of kdrama info and returns it
    '''
    global rank_num

    row = copy.copy(dict_row)

    # link
    row['link'] = link
    
    # rank_num
    row['rank'] = rank_num
    rank_num += 1

    # title
    if 'name' in data: 
        row['title'] = data['name']

    # country
    if keys_exists(data, 'countryOfOrigin', 'name'):
        row['country'] = data['countryOfOrigin']['name']

    # description
    if 'description' in data:
        row['description'] = data['description']

    # episode
    row['ep'] = get_detail(details, episode_label)

    # genres
    if 'genre' in data:
        row['genres'] = data['genre']

    # keywords
    if 'keywords' in data:
        row['keywords'] = data['keywords']

    # aired
    if 'datePublished' in data:
        row['aired'] = data['datePublished']

    # network
    if keys_exists(data, 'publisher', 'name'):
        row['network'] = data['publisher']['name']

    # duration
    row['duration'] = get_detail(details, duration_label)

    # content_rating
    row['content_rating'] = get_detail(details, content_rating_label)

    # scores
    if keys_exists(data, 'aggregateRating', 'ratingValue'):
        row['score'] = data['aggregateRating']['ratingValue']

    # scored_by
    if keys_exists(data, 'aggregateRating', 'ratingCount'):
        row['num_scored_by'] = data['aggregateRating']['ratingCount']

    # watchers
    row['num_watcher'] = get_detail(stats, watchers_label)

    # actors
    if 'actor' in data:
        list_of_actors = data['actor']
        actor_list = []
        for act in list_of_actors:
            actor_list.append(act['name'])
        row['actors'] = actor_list

    # screenwriter
    row['screenwriter'] = get_screenwriter(soup)

    # director
    row['director'] = get_director(soup)

    sleep(1)

    return row

def add_all_kdata():
    """gets korean drama info from each link and adds it to an array of dictionaries
    """
    links = get_links()
    progress = 0
    total = len(links)

    for link in links:
        progress_bar(progress, total)

        soup = get_soup(link)
        kdata.append(get_row(link, get_data(soup), get_details(soup), get_stats(soup), soup))

        progress += 1

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    '''just a progress bar'''
    percent = 100 * (progress / float(total))
    bar = ' ' * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")


def create_csv_file():
    """creates a csv file with all kdrama info
    """
    with open(filename, 'w', newline='') as file:
        fieldnames = ['link', 'rank', 'title', 'country', 'description', 'ep', 'genres', 'keywords', 'aired', 'network',
        'duration', 'content_rating', 'score', 'num_scored_by', 'num_watcher', 'actors', 'screenwriter', 'director']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
<<<<<<< HEAD
get_json()
=======
        for row in kdata:
            writer.writerow(row)

def get_links():
    """gets all links from a csv containing the links

    Returns:
        _type_: list of links
    """
    file_link = "csv\shows.csv"
    data = pd.read_csv(file_link)
    return data['link'].tolist() # converts all links into a list

def run():
    """runs the scraping scripts and gets all kdrama info
    """
    add_all_kdata() # processes each link and gets all info on a kdrama and adds to kdata[]
    create_csv_file() # adds each element of kdata (all info on one kdrama) to the csv

run()
>>>>>>> 9121047af7cae0677e4f341fdf56823507cdb43c
