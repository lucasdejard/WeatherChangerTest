#section for get the next 24h temperature
# I had a problem in the API(climatempo) because it only works in Brazilian countrys and a i did not know about it kkkkk
# So i changed all the foreign cities
def Bel(self):
    import requests,json
    from datetime import datetime as dt
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    requisicao=requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/7704/hours/72?token=89dbc4c2ae16bdd7d8211c678c4bb3e1')
    print(requisicao)
    now=dt.now()
    ho=now.hour
    tempo=json.loads(requisicao.text)
    x=ho
    space=[]
    y=0
    while (x<(ho+24)):
        space.append((tempo['data'][y]['temperature']['temperature']))
        y=y+1
        x=x+1
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],space)
    plt.title('Weather Belém')
    plt.ylabel('Weather ºc')
    plt.xlabel('Next 24 Hours')
    plt.show()
    # API KEY:  89dbc4c2ae16bdd7d8211c678c4bb3e1


def NY(self):
    import requests,json
    from datetime import datetime as dt
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    requisicao=requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/hours/72?token=89dbc4c2ae16bdd7d8211c678c4bb3e1')
    print(requisicao)
    now=dt.now()
    ho=now.hour
    tempo=json.loads(requisicao.text)
    x=ho
    space=[]
    y=0
    while (x<(ho+24)):
        space.append((tempo['data'][y]['temperature']['temperature']))
        y=y+1
        x=x+1
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],space)
    plt.title('Weather São Paulo')
    plt.ylabel('Weather ºc')
    plt.xlabel('Next 24 Hours')
    plt.show()

def Lond(self):
    import requests,json
    from datetime import datetime as dt
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    requisicao=requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/5959/hours/72?token=89dbc4c2ae16bdd7d8211c678c4bb3e1')
    print(requisicao)
    now=dt.now()
    ho=now.hour
    tempo=json.loads(requisicao.text)
    x=ho
    space=[]
    y=0
    while (x<(ho+24)):
        space.append((tempo['data'][y]['temperature']['temperature']))
        y=y+1
        x=x+1
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],space)
    plt.title('Weather Rio de Janeiro')
    plt.ylabel('Weather ºc')
    plt.xlabel('Next 24 Hours')
    plt.show()
