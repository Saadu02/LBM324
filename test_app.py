import pytest
from app import app, db, Todo

# Test-Setup und -Teardown
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.sqlite'  # Verwende eine separate Test-Datenbank
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Erstelle alle Tabellen in der Test-Datenbank
        yield client
        with app.app_context():
            db.drop_all()  # Lösche die Test-Datenbank nach dem Test

# Test: Hinzufügen einer neuen Aufgabe
def test_add_todo(client):
    response = client.post('/add', data={'title': 'Test Todo'})
    assert response.status_code == 302  # 302 bedeutet, dass eine Weiterleitung erfolgt
    todo = Todo.query.first()  # Holen Sie sich das erste Todo-Element
    assert todo.title == 'Test Todo'
    assert todo.complete is False  # Die Aufgabe sollte nicht abgeschlossen sein

# Test: Aktualisieren einer Aufgabe
def test_update_todo(client):
    with app.app_context():
        # Erstelle ein Todo und speichere es
        todo = Todo(title='Test Todo', complete=False)
        db.session.add(todo)
        db.session.commit()

        # Stelle sicher, dass die Instanz aktualisiert wird
        db.session.refresh(todo)

        # Teste die Update-Route
        response = client.get(f'/update/{todo.id}')
        if response.status_code == 302:
            response = client.get(response.headers['Location'])
        assert response.status_code == 200


# Test: Löschen einer Aufgabe
def test_delete_todo(client):
    with app.app_context():
        # Erstelle ein Todo und speichere es
        todo = Todo(title='Test Todo', complete=False)
        db.session.add(todo)
        db.session.commit()

        # Stelle sicher, dass die Instanz aktualisiert wird
        db.session.refresh(todo)

        # Teste die Delete-Route
        response = client.get(f'/delete/{todo.id}')
        if response.status_code == 302:
            response = client.get(response.headers['Location'])  # Folge der Weiterleitung
        assert response.status_code == 200