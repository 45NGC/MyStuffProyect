from turtle import title
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windows.film_detail_window import FilmDetailWindow

class FilmCell(Gtk.EventBox):

	def __init__(self, title, director, year, running_time, description, cover):
		super().__init__()
		self.title = title
		self.director = director
		self.year = year
		self.running_time = running_time
		self.description = description
		self.cover = cover

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
		box.pack_start(Gtk.Label(label=title), False, False, 0)
		box.pack_start(cover, True, True, 0)
		self.add(box)

		# If the user presses the cell show film_detail_window
		self.connect("button-release-event", self.on_click_film)

	def on_click_film(self, widget, event):
		detail_window = FilmDetailWindow(self.title, self.director, self.year, self.running_time, self.description, self.cover)
		detail_window.show_all()