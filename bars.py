import config, requests, json
from datetime import datetime 

# Grabbing data from csv file
holdings = open('data/qqq.csv').readlines()

# Isolating stock tickers from holdings
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]

# Convert to comma-separated list
symbols = ','.join(symbols)

#print(symbols)

# Use alpaca api to retrieve stock data with symbols list
days_bar_url = "{}/day?symbols={}&limit=1000".format(config.BARS_URL, symbols)

r = requests.get(days_bar_url, headers=config.HEADERS)

data = r.json()

#print(json.dumps(r.json(), indent=4))

for symbol in data:
    filename = 'data/ohlc/{}.txt'.format(symbol)
    f = open(filename, 'w+')
    f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
    #print(data[symbol])

    for bar in data[symbol]:
        t = datetime.fromtimestamp(bar['t'])
        day = t.strftime('%Y-%m-%d')
        
        line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
        f.write(line)