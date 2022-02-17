import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.cells.film_cell import FilmCell
from windows.cells.book_cell import BookCell

class PrincipalWindow(Gtk.Window):
	film_flowbox = Gtk.FlowBox()
	book_flowbox = Gtk.FlowBox()

	def __init__(self, films_data, books_data):
		super().__init__(title="Catalog")
		self.connect("destroy", Gtk.main_quit)

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(900, 900)
		self.set_position(Gtk.WindowPosition.CENTER)
		header = Gtk.HeaderBar(title="MyStuffProyect")
		#header.set_subtitle("2021 Catalog")
		header.props.show_close_button = True
		self.set_titlebar(header)


        ## WINDOW ELEMENTS ##

		# SEARCH BAR
		#search_bar = Gtk.SearchBar()

		# SCROLLED FILMS
		scrolled_films = Gtk.ScrolledWindow()
		scrolled_films.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled_films.add(self.film_flowbox)
		# SCROLLED SERIES
		# SCROLLED BOOKS
		scrolled_books = Gtk.ScrolledWindow()
		scrolled_books.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled_books.add(self.book_flowbox)
		# SCROLLED MUSIC
		# SCROLLED GAMES
		# SCROLLED MEMES

		# STACK SWITCHER
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		# Depending on the button of the stack switcher that we toggle the flowbox will display:

		# -Films
		for item in films_data:
			film_cell = FilmCell(item.get("title"),item.get("director"), item.get("year"), item.get("running_time"), item.get("synopsis"), item.get("cover_path"))
			self.film_flowbox.add(film_cell)
		
		stack.add_titled(scrolled_films, "check_films", "Films")

		# -Series

		# -Books
		for item in books_data:
			book_cell = BookCell(item.get("title"),item.get("author"), item.get("year"), item.get("book_type"), item.get("synopsis"), item.get("cover_path"))
			self.book_flowbox.add(book_cell)
		
		stack.add_titled(scrolled_books, "check_books", "Books")
		# -Music

		# -Games

		# -Memes

		# Implementation of STACK SWITCHER.
		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)

		# ADD ELEMENTS TO THE BOXES

		# TODO
		# This box will display a search bar and 3 buttons : 
		# - Delete button 
		# - Add button
		# - Filter button
		#box_tools = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		#box_tools.pack_start(search_bar, True, True, 0)
		#box_tools.pack_end(delete_button, True, True, 0)
		#box_tools.pack_end(add_button, True, True, 0)
		#box_tools.pack_end(filter_button, True, True, 0)

		# ADD THE BOXES TO THE WINDOW

		box_principal = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 40)
		#box_principal.pack_start(box_tools, False, False, 0)
		box_principal.pack_start(stack_switcher, False, False, 0)
		box_principal.pack_start(stack, True, True, 0)
		#box_principal.pack_start(scrolled_films, True, True, 0)
		self.add(box_principal)