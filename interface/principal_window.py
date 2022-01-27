import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PrincipalWindow(Gtk.Window):
	flowbox = Gtk.FlowBox()

	def __init__(self, data_source):
		super().__init__(title="Catalog")
		self.connect("destroy", Gtk.main_quit)