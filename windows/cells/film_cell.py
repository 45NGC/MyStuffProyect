import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from windows.detail_windows.film_detail_window import FilmDetailWindow

class FilmCell(Gtk.EventBox):

	def __init__(self, title, director, year, running_time, synopsis, cover_path):
		super().__init__()
		self.title = title
		self.director = director
		self.year = year
		self.running_time = running_time
		self.synopsis = synopsis
		self.cover_path = cover_path

		# Use cover_path to create a Gtk.Image of the cover
		# COVER
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = cover_path, width=200, height=200, preserve_aspect_ratio=False)
		cover = Gtk.Image.new_from_pixbuf(pixbuf)

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		box.pack_start(Gtk.Label(label=title), False, False, 0)
		box.pack_start(cover, False, False, 0)
		self.add(box)

		# If the user presses the cell show film_detail_window
		self.connect("button-release-event", self.on_click_film)

		# Add 2 if conditionals, one for each button of the interface:
		#if the user toggles the mod option : self.connect("button-release-event", self.mod_click_film)
		#if the user toggles the eliminate option : self.connect("button-release-event", self.delete_click_film)

	def on_click_film(self, widget, event):
		detail_window = FilmDetailWindow(self.title, self.director, self.year, self.running_time, self.synopsis, self.cover_path)
		detail_window.show_all()