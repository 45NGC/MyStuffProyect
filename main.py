import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from interface.load_window import LoadWindow

win=LoadWindow()
win.show_all()

Gtk.main()