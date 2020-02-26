import requests
from   bs4 import BeautifulSoup


def getReports(authCookie, idUser):
    url = 'https://wealth.emaplan.com/ema/Advisor/Clients/' + idUser + '/Reports/View/CashFlowReport'
    print(url)
    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/5.0'
        s.headers['authority'] = 'wealth.emaplan.com'
        s.headers['path'] = '/ema/Advisor/Clients/' + idUser + '/Reports/View/CashFlowReport'

        cookies = {'emaAuthentication': authCookie}

        r    = s.get(url, cookies = cookies)
        soup = BeautifulSoup(r.content, 'html5lib')
        
        # print(r.content)
        target = 'ctl00$Content$PageContent_$ReportControl$ctl04$ctl01'
        argument = 'CashFlowWithdrawalsReport'
        # print(target)

        # unsupported CSS Selector 'input[name^=ctl00][value]'
        data = {}
        for tag in soup.select('input[name^=nobr]'):
            if tag.get('value'):
                key, value = tag['name'], tag['value']
                data[key] = value
        # data  = { tag['name']: tag['value'] 
        #               for tag in soup.select('input[name^=ctl00]') if tag.get('value') }
        state = { tag['name']: tag['value'] for tag in soup.select('input[name^=__]') }

        data.update(state)
        # col = soup.find_all('rptHdrCol')
        # print(col)
        # print("CONTENT ", r.content)
        # print(data)
        # print(state)

        data['__EVENTTARGET'] = target
        data['__EVENTARGUMENT'] = argument

        r    = s.post(url, data=data, cookies = cookies)
        soup = BeautifulSoup(r.content, 'html5lib')
        # print("-------",soup)
        # unsupported CSS Selector 'tr:not(.tr_header)'
        for table in soup.find_all('table', {'cellpadding':0}):
            print(" ------------- ",table)
            