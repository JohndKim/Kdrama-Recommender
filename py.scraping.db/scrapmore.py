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

screenwriter_label = "Screenwriter: "
director_label = "Director: "

# the info of each kdrama
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
    try:
        response = requests.get(link)
    except Exception:
        print(f"some error with : {link}")
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

    #sleep(1)

    return row

def add_all_kdata():
    """gets korean drama info from each link and adds it to an array of dictionaries
    """
    links = get_links()
    progress = 0
    total = len(links)

    for link in links:
        try:
            progress_bar(progress, total)

            soup = get_soup(link)
            kdata.append(get_row(link, get_data(soup), get_details(soup), get_stats(soup), soup))

            progress += 1
        except Exception:
            print(f"error with : {link}")

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    '''just a progress bar'''
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + " " * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")


def create_csv_file():
    """creates a csv file with all kdrama info
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['link', 'rank', 'title', 'country', 'description', 'ep', 'genres', 'keywords', 'aired', 'network',
        'duration', 'content_rating', 'score', 'num_scored_by', 'num_watcher', 'actors', 'screenwriter', 'director']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
        for row in kdata:
            try:
                writer.writerow(row)
            except Exception:
                print(f"error csv with : {row} ")
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

print(colorama.Fore.RED + "done!")
print(colorama.Fore.RESET)
    
