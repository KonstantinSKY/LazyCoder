# module for get link (address line) from browsers

# TODO how install tKinter
import pyautogui as pag
import pyperclip

import time
import os

import urllib.request
import requests
import dryscrape
import dryscrape.driver.webkit
import dryscrape.mixins

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

sess = dryscrape.Session()
sess.set_header("User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0")
# we don't need images
sess.set_attribute('auto_load_images', False)
sess.set_timeout(100)
sess.visit(url)
print(sess.headers())
sess.render('screenshot.png')
#

# # waiting
sess.wait_for(lambda: sess.at_xpath('/html/body/div[5]'))
sess.render('screenshot2.png')

doc = sess.body()
print(doc)

soup = BeautifulSoup(doc, 'lxml')
#
# frame = sess.at_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]')
# # response = sess.body()
# # <a class="ant-dropdown-link ant-dropdown-trigger">
#
# print(frame['src'])
sess.render('screenshot3.png')
#
#
# # <a class="ant-dropdown-link ant-dropdown-trigger">'
# sess.render('screenshot2.png')
#
# # print(response)
# # soup = BeautifulSoup(sess.body(), 'lxml')
print(soup.text)
#
# #
# #
# # # req = urllib.request.Request(
# # #     url,
# # #     headers={
# # #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# # #     }
# # # )
# #
# # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
# # # html = urllib.request.urlopen(req).read()
# #
# # response = requests.get(url, headers=headers)
# # print(response.text)
# #
# # soup = BeautifulSoup(html, 'lxml').text
# # # print(soup)