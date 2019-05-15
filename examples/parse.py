from bs4 import BeautifulSoup
import requests

import re

import os


def stenogram_format(text):
    """
    Function for text formatting.
    """
    time_pattern = r'\d{2}:\d{2}:\d{2}'
    remark_pattern = r'\(.+\)'
    sten_text = ''
    prev = ''
    for line in text:
        if re.match(time_pattern, line):
            pass
        elif re.search(remark_pattern, line):
            pos = line.index('(')
            line1 = line[:pos]
            pos = line.index(')')
            line2 = line[pos + 1:]
            nline = line1 + line2

            sten_text = prev + nline + '\n'
            prev = sten_text
        else:
            sten_text = prev + line + '\n'
            prev = sten_text
    return sten_text


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

    start = time.time()
    write_files(8)
    end = time.time()
    print(end - start)
