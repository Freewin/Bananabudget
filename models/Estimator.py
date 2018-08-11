import datetime

'''
​​​​Every day, Bob buys a banana from the same grocery store on his way to work.
At this grocery store, bananas are priced in a dynamic, yet predictable way:
the first 7 days of the month, bananas cost $0.05;
the second 7 days of the month, bananas cost $0.10;
the third 7 days of the month, bananas cost $0.15;
the fourth 7 days of the month, bananas cost $0.20;
and any remaining days of the month after that, bananas cost $0.25.
'''


class Estimator:

    def price_for_day(self, day, price):
        if (day >= 1 and day <= 7):
            return price * 1
        elif (day > 7 and day <= 14):
            return price * 2
        elif (day > 14 and day <= 21):
            return price * 3
        elif (day > 21 and day <= 28):
            return price * 4
        elif (day > 28 and day <= 31):
            return price * 5
        else:
            return -1  # don't know what to do if days is over 31

    def is_weekend(self, date_under_test):
        if date_under_test.weekday() == 5 or date_under_test.weekday() == 6:
            return True
        else:
            return False

    def get_estimate(self, input_date, num_days, starting_price):
        # TODO does not work for year estimate
        # TODO add currency formatting for output
        (month, day, year) = input_date.split("-")
        date = datetime.datetime(int(year), int(month), int(day))
        total = 0
        price = starting_price

        while num_days != 0:
            # datetime reference sat = 5, sun = 6
            if not self.is_weekend(date):
                total = total + self.price_for_day(num_days, price)

            num_days = num_days - 1
            date = date + datetime.timedelta(days=1)

        return total


em = Estimator()
print(em.get_estimate("08-01-2018", 1, 0.05))
print(em.get_estimate("08-01-2018", 31, 0.05))
print(em.get_estimate("02-01-2018", 28, 0.05))
