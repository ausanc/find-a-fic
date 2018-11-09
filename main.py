import requests
import json
import time
from bs4 import BeautifulSoup


def make_search_url(page_num):
    search_prefix = (
        "https://www.fanfiction.net/book/Harry-Potter/"
        "?&srt=2&lan=1&r=10&c1=11&p="
    )
    return search_prefix + str(page_num)


def make_author_url(author):
    author_prefix = "https://www.fanfiction.net"
    return author_prefix + author


def page_authors(page):
    authors = []
    story_posts = page.find_all('div', attrs={'class': 'z-list'})

    for story in story_posts:
        links = story.find_all('a')
        author_links = [a.get('href') for a in links if a.get('href').startswith("/u/")]
        author = author_links[0]
        authors.append(author)

    return authors


def count_stories(author):
    print("Getting stories for %s" % author)
    r = requests.get(make_author_url(author))
    author_page = BeautifulSoup(r.text, 'html.parser')
    time.sleep(0.5)
    story_count = author_page.find(id='l_st').find('span').text
    print("Found %s stories for user %s." % (story_count, author))
    return int(story_count)


def authors():
    encountered_authors = []
    for page_num in range(370, 500):
        print("Getting page %s" % page_num)
        r = requests.get(make_search_url(page_num))
        page = BeautifulSoup(r.text, 'html.parser')
        for author in page_authors(page):
            if author not in encountered_authors:
                encountered_authors.append(author)
                if count_stories(author) == 2:
                    yield author, page_num


def save_data_as_json(data, file_name):
    with open('%s.json' % file_name, 'w') as f:
        json.dump(data, f, indent=4)


valid_authors = {}
for author, page_num in authors():
    valid_authors[author] = {
        "url": make_author_url(author),
        "first_occurance": page_num
    }
    save_data_as_json(valid_authors, "valid_authors")
