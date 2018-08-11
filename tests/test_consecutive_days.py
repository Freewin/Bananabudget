from models.Budget import Budget

banana_budget = Budget()


def test_price_for_day_two_consecutive_days_at_price_tier_one():
    number_of_days = 2
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.json()["totalCost"] == "$0.10"


def test_price_for_day_three_consecutive_days_at_price_tier_one():
    number_of_days = 3
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.json()["totalCost"] == "$0.15"


def test_price_for_day_five_consecutive_days_at_price_tier_one():
    # tier 1 includes weekends so -2 days
    number_of_days = 5
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.json()["totalCost"] == "$0.15"


def test_price_for_day_seven_consecutive_days_at_price_tier_one():
    # 7 days is 5 buying days due to 2 days of weekend
    number_of_days = 7
    response = banana_budget.get_price(number_of_days, "08-01-2018")
    assert response.json()["totalCost"] == "$0.25"


def test_price_for_day_two_consecutive_days_at_price_tier_two():
    number_of_days = 2
    response = banana_budget.get_price(number_of_days, "08-08-2018")
    assert response.json()["totalCost"] == "$0.20"


def test_price_for_day_three_consecutive_days_at_price_tier_two():
    number_of_days = 3
    response = banana_budget.get_price(number_of_days, "08-08-2018")
    assert response.json()["totalCost"] == "$0.30"


def test_price_for_day_five_consecutive_days_at_price_tier_two():
    # includes weekends so -2 days
    number_of_days = 5
    response = banana_budget.get_price(number_of_days, "08-08-2018")
    assert response.json()["totalCost"] == "$0.30"


def test_price_for_day_seven_consecutive_days_at_price_tier_two():
    # 7 days is 5 buying days due to 2 days of weekend
    number_of_days = 7
    response = banana_budget.get_price(number_of_days, "08-08-2018")
    assert response.json()["totalCost"] == "$0.50"


def test_price_for_day_two_consecutive_days_at_price_tier_three():
    number_of_days = 2
    response = banana_budget.get_price(number_of_days, "08-15-2018")
    assert response.json()["totalCost"] == "$0.30"


def test_price_for_day_three_consecutive_days_at_price_tier_three():
    number_of_days = 3
    response = banana_budget.get_price(number_of_days, "08-15-2018")
    assert response.json()["totalCost"] == "$0.45"


def test_price_for_day_five_consecutive_days_at_price_tier_three():
    # includes weekends so -2 days
    number_of_days = 5
    response = banana_budget.get_price(number_of_days, "08-15-2018")
    assert response.json()["totalCost"] == "$0.45"


def test_price_for_day_seven_consecutive_days_at_price_tier_three():
    # 7 days is 5 buying days due to 2 days of weekend
    number_of_days = 7
    response = banana_budget.get_price(number_of_days, "08-15-2018")
    assert response.json()["totalCost"] == "$0.75"


def test_price_for_day_two_consecutive_days_at_price_tier_four():
    number_of_days = 2
    response = banana_budget.get_price(number_of_days, "08-22-2018")
    assert response.json()["totalCost"] == "$0.40"


def test_price_for_day_three_consecutive_days_at_price_tier_four():
    number_of_days = 3
    response = banana_budget.get_price(number_of_days, "08-22-2018")
    assert response.json()["totalCost"] == "$0.60"


def test_price_for_day_five_consecutive_days_at_price_tier_four():
    # includes weekends so -2 days
    number_of_days = 5
    response = banana_budget.get_price(number_of_days, "08-22-2018")
    assert response.json()["totalCost"] == "$0.60"


def test_price_for_day_seven_consecutive_days_at_price_tier_four():
    # 7 days is 5 buying days due to 2 days of weekend
    number_of_days = 7
    response = banana_budget.get_price(number_of_days, "08-22-2018")
    assert response.json()["totalCost"] == "$1.00"


def test_price_for_day_two_consecutive_days_at_price_tier_five():
    number_of_days = 2
    response = banana_budget.get_price(number_of_days, "08-29-2018")
    assert response.json()["totalCost"] == "$0.50"


def test_price_for_day_three_consecutive_days_at_price_tier_five():
    number_of_days = 3
    response = banana_budget.get_price(number_of_days, "08-29-2018")
    assert response.json()["totalCost"] == "$0.75"


