from models.Budget import Budget

banana_budget = Budget()


def test_total_price_for_twenty_eight_day_month():
    number_of_days = 28
    response = banana_budget.get_price(number_of_days, "02-01-2018")
    assert response.json()["totalCost"] == "$2.50"


def test_total_price_for_thirty_day_month():
    number_of_days = 30
    response = banana_budget.get_price(number_of_days, "09-01-2018")
    assert response.json()["totalCost"] == "$2.50"


def test_total_price_for_thirty_one_day_month():
    number_of_days = 31
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.json()["totalCost"] == "$3.25"


def test_total_price_for_three_hundred_sixty_five_days():
    number_of_days = 365
    response = banana_budget.get_price(number_of_days, "01-01-2018")
    assert response.json()["totalCost"] == "$35.25"
