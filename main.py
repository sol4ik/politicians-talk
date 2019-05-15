from modules.convocation.convocation import Convocation
from modules.session.session import Session

import os
import re

convocations = list()
sessions = list()
politicians = list()

print('...')  # to track progress
for filename in os.listdir('docs/stenograms_lists'):
    if filename != "stenograms":
        path = 'docs/stenograms_lists/' + filename
        with open(path, 'r') as read_file:
            print('...parsing {}'.format(filename))  # to track progress
            # create Convocation object
            no_pattern = r'\d'  # get convocation number
            no = re.search(no_pattern, filename)
            no = int(no[0])

            new_conv = Convocation(no=no)
            convocations.append(new_conv)

            # go through the urls
            for line in read_file.readlines():
                url = line[:-1]

                new_session = Session()
                sessions.append(new_session)
                new_session.url = url

                new_session.set_date()

                date = new_session.session_date
                print('......parsing {} session'. format(date))  # to track progress

                new_session.parse_html()

                new_session.set_announcer()
                print('.........formatting {} session'.format(date))  # to track progress
                new_session.format()

                print('.........creating\\updating politicians'.format(date))  # to track progress
                pols = new_session.create_politicians()
                new_conv.politicians_list.extend(pols)

                # to_phrases
                #   phrase_analysis
                #   create Idea objs
                #   update Politician objs
                #   update Convocation objs
                # update Session obj

                # get all Politician objs
                # get all Convocation objs
                # final update
