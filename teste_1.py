import gi,requests,json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from datetime import datetime as dt
import matplotlib.pyplot as plt

windows = Gtk.Window(title="Hello World")
label=Gtk.Label('Temperatura')
belemb=Gtk.Button('Belém,Pa')
nyb=Gtk.Button('New York,Ny')
londonb=Gtk.Button('City of london,London')
vbox=Gtk.VBox()
hbox=Gtk.HBox()

windows.add(vbox)

vbox.add(label)
vbox.add(hbox)

hbox.add(belemb)
hbox.add(nyb)
hbox.add(londonb)
global varib
varib=1
variny=1
varil=1
def tempb(widget):
    global tempbl,varib
    tempbl=Gtk.Window(title='Weather Belém')
    varib=0
    print('ver')
    print(varib)
    trys=0
    while varib==0:
        print('what')
        requisicao=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Belém&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
        tempo=json.loads(requisicao.text)
        reqt=((tempo['weather'][0]['main']))
        atl=Gtk.Button('atualize')
        print(reqt)
        vbox1=Gtk.VBox()
        tempbl.add(vbox1)
        tempbl.add(vbox1)
        lblreqt=Gtk.Label(reqt)
        vbox1.add(lblreqt)
        vbox1.add(atl)
        tempbl.set_default_size(640,480)
        tempbl.show_all()
        varib=1
        print("funcionalop")
    def butb(widget):
        global varib
        varib=0

    atl.connect("clicked",butb)


def tempny(widget):
    global tempnyl,variny
    tempnyl=Gtk.Window(title='Weather New York')
    variny=0
    print('ver')
    print(variny)
    while variny==0:
        requisicao2=requests.get('http://api.openweathermap.org/data/2.5/weather?q=New York&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
        tempo2=json.loads(requisicao2.text)
        reqt2=(tempo2['weather'][0]['main'])
        atl2=Gtk.Button("atualize")
        print(reqt2)
        vbox2=Gtk.VBox()
        tempnyl.add(vbox2)
        tempnyl.add(vbox2)
        lblreqt2=Gtk.Label(reqt2)
        vbox2.add(lblreqt2)
        vbox2.add(atl2)
        tempnyl.set_default_size(640,480)
        tempnyl.show_all()
        variny=1
        print("funcionalop")
    def butny(widget):
        global varib
        varib=0
    atl2.connect("clicked",butny)


def templ(widget):
    global templl,varil
    templl=Gtk.Window(title='Weather City Of London')
    varil=0
    print('ver')
    print(varil)
    while varil==0:
        requisicao3=requests.get('http://api.openweathermap.org/data/2.5/weather?q=City of London&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
        tempo3=json.loads(requisicao3.text)
        reqt3=(tempo3['weather'][0]['main'])
        atl3=Gtk.Button("atualize")
        print(reqt3)
        vbox3=Gtk.VBox()
        templl.add(vbox3)
        templl.add(vbox3)
        lblreqt3=Gtk.Label(reqt3)
        vbox3.add(lblreqt3)
        vbox3.add(atl3)
        templl.set_default_size(640,480)
        templl.show_all()
        varil=1
        print("funcionalop")
    def butl(widget):
        global varib
        varib=0
    atl3.connect("clicked",butl)




belemb.connect("clicked",tempb)
nyb.connect("clicked",tempny)
londonb.connect("clicked",templ)

windows.show_all()
windows.connect("destroy", Gtk.main_quit)
Gtk.main()
