from models.Budget import Budget

banana_budget = Budget()
status_code_bad_request = 400
status_code_ok = 200
status_msg = "Invalid startDate"


def test_day_month_year_time_format():
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "31-08-2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_unexpected_separator_dot():
    # This works even though out of spec
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "08.01.2018")
    assert response.status_code == status_code_ok


def test_unexpected_separator_slash():
    # This works even though out of spec
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "08.01.2018")
    assert response.status_code == status_code_ok


def test_out_of_bounds_month():
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "13/01/2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_out_of_bounds_day():
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "08/32/2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_year_distant_past():
    # Year can't really go out of bounds like day and date can
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "01/01/0000")
    assert response.status_code == status_code_ok

def test_year_far_future():
    # Year can't really go out of bounds like day and date can
    number_of_days = 1
    response = banana_budget.get_price(number_of_days, "01/01/2050")
    assert response.status_code == status_code_ok
