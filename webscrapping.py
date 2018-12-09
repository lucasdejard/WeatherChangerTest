#section for get the next 24h temperature

def Bel(widget):
    import requests,json
    from datetime import datetime as dt
    gi.require_version ( "Gtk" , "3.0" )
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
    gi.require_version ( "Gtk" , "3.0" )
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
    #API KEY:    89dbc4c2ae16bdd7d8211c678c4bb3e1


def Lond(self):
    import requests,json
    from datetime import datetime as dt
    gi.require_version ( "Gtk" , "3.0" )
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
    #API KEY:    89dbc4c2ae16bdd7d8211c678c4bb3e1

# Section to atualize the Weather now


def Atb(self):
    import requests,json
    from datetime import datetime as dt
    gi.require_version ( "Gtk" , "3.0" )
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    print()


def Atny(self):
    import requests,json
    from datetime import datetime as dt
    gi.require_version ( "Gtk" , "3.0" )
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    print()


def Atl(self):
    import requests,json
    from datetime import datetime as dt
    gi.require_version ( "Gtk" , "3.0" )
    from gi.repository import Gtk
    import matplotlib.pyplot as plt
    import time

    print()
