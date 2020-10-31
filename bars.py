import config, requests, json

minute_bars_url = config.BARS_URL + "/5Min?symbols=MSFT&limit=1000"

days_bar_url = "{}/day?symbols={}&limit=1000".format(config.BARS_URL, 'AAPL,MSFT')

r = requests.get(days_bar_url, headers=config.HEADERS)

print(json.dumps(r.json(), indent=4))