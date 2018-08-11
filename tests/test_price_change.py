from models.Budget import Budget

banana_budget = Budget()
number_of_days = 1
status_code_ok = 200


def test_price_for_day_one_current_month():
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.05"


def test_price_for_day_seven_current_month():
    response = banana_budget.get_price(number_of_days, "08-07-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.05"


def test_price_for_day_eight_current_month():
    response = banana_budget.get_price(number_of_days, "08-08-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.10"


def test_price_for_day_fourteen_current_month():
    response = banana_budget.get_price(number_of_days, "08-14-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.10"


def test_price_for_day_fifteen_current_month():
    response = banana_budget.get_price(number_of_days, "08-15-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.15"


def test_price_for_day_twentyone_current_month():
    response = banana_budget.get_price(number_of_days, "08-21-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.15"


def test_price_for_day_twentytwo_current_month():
    response = banana_budget.get_price(number_of_days, "08-22-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.20"


def test_price_for_day_twentyeight_current_month():
    response = banana_budget.get_price(number_of_days, "08-28-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.20"


def test_price_for_day_twentynine_current_month():
    response = banana_budget.get_price(number_of_days, "08-29-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.25"


def test_price_for_day_thirtyone_current_month():
    response = banana_budget.get_price(number_of_days, "08-31-2018")
    assert response.status_code == status_code_ok
    assert response.json()["totalCost"] == "$0.25"
