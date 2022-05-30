from employee import Employee

TestEmployee = Employee('Big', 'Smoke', 320)


def test_email():
    assert TestEmployee.email == 'Big.Smoke@email.com'
    assert TestEmployee.email != 'Big@email.com'


def test_fullname():
    assert TestEmployee.fullname == 'Big Smoke'
    assert TestEmployee.fullname != 'BigSmoke'
    assert TestEmployee.fullname in 'Big Big Smoke Smoke Big'


def test_apply_raise():
    assert TestEmployee.pay == 320
    TestEmployee.apply_raise()
    assert TestEmployee.pay != 320


# IN PROGRESS -----------------------------------------------------------
# def test_monthly_schedule(requests_mock):
#     requests_mock.get(f"http://company.com/{TestEmployee.last}")
#     assert TestEmployee.monthly_schedule()
#     assert TestEmployee.monthly_schedule().status_code == 200
