import helper


def test_sort():
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    for todo in todos:
        helper.add(todo[0], todo[1])

    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date


def test_add_with_category():
    helper.items.clear()  # Leeren Sie die Liste vor dem Test
    helper.add("Universum debuggen", "2023-09-06", "Wissenschaft")
    helper.add("Sinn des Lebens entdecken", "2023-09-01", "Philosophie")

    assert helper.items[0].category == "Philosophie"
    assert helper.items[1].category == "Wissenschaft"
