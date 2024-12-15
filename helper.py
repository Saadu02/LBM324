import operator


class TodoItem:
    def __init__(self, title, date):
        self.title = title
        self.date = date


# Liste für ToDo-Items
items = []


def add(title, date):
    items.append(TodoItem(title, date))
    items.sort(key=operator.attrgetter("date"))
