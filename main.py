from modules.convocation.convocation import Convocation
from modules.session.session import Session

import os
import re

convocations = list()

print('...')  # to track progress
for filename in os.listdir('docs/stenograms_lists'):
    if filename != "stenograms":
        with open(filename, 'r') as read_file:
            print('\tparsing {}...'.format(filename))  # to track progress
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
                new_session.url = url

                new_session.set_date()

                date = new_session.session_date
                print('\t\tworking on {} session...'. format(date))  # to track progress

                new_session.parse_html()
