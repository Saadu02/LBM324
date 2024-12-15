import operator


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
