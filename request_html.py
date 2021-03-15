from requests_html import HTMLSession, HTML
from bs4 import BeautifulSoup

sess = HTMLSession()
sess.headers = 'User-Agent', 'User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0'

response = sess.get('https://leetcode.com/problems/decode-xored-array/')

print(response.headers)

print(response.html.links)

response.html.render(timeout=10, sleep=10)

#print(response.html.find('A New Way to Learn'))
# a_hrefs = response.html.xpath('A New Way to Learn')

body = response.content
print(body)
# soup = BeautifulSoup(body, 'lxml')

# print(response.html.find('A New Way to Learn', first=True))

# print(soup.text)