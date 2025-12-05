import requests

class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user, password):
        """Получить токен авторизации"""
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["token"]



    def create_employee(self, name):
        """Создать employee"""
        employee = {
            "first_name": name,
            "last_name": "Ivanov",
            "middle_name": "Greg",
            "company_id": 1,
            "email": "ivanov@gmail.com",
            "phone": "0666565476544",
            "birth_date": "1980-01-01",
            "is_active": True
        }

        resp = requests.post(self.url + '/employee/create', json=employee)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return {
            "message": "employee успешно создан",
            "data": resp.json()
        }





