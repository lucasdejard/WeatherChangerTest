import gi, requests, json
gi.require_version ( "Gtk" , "3.0" )
from gi.repository import Gtk
from datetime import datetime as dt
import matplotlib.pyplot as plt
import time
from agoravai import tempb,tempny,templ
# I had a problem in the API(climatempo) because it only works in Brazilian countrys and a i did not know about it kkkkk
# So i changed all the foreign cities

windows = Gtk.Window( title="Weather Cities")
label=Gtk.Label('Weather')
belemb=Gtk.Button('Belém,Pa')
nyb=Gtk.Button('São Paulo,Sp')
londonb=Gtk.Button('Rio de Janeiro,Rj')

vbox=Gtk.VBox()
hbox=Gtk.HBox()

windows.add(vbox)

vbox.add(label)
vbox.add(hbox)

hbox.add(belemb)
hbox.add(nyb)
hbox.add(londonb)


belemb.connect("clicked",tempb)
nyb.connect("clicked",tempny)
londonb.connect("clicked",templ)


windows.show_all()
windows.connect("destroy", Gtk.main_quit)
Gtk.main()


