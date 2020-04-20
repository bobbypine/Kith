import webbrowser
import json
import requests
import time
import urllib3

urllib3.disable_warnings()


def keysearch(keyword, size):
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
            print(items['title'], 'https://kith.com/products/{}'.format(items['handle']))
            itemurl = 'https://kith.com/products/{}'.format(items['handle'])
            #webbrowser.open('https://kith.com/products/{}'.format(items['handle']))
            print('Product Found at {} in {:.2f} Seconds'.format(time.strftime("%I:%M:%S"),time.time() - starttime))
            print('Adding to cart...')
            url2 = '{}.json'.format(itemurl)
            response2 = requests.get(url=url2, verify=False)
            data2 = json.loads(response2.content.decode('utf-8'))
            for sizes in data2['product']['variants']:
                if sizes['title'] == size:
                    carturl = 'https://kith.com/cart/{}:1'.format(sizes['id'])
                    webbrowser.open(carturl)



keyword = input('Enter Keyword(s): ').lower()
keylist = keyword.split(",")
size = input('Enter Size, Hit Enter When Ready: ').upper()
print()

for keyword in keylist:
    keysearch(keyword, size)

for _ in range(240):
    try:
        if not mylists:
            print('Product Not Found, Will Look Again...')
            time.sleep(0.25)
            keysearch(keyword, size)
    except Exception as e:
        print('{}: or Webstore Closed'.format(e))
print('Program Ended')
print('------------------------------------------------------------------------------------------------------------')
