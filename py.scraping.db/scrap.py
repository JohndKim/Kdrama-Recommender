import requests
from bs4 import BeautifulSoup
import re
import csv
from time import sleep
import math
import colorama

url_completed = "https://mydramalist.com/search?adv=titles&ty=68&co=3&st=3&so=top&page=1"  # kdrama site url 161
url_ongoing = "https://mydramalist.com/search?adv=titles&ty=68&co=3&st=1&so=top&page=1" # 1
links = []  # links of all kdrama

"""Checks regex

if regex doesn't match, returns -1; else returns the page number + 1
"""


def check_regex(regex, page_num):
    if bool(re.search(regex, page_num)):
        new_page_num = int(page_num) + 1
        return str(new_page_num)
    return -1


def update_link(url):
    """Updates link to the next page url
    """
    
    # PN = page number
    three_digit_pin = url[-3:]
    regex_three_digit = "\\d{3}"
    two_digit_pin = url[-2:]
    regex_two_digit = "\\d{2}"
    one_digit_pin = url[-1:]
    regex_one_digit = "\\d{1}"

    if check_regex(regex_three_digit, three_digit_pin) != -1:
        return url[:-3] + check_regex(regex_three_digit, three_digit_pin)

    elif check_regex(regex_two_digit, two_digit_pin) != -1:
        return url[:-2] + check_regex(regex_two_digit, two_digit_pin)

    elif check_regex(regex_one_digit, one_digit_pin) != -1:
        return url[:-1] + check_regex(regex_one_digit, one_digit_pin)

    """add links to link list from this URL
    """


def add_links(url):
    response = requests.get(url)  # sends and get HTTP response
    
    soup = BeautifulSoup(response.text, "html.parser")

    kdrama_sites = soup.select(
        "div > div.col-xs-9.row-cell.content > h6 > a:nth-child(1)"
    )  # list of all items with this selector

    for site in kdrama_sites:
        #print(site)
        links.append("https://mydramalist.com" + site.get("href"))

    sleep(1) #just to make sure to not overflow with requests
    
    """Adds all links from the mydramalist to links list
    """


def add_all_links(url, progress, total):
    """_summary_

    Args:
        url (_type_): _description_
    """
    before_url = links[-1]
    add_links(url)
    after_url = links[-1]

    progress_bar(progress + 1, total)
    # last page
    if before_url == after_url:
        return
    
    add_all_links(update_link(url), progress + 1, total)




def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = ' ' * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

print("starting with ongoing:")


add_links(url_ongoing)


print(colorama.Fore.RED + "ongoing done!")
print(colorama.Fore.RESET + "moving on to completed:")

progress_bar(0, 1)
add_links(url_completed)
add_all_links(update_link(url_completed), 0, 161)

print(colorama.Fore.RED + "completed done!")
print(colorama.Fore.RESET + "moving on to creating csv file:")


filename = "csv\shows.csv"

# adds all links into a row "link"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["link"])
    for link in links:
        writer.writerow([link])
        
        

print(colorama.Fore.RED + "done!")
print(colorama.Fore.RESET)

