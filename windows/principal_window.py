import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.cells.film_cell import FilmCell

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

		# Only one button can be toggled at a time
		# def on_button_toggled(name):
		# 	print('Button '+name+' toggled')
		# 	# Untoggle all the buttons
		# 	films_button.set_active(False)
		# 	series_button.set_active(False)
		# 	music_button.set_active(False)
		# 	books_button.set_active(False)
		# 	games_button.set_active(False)

		# 	# Set to active state just the button pressed
		# 	if name == 'films': films_button.set_active(True)
		# 	if name == 'series': series_button.set_active(True)
		# 	if name == 'music': music_button.set_active(True)
		# 	if name == 'books': music_button.set_active(True)
		# 	if name == 'games': games_button.set_active(True)

		films_button = Gtk.ToggleButton(label="FILMS")
		films_button.set_active(True)
		# films_button.connect("toggled", on_button_toggled, "films")

		series_button = Gtk.ToggleButton(label="SERIES")
		# series_button.connect("toggled", on_button_toggled, "series")
		
		music_button = Gtk.ToggleButton(label="MUSIC")
		# music_button.connect("toggled", on_button_toggled, "music")
		
		books_button = Gtk.ToggleButton(label="BOOKS")
		# books_button.connect("toggled", on_button_toggled, "books")
		
		games_button = Gtk.ToggleButton(label="GAMES")
		# games_button.connect("toggled", on_button_toggled, "games")

		
		
		# STACK SWITCHER
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		stack.add(films_button)
		stack.add(series_button)
		stack.add(books_button)
		stack.add(music_button)
		stack.add(games_button)

		# Implementation of stack switcher.
		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		
		# SCROLLED
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.flowbox)
		

		for item in data_source:
			cell = FilmCell(item.get("title"),item.get("director"), item.get("year"), item.get("running_time"), item.get("synopsis"), item.get("cover_path"))
			self.flowbox.add(cell)

		# ADD ELEMENTS TO THE BOXES

		# This box will display a search bar and 3 buttons : 
		# - Delete button 
		# - Add button
		# - Filter button
		box_tools = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		box_tools.pack_start(search_bar, True, True, 0)
		#box_tools.pack_end(delete_button, True, True, 0)
		#box_tools.pack_end(add_button, True, True, 0)
		#box_tools.pack_end(filter_button, True, True, 0)

		# This box will display 5 buttons : 
		# - Films 
		# - Series 
		# - Music 
		# - Books 
		# - Games
		#box_sector = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		#box_sector.pack_start(games_button, True, True, 0)


		# ADD THE BOXES TO THE WINDOW

		box_principal = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 40)
		box_principal.pack_start(box_tools, False, False, 0)
		#box_principal.pack_start(box_sector, True, True, 0)
		box_principal.pack_start(stack_switcher, False, False, 5)
		box_principal.pack_start(scrolled, True, True, 0)
		self.add(box_principal)