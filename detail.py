import json
import requests
from bs4 import BeautifulSoup


with open("valid_authors.json") as f:
    valid_authors = json.load(f)


def get_webpage(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def extract_story_matrix(page):
    stories = page.find_all('div', attrs={'class': 'z-list mystories'})
    returnable = []
    for story in stories:
        story_info = story.find('div', attrs={'class': 'z-padtop2 xgray'}).text
        print(story_info)
        matrix = {}
        matrix["ginny"] = "Ginny W." in story_info and "2012" in story_info
        matrix["hermione"] = "Hermione G." in story_info and "2012" in story_info
        returnable.append(matrix)
    print(returnable)
    return returnable


def story_matrix_valid(matrix):
    type_1 = matrix[0]["ginny"] and matrix[1]["hermione"]
    type_2 = matrix[0]["hermione"] and matrix[1]["ginny"]
    return type_1 or type_2


def save_data_as_json(data, file_name):
    with open('%s.json' % file_name, 'w') as f:
        json.dump(data, f, indent=4)


viable_authors = {}

for author, data in valid_authors.items():
    print(data["url"])
    author_page = get_webpage(data["url"])
    story_matrix = extract_story_matrix(author_page)
    valid = story_matrix_valid(story_matrix)
    if valid:
        viable_authors[author] = data["url"]
        save_data_as_json(viable_authors, "viable_authors")
