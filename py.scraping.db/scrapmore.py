import requests
from bs4 import BeautifulSoup
import re
import csv
from time import sleep
from lxml import etree


filename = "csv\links.csv"

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
    
    #get statistics section
    statistics = soup.select(
        "div > div.container-fluid.title-container > div > div.col-lg-4.col-md-4 > div > div:nth-child(3) > div.box-body.light-b > ul > li"
    )
    for stat in statistics:
        print(stat.get("innerHTML"))
    

def process_details(details):
    pass

def process_stats(stats):
    pass

get_data("https://mydramalist.com/49231-move-to-heaven")