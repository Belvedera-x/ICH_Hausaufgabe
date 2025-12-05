from QA_Auto.Hausaufgabe_7.employee_api import EmployeeApi

base_url = "https://restful-booker.herokuapp.com"
api = EmployeeApi(base_url)


def test_check_auth():
    api.get_token("admin", "password123")


def test_create_employee_increases_count():

    base_url = "http://5.101.50.27:8000"
    api = EmployeeApi(base_url)
    res = api.create_employee("Oleg")
    assert res["message"] == "employee успешно создан"
    print(res)

