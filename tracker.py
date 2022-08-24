import requests
import time

#global variables
api_key = 'ab8b052d-7e9e-4e88-9b0f-d94dc16404e8'
bot_token = '1802925243:AAFY4sBJ7YWVoll5cJJPniVoGUDMZZ7pCxs'
chat_id = '1708631573'
threshold = .20
time_interval = 5 * 60 #seconds

def get_dogecoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start':'1','limit':'5000','convert':'USD'}
    headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': api_key}

    #coinmarketcap api request
    response = requests.get(url,headers=headers)
    response_json = response.json()

#get price from json
    dogecoin_price = response_json['data'][5]
    return dogecoin_price['quote']['USD']['price']

#function to send telegram message
def send_message(chat_id,msg):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}'

#send the msg
    requests.get(url)

#main function
def main():
    price_list = []

#infinite loop
    while True:
        price = get_dogecoin_price()
        price_list.append(price)

#if price falls below threshold send emergency msg
        if price < threshold:
            send_message(chat_id=chat_id,msg=f'DogeCoin Price Drop Alert:{price}')

#send last 6 bitcoin prices
        if len(price_list) >= 6:
            send_message(chat_id=chat_id,msg=price_list)
            #empty price list
            price_list = []
#get price for every dash minutes
        time.sleep(time_interval)

#activate main() function
if __name__ == '__main__':
    main()