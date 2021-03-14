# module for get link (address line) from browsers

# TODO how install tKinter
import pyautogui as pag
import pyperclip

import os

import urllib.request
import requests
# TODO new project
# TODO import dryscrape

from bs4 import BeautifulSoup

# def get_url_browser:

start_location = pag.locateOnScreen('img/chrome.png')
print(start_location)
if start_location is None:
    exit()
start_point = pag.center(start_location)
print(start_point)
x, y = start_point
print(x, y)
x += 30
print(x, y)
pag.click(x, y)

pag.hotkey('ctrl', 'c')

url = pyperclip.paste()
print(url)


# req = urllib.request.Request(
#     url,
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     }
# )

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
# html = urllib.request.urlopen(req).read()

response = requests.get(url, headers=headers)
print(response.text)

# soup = BeautifulSoup(html, 'lxml').text
# print(soup)