import webbrowser
import json
import requests
import time
import urllib3

urllib3.disable_warnings()


def keysearch(keyword):
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
            webbrowser.open('https://kith.com/products/{}'.format(items['handle']))
            print('Product Found at {} and Opened in {:.2f} Seconds'.format(time.strftime("%I:%M:%S"),time.time() - starttime))
            print()

keyword = input('Enter Keyword(s), Hit Enter When Ready:').lower()
keylist = keyword.split(",")
print()

for keyword in keylist:
    keysearch(keyword)

for _ in range(240):
    try:
        if not mylists:
            print('Product Not Found, Will Look Again...')
            time.sleep(0.25)
            keysearch(keyword)
    except Exception as e:
        print('{}: or Webstore Closed'.format(e))
print('Program Ended')
print('------------------------------------------------------------------------------------------------------------')
