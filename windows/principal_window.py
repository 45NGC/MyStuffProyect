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
		self.set_default_size(900, 900)
		self.set_position(Gtk.WindowPosition.CENTER)

		# HEADER
		header = Gtk.HeaderBar(title="Films")
		header.set_subtitle("2021 Catalog")
		header.props.show_close_button = True
		self.set_titlebar(header)

        # WINDOW ELEMENTS

		# SEARCH BAR
		search_bar = Gtk.SearchBar()

		# BUTTONS

		# SCROLLED
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.flowbox)
		

		for item in data_source:
			cell = FilmCell(item.get("title"),item.get("director"), item.get("year"), item.get("running_time"), item.get("synopsis"), item.get("cover_path"))
			self.flowbox.add(cell)

		# ADD ELEMENTS TO THE WINDOW

		# This box will display a search bar and 3 buttons : 
		# - Delete button 
		# - Add button
		# - Filter button
		box_tools = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		box_tools.pack_start(search_bar, True, True, 0)
		#box_tools.pack_end(delete_button, True, True, 0)
		#box_tools.pack_end(add_button, True, True, 0)
		#box_tools.pack_end(filter_button, True, True, 0)

		# This box will display 4 buttons : 
		# - Films 
		# - Series 
		# - Music 
		# - Books
		box_sector = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		#box_tools.pack_start(films_button, True, True, 0)
		#box_tools.pack_start(series_button, True, True, 0)
		#box_tools.pack_start(books_button, True, True, 0)
		#box_tools.pack_start(music_button, True, True, 0)

		box_principal = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		box_principal.pack_start(box_tools, True, True, 0)
		box_principal.pack_start(scrolled, True, True, 0)
		self.add(box_principal)