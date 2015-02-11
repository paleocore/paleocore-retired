import csv
from models import Site, Date

with open('D:/Users/mcpherro/PycharmProjects/Sites/sites.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[1]