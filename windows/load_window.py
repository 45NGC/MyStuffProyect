import json
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from windows.principal_window import PrincipalWindow


class LoadWindow(Gtk.Window):
	label = Gtk.Label("LOADING ...")
	spinner = Gtk.Spinner()
	box =  Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

	def __init__(self):
		super().__init__(title="")
		self.connect("destroy", Gtk.main_quit)
		
		# WINDOW PROPERTIES
		self.set_border_width(60)
		self.set_default_size(300, 150)
		self.set_resizable(False)
		self.set_position(Gtk.WindowPosition.CENTER)
        
		# WINDOW ELEMENTS
		self.spinner.props.active = True

		# ADD ELEMENTS TO THE WINDOW
		self.box.pack_start(self.label, False, False, 0)
		self.box.pack_start(self.spinner, False, False, 0)
		self.add(self.box)

		self.load_json()

	def load_json(self):

		data = 'data/data.json'

		with open(data) as elements:
			json_list = json.load(elements)

		# Lists to introduce the data of the json
		films_list = []
		series_list = []
		books_list = []
		music_list = []
		games_list = []
		memes_list = []

		for json_item in json_list:

			# FILMS
			if json_item.get("type") == "film":

				title = json_item.get("title")
				director = json_item.get("director")
				year = json_item.get("year")
				running_time = json_item.get("running_time")
				synopsis = json_item.get("synopsis")
				cover_path = json_item.get("cover_path")

				# Introduce the items in item_list
				films_list.append({"title":title, "director":director, "year":year, "running_time":running_time, "synopsis":synopsis, "cover_path":cover_path})
			
			# SERIES
			if json_item.get("type") == "series":
				print()

			# BOOKS
			if json_item.get("type") == "book":
				print()

			# MUSIC
			if json_item.get("type") == "music":
				print()

			# GAMES
			if json_item.get("type") == "game":
				print()

			# MEMES
			if json_item.get("type") == "meme":
				print()

			
		print(films_list[1])
		GLib.idle_add(self.start_principal_window, films_list)

    # Start the principal window
	def start_principal_window(self, films_list):
		win = PrincipalWindow(films_list)
		win.show_all()
		self.disconnect_by_func(Gtk.main_quit)
		self.close()