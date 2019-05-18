#!/bin/env ipython

from modules.convocation.convocation import Convocation
from modules.session.session import Session

from modules.session.exception.exception import ParseError

from modules.create_db.create_db import to_db

import os
import re

import time


def main():
    """
    Main function of the system.
    """
    convocations = list()
    sessions = list()
    politicians = set()

    print('> start')  # to track progress
    for filename in os.listdir('docs/stenograms_lists'):
        # if filename != "stenograms.list":
        if filename == "stenograms_skl8.list":
            path = 'docs/stenograms_lists/' + filename
            path = os.path.relpath(path)
            with open(path, 'r') as read_file:
                start = time.time()
                print('>  parsing {}...'.format(filename))  # to track progress
                # create Convocation object
                no_pattern = r'\d'  # get convocation number
                no = re.search(no_pattern, filename)
                no = int(no[0])

                new_conv = Convocation(no=no)
                convocations.append(new_conv)

                # go through the urls
                for line in read_file.readlines():
                    url = line[:-1]

                    new_session = Session(convocation=new_conv)
                    sessions.append(new_session)
                    new_session.url = url

                    new_session.set_date()

                    date = new_session.session_date
                    print('>   parsing {} session...'. format(date))  # to track progress

                    try:
                        new_session.parse_html()
                    except ParseError as err:
                        print(err)
                        continue

                    new_session.set_announcer()
                    print('>    formatting {} session...'.format(date))  # to track progress
                    new_session.format()

                    print('>    creating\\updating politicians...'.format(date))  # to track progress
                    pols = new_session.create_politicians()
                    for pol in pols:
                        pol.ideas_rating()
                        pol.ideas_timeline()
                    politicians = politicians.union(pols)

                    new_conv.politicians_list.extend(pols)

                    print('>    dividing into phrases and analysing...'.format(date))  # to track progress
                    new_session.to_phrases()

                    print('> {}'.format(time.time() - start))
            new_conv.ideas_rating()
    return convocations, politicians

# print(time.time() - start)
# politicians = list(politicians)
# for pol in politicians:
#     print(pol)
#     for idea in pol.ideas:
#         print(idea.name, '|', idea.session_date, '|', idea.context[:50])
#     print('--------')
