# Parse csv to html list
# file: patrons_sample.csv

import csv
html_output = ''
names = []

with open('patrons_sample.csv', 'r') as datafile:
    csv_reader = csv.reader(datafile)

    # we don't want the header row
    next(csv_reader)

    for line in csv_reader:
        if line[0] == "No Reward":
            continue
        names.append(f'{line[0]} {line[1]}')

# for name in names:
#     print(name)

html_output += f'<p>There are currently {len(names)} public contributors.</p>\n'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)