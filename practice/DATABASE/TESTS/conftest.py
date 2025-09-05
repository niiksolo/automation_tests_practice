import os
import sqlite3
import pytest

@pytest.fixture
def db():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'BASE',  "Chinook_Sqlite.sqlite")
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Файл базы данных не найден по пути: {db_path}")
    conn = sqlite3.connect(db_path)
    yield conn
    conn.close()