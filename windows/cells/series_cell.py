import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from windows.detail_windows.series_detail_window import SeriesDetailWindow

class SeriesCell(Gtk.EventBox):

	def __init__(self, title, director, year, seasons, episodes, episode_running_time, synopsis, cover_path):
		super().__init__()
		self.title = title
		self.director = director
		self.year = year
		self.seasons = seasons
		self.episodes = episodes
		self.episode_running_time = episode_running_time
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
		self.connect("button-release-event", self.on_click_series)

		# Add 2 if conditionals, one for each button of the interface:
		#if the user toggles the mod option : self.connect("button-release-event", self.mod_click_film)
		#if the user toggles the eliminate option : self.connect("button-release-event", self.delete_click_film)

	def on_click_series(self, widget, event):
		detail_window = SeriesDetailWindow(self.title, self.director, self.year, self.seasons, self.episodes, self.episode_running_time, self.synopsis, self.cover_path)
		detail_window.show_all()