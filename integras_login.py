import requests
from   bs4 import BeautifulSoup

import integras_scrapping_clients
import integras_scrapping

from datetime import datetime

url = 'https://wealth.emaplan.com/ema/SignIn?ema%2fberthelfisher%2fintegraspartners'
print(url)

loggerFile = open('append.txt', 'a') 
loggerFile.write('\nAccessed on ' + str(datetime.now()))

with requests.session() as s:
    s.headers['user-agent'] = 'Mozilla/5.0'
    s.headers['authority'] = 'wealth.emaplan.com'
    s.headers['path'] = '/ema/SignIn?ema%2fberthelfisher%2fintegraspartners'
    s.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    data = {}
    data['Username'] = "KeithJ2"
    data['Password'] = "Password13"

    r    = s.post(url, data = data)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html5lib')
        # print(soup.title.text)
        if soup.title.text == 'Home':
        	print("Logged In :)")
        	integras_scrapping_clients.getClients(authCookie = r.cookies['emaAuthentication'])
        	integras_scrapping.getReports(authCookie = r.cookies['emaAuthentication'], idUser = "5a4ab03d-7586-4630-9f00-006f5fc0fa2a")
        else: 
        	print("Not Logged In")
    else: print('NOT LOGGED IN')