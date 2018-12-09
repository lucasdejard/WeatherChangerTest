import gi,requests,json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from webscrapping import Bel,NY,Lond





def tempb(widget):
    global requisicao,tempo,reqt,tempbl,vbox1,hbox1,lblreqt,atl,bel24,x
    x=1
    tempbl=Gtk.Window(title='Weather Belém')
    requisicao=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Belém&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo=json.loads(requisicao.text)
    reqt=((tempo['weather'][0]['main']))
    bel24=Gtk.Button('Next 24h Temperature')
    atl=Gtk.Button('atualize')
    print(reqt)
    vbox1=Gtk.VBox()
    hbox1=Gtk.HBox()
    tempbl.add(vbox1)
    lblreqt=Gtk.Label(reqt)
    vbox1.add(lblreqt)
    vbox1.add(hbox1)
    hbox1.add(atl)
    hbox1.add(bel24)
    tempbl.set_default_size(640,480)
    tempbl.show_all()
    print("Belém Working")
    bel24.connect('clicked',Bel)
    atl.connect('clicked',Atb)


def Atb(self):
    global tempbl,requisicao,tempo,reqt,bel24,atl,vbox1,hbox1,lblreqt
    print(x)
    requisicao=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Belém&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo=json.loads(requisicao.text)
    reqt=((tempo['weather'][0]['main']))
    tempbl.remove(vbox1)
    bel24=Gtk.Button('work')
    atl=Gtk.Button('work')
    print(reqt)
    vbox1=Gtk.VBox()
    hbox1=Gtk.HBox()
    tempbl.add(vbox1)
    lblreqt=Gtk.Label(reqt)
    vbox1.add(lblreqt)
    vbox1.add(hbox1)
    hbox1.add(atl)
    hbox1.add(bel24)
    tempbl.set_default_size(640,480)
    tempbl.show_all()
    print("Belém Working")



def tempny(widget):
    tempnyl=Gtk.Window(title='Weather New York')
    requisicao2=requests.get('http://api.openweathermap.org/data/2.5/weather?q=New York&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo2=json.loads(requisicao2.text)
    reqt2=(tempo2['weather'][0]['main'])
    NY24=Gtk.Button("Next 24h Temperature")
    atl2=Gtk.Button('atualize')
    print(reqt2)
    vbox2=Gtk.VBox()
    hbox2=Gtk.HBox()
    tempnyl.add(vbox2)
    lblreqt2=Gtk.Label(reqt2)
    vbox2.add(lblreqt2)
    vbox2.add(hbox2)
    hbox2.add(atl2)
    hbox2.add(NY24)
    tempnyl.set_default_size(640,480)
    tempnyl.show_all()
    print("NY working")
    atl2.connect('clicked',Atny)
    NY24.connect('clicked',NY)


def Atny(self):

    print()


def templ(widget):
    templl=Gtk.Window(title='Weather City Of London')
    requisicao3=requests.get('http://api.openweathermap.org/data/2.5/weather?q=City of London&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo3=json.loads(requisicao3.text)
    reqt3=(tempo3['weather'][0]['main'])
    lond24=Gtk.Button("Next 24h Temperature")
    atl3=Gtk.Button('atualize')
    print(reqt3)
    vbox3=Gtk.VBox()
    hbox3=Gtk.HBox()
    templl.add(vbox3)
    lblreqt3=Gtk.Label(reqt3)
    vbox3.add(lblreqt3)
    vbox3.add(hbox3)
    hbox3.add(atl3)
    hbox3.add(lond24)
    templl.set_default_size(640,480)
    templl.show_all()
    print("London working")
    atl3.connect('clicked',Atl)
    lond24.connect('clicked',Lond)


def Atl(self):
    print()
