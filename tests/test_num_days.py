from models.Budget import Budget

banana_budget = Budget()
status_code_bad_request = 400
status_msg = "Invalid numberOfDays"


def test_negative_number_of_days():
    number_of_days = -1
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_zero_number_of_days():
    number_of_days = 0
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_non_integer_number_of_days():
    number_of_days = 1.479963
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg


def test_extremely_large_number_of_days():
    number_of_days = 2147483647
    response = banana_budget.get_price(number_of_days, "01-01-2018")
    assert response.status_code == status_code_bad_request
    assert response.json()["error"] == status_msg
