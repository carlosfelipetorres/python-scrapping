import requests
import json

import dbconnection

def getClients(authCookie):

    url = 'https://wealth.emaplan.com/ema/api/Clients/Search'

    print(url, authCookie)

    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/5.0'
        s.headers['authority'] = 'wealth.emaplan.com'
        s.headers['path'] = '/ema/api/Clients/Search'

        cookies = {'emaAuthentication': authCookie}

        data = {}
        data['Affinity'] = "All"
        data['SortField'] = "LastNameFirst"
        data['SortDescending'] = "false"
        data['StartRecord'] = 1
        data['EndRecord'] = 200
        data['NumberOfRecords'] = 20

        r    = s.post(url, data = data, cookies = cookies)
        
        if r.status_code == 200:
            users = json.loads(r.content.json())
            dbconnection.insert_users_list(users)
        else: print('NOT LOGGED IN')

    