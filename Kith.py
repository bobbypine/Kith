import webbrowser
import json
import requests
import time
import urllib3
import logging

urllib3.disable_warnings()


def keysearch(keyword, size):
    logging.basicConfig(level=logging.INFO, filename='Kith_Log.log', filemode='w',
                        format = " %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p ")
    starttime = time.time()
    url = 'https://www.kith.com/products.json'
    response = requests.get(url=url, verify=False)
    data = json.loads(response.content.decode('utf-8'))
    mylist = []
    global mylists
    mylists = mylist
    for items in data['products']:
        if keyword in items['title'].lower():
            mylist.append(items['title'])
            product = items['title']
            print(items['title'], 'https://kith.com/products/{}'.format(items['handle']))
            itemurl = 'https://kith.com/products/{}'.format(items['handle'])
            #webbrowser.open('https://kith.com/products/{}'.format(items['handle']))
            print('Product Found at {} in {:.2f} Seconds'.format(time.strftime("%I:%M:%S"),time.time() - starttime))
            print('Generating Cart Link...')
            #print('Taking you to queue...')
            url2 = '{}.json'.format(itemurl)
            response2 = requests.get(url=url2, verify=False)
            data2 = json.loads(response2.content.decode('utf-8'))
            for sizes in data2['product']['variants']:
                if sizes['title'] == size:
                    carturl = 'https://kith.com/cart/add?id={}'.format(sizes['id'])
                    logging.info(f'Cart URL for {product}: {carturl}')
                    print('Cart Link: {}'.format(carturl))
                    webbrowser.open(carturl)


keyword = input('Enter Keyword(s): ').lower()
keylist = keyword.split(",")
size = input('Enter Size, Hit Enter When Ready: ')
if size.isnumeric() is False:
    size = size.upper()
print()

for keyword in keylist:
    keysearch(keyword, size)

for _ in range(600):
    try:
        if not mylists:
            print('Product Not Found, Will Look Again...')
            time.sleep(0.25)
            keysearch(keyword, size)
    except Exception as e:
        print('{}: or Webstore Closed'.format(e))
print('Program Ended')
print('------------------------------------------------------------------------------------------------------------')
