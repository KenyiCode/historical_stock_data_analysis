import config, requests, json

# Grabbing data from csv file
holdings = open('data/qqq.csv').readlines()

# Isolating stock tickers from holdings
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]

# Convert to comma-separated list
symbols = ','.join(symbols)

print(symbols)

# Use alpaca api to retrieve stock data with symbols list
days_bar_url = "{}/day?symbols={}&limit=1000".format(config.BARS_URL, symbols)

r = requests.get(days_bar_url, headers=config.HEADERS)

print(json.dumps(r.json(), indent=4))