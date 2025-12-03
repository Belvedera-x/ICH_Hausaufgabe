from Hausaufgabe.HA_7.employee_api import EmployeeApi


def test_create_employee_increases_count():

    base_url = "http://5.101.50.27:8000"
    api = EmployeeApi(base_url)
    res = api.create_employee("Oleg")
    assert res["message"] == "employee успешно создан"
    print(res)

