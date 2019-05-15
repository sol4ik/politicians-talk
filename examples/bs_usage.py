from bs4 import BeautifulSoup
import requests

import re

import os


def write_files(n):
    """
    n - номер скликання 1-8
    """
    sten_links = []

    cur_path = os.path.dirname(__file__)
    path = os.path.relpath('../docs/stenograms_lists/stenograms_skl' + str(n)+ '1.list', cur_path)

    with open(path, 'r') as links:
        for line in links.readlines():
            sten_links.append(line)

    for link in sten_links:
        pattern = r'\d{8}-?\d?'
        f_name = re.search(pattern, link)
        sten = open('../docs/stenograms/skl' + str(n) + '/stenogram_' + str(f_name.group(0)) + '.htm', mode='w')

        page_response = requests.get(link[:-1], timeout=1)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        text_content = []
        for i in range(0, len(page_content.find_all("p", attrs={"align": None}))):
            paragraphs = page_content.find_all("p", attrs={"align": None})[i].text
            text_content.append(paragraphs)

        # text_content = stenogram_format(text_content)
        sten.write('\n'.join(text_content))
        sten.close()


if __name__ == "__main__":
    import time

    write_files(8)
    end = time.time()
