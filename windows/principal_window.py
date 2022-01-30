import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.film_cell import FilmCell

class PrincipalWindow(Gtk.Window):
	flowbox = Gtk.FlowBox()

	def __init__(self, data_source):
		super().__init__(title="Catalog")
		self.connect("destroy", Gtk.main_quit)

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(350, 600)
		self.set_position(Gtk.WindowPosition.CENTER)

        # WINDOW ELEMENTS
		
		#vbox = Gtk.VBox(False, 2)
		#vbox.pack_start(False, False, 0)

		header = Gtk.HeaderBar(title="Films")
		header.set_subtitle("2021 Catalog")
		header.props.show_close_button = True

		self.set_titlebar(header)

		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.flowbox)
		

		for item in data_source:
			cell = FilmCell(item.get("title"),item.get("director"), item.get("year"), item.get("running_time"), item.get("description"), item.get("cover"))
			self.flowbox.add(cell)

		# ADD ELEMENTS TO THE WINDOW
		box_principal = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		#box_principal.pack_start(vbox, False, False, 0)
		box_principal.pack_start(scrolled, True, True, 0)
		self.add(box_principal)