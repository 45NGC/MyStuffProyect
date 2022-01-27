import json
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from principal_window import PrincipalWindow
from data import films

class LoadWindow(Gtk.Window):
	label = Gtk.Label("Cargando elementos...")
	spinner = Gtk.Spinner()
	box =  Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

	def __init__(self):
		super().__init__(title="")
		self.connect("destroy", Gtk.main_quit)
		
		# WINDOW PROPERTIES
		self.set_border_width(60)
		self.set_default_size(300, 150)
		self.set_resizable(False)
        
		# WINDOW ELEMENTS
		self.spinner.props.active = True
		self.set_position(Gtk.WindowPosition.CENTER)

		# ADD ELEMENTS TO THE WINDOW
		self.box.pack_start(self.label, False, False, 0)
		self.box.pack_start(self.spinner, False, False, 0)
		self.add(self.box)
		self.load_jason()

	def load_jason(self):
		json_list = films.json()

		# List to introduce the data of the json
		item_list = []

		for json_item in json_list:

			# Get title, description and image of the film
			title = json_item.get("title")
			description = json_item.get("description")
			cover = json_item.get("cover")


			# Introduce the items in item_list
			item_list.append({"title":title, "description":description, "cover":cover})

		GLib.idle_add(self.start_principal_window, item_list)

    # Start the principal window
	def start_principal_window(self, loaded_items_list):
		win = PrincipalWindow(loaded_items_list)
		win.show_all()
		self.disconnect_by_func(Gtk.main_quit)
		self.close()