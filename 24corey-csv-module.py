# csv module
import csv

with open('random_contacts.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # next(csv_reader) # skip the header row
    with open('new_contacts.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv, delimiter='\t')

        for line in csv_reader:
            print(line[2])
            csv_writer.writerow(line)

# DictReader and DictWriter
with open('random_contacts.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    with open('latest_contacts.csv', 'w') as new_csv:
        fieldnames = ['first_name', 'email']
        csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames, delimiter='-')

        csv_writer.writeheader() # write the header row

        for line in csv_reader:
            print(line['email'])
            del line['last_name'] # remove the last_name key-value pair
            csv_writer.writerow(line)
