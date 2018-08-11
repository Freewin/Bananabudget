import requests


class Budget:

    def get_price(self, number_of_days, start_date):
        url = "https://bananabudget.azurewebsites.net/"
        querystring = {"startDate": start_date, "numberOfDays": number_of_days}
        headers = {
            'Cache-Control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
