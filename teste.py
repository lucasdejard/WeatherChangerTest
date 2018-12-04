import gi,requests,json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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

def tempb(widget):
    tempbl=Gtk.Window(title='Belém')
    requisicao=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Belém&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo=json.loads(requisicao.text)
    reqt=(float(tempo['main']['temp'])-273.15)
    print(reqt)
    vbox1=Gtk.VBox()
    tempbl.add(vbox1)
    lblreqt=Gtk.Label(str(reqt)+'ºc')
    vbox1.add(lblreqt)
    tempbl.set_default_size(640,480)
    tempbl.show_all()
    print("funciona")

def tempny(widget):
    tempnyl=Gtk.Window(title='New York')
    requisicao2=requests.get('http://api.openweathermap.org/data/2.5/weather?q=New York&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo2=json.loads(requisicao2.text)
    reqt2=(float(tempo2['main']['temp'])-273.15)
    print(reqt2)
    vbox2=Gtk.VBox()
    tempnyl.add(vbox2)
    lblreqt2=Gtk.Label(str(reqt2)+'ºc')
    vbox2.add(lblreqt2)
    tempnyl.set_default_size(640,480)
    tempnyl.show_all()
    print("funciona")

def templ(widget):
    templ=Gtk.Window(title='Weather City Of London')
    requisicao3=requests.get('http://api.openweathermap.org/data/2.5/weather?q=City of London&appid=a5d84c2b0dbdc187d1521773a2bd3a22')
    tempo3=json.loads(requisicao3.text)
    reqt3=(float(tempo3['main']['temp'])-273.15)
    print(reqt3)
    vbox3=Gtk.VBox()
    templ.add(vbox3)
    lblreqt3=Gtk.Label(str(reqt3)+'ºc')
    vbox3.add(lblreqt3)
    templ.set_default_size(640,480)
    templ.show_all()
    print("funciona")

belemb.connect("clicked",tempb)
nyb.connect("clicked",tempny)
londonb.connect("clicked",templ)

windows.show_all()
windows.connect("destroy", Gtk.main_quit)
Gtk.main()
