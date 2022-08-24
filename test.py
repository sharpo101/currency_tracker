import requests
api_key = 'ab8b052d-7e9e-4e88-9b0f-d94dc16404e8'

def get_bitcoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start':'1','limit':'5000','convert':'USD'}
    headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': api_key}

    #coinmarketcap api request
    response = requests.get(url,headers=headers)
    response_json = response.json()

#get price from json
    bitcoin_price = response_json['data'][5]
    #return bitcoin_price['quote']['USD']['price']
    print(bitcoin_price)

get_bitcoin_price()
