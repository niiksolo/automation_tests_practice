
import requests
import pyodbc
from faker import Faker

fake = Faker()

class TestDbIntegration:

    API_URL = 'http://localhost:5000/user'
    connection_string = 'test_users.db'
    def setup_method(self):   # метод генерируем нового польз
        self.test_user = {
            'username':fake.name(),
            'email': fake.email()
        }
    def test_create_user(self):   #создаем
        response = requests.post (
            url=self.API_URL,
            json=self.test_user
        )
        assert response.status_code == 200

        connection = pyodbc.connect(self.connection_string) #заходим в базу
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?',\
                       (self.test_user['email']))
        user = cursor.fetchone()
        print(user)
        connection.close()

        assert user is not None
        assert user[1] == self.test_user['username']
        assert user[2] == self.test_user['email']