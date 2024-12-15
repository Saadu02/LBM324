import operator
import csv
from io import StringIO


class TodoItem:
    def __init__(self, title, date, category=None):
        self.title = title
        self.date = date
        self.category = category


# Liste für ToDo-Items
items = []


def add(title, date, category=None):
    items.append(TodoItem(title, date, category))
    items.sort(key=operator.attrgetter("date"))


def get_csv():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Title", "Date", "Category"])
    for item in items:
        writer.writerow([item.title, item.date, item.category])

    return output.getvalue()  # Hier außerhalb der Schleife
