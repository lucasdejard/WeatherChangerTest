import gi, requests, json
gi.require_version ( "Gtk" , "3.0" )
from gi.repository import Gtk
from datetime import datetime as dt
import matplotlib.pyplot as plt
import time
from agoravai import tempb,tempny,templ

windows = Gtk.Window( title="Hello World")
label=Gtk.Label('Weather')
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


belemb.connect("clicked",tempb)
nyb.connect("clicked",tempny)
londonb.connect("clicked",templ)


windows.show_all()
windows.connect("destroy", Gtk.main_quit)
Gtk.main()


