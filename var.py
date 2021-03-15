
from dryscrape.session import Session
from dryscrape.mixins import WaitTimeoutError

from bs4 import BeautifulSoup


def new_session():
    session = Session()
    session.set_attribute('auto_load_images', False)
    session.set_header('User-Agent', 'User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0')
    return session


def session_reset(session):
    return session.reset()


def session_visit(session, url, check):
    session.visit(url)
    print('=' * 200)
    # ensure that the market table is visible first
    if check:
        try:
            print('=' * 200)
            session.wait_for(lambda: session.at_xpath(
                '//*[@id="landing-page-app"]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]/span', timeout=10))

        except WaitTimeoutError:
            print('=' * 200)
            pass
    body = session.body()
    # session_reset(session)
    return body


SESSION = new_session()
URL = 'https://leetcode.com/'
CHECK = True

BODY = session_visit(SESSION, URL, CHECK)
print(BODY)
soup = BeautifulSoup(BODY, 'lxml')
SESSION.render('screenshot2.png')

RESULT = soup.find('div', {'id': 'answer-45824047'})

# print(RESULT)
