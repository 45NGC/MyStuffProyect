from cProfile import run
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FilmDetailWindow(Gtk.Window):

	def __init__(self, title, director, year, running_time, synopsis, cover):
		super().__init__(title="Details")

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(700, 700)
		self.set_resizable(False)
		self.set_position(Gtk.WindowPosition.CENTER)

		# WINDOW ELEMENTS
		horizontal_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		vertical_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		details_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

		# COVER
		my_pixbuf = Gtk.Image.get_pixbuf(cover)
		image = Gtk.Image()
		image.set_from_pixbuf(my_pixbuf)
		

		# DETAILS
		title = Gtk.Label(label = title)
		year = Gtk.Label(label = year)
		running_time = Gtk.Label(label = running_time)
		director = Gtk.Label(label = director)

		# ADD THE DETAILS TO A DETAILS BOX ORIENTED VERTICALLY
		details_box.pack_start(Gtk.Label(title), False, False, 0)
		details_box.pack_start(Gtk.Label(year), False, False, 0)
		details_box.pack_start(Gtk.Label(running_time), False, False, 0)
		details_box.pack_start(Gtk.Label(director), False, False, 0)

		# ADD THE ELEMENTS TO A HORIZONTAL ORIENTED BOX
		horizontal_box.pack_start(image, True, True, 0)
		horizontal_box.pack_start(details_box, True, True, 0)

		# ADD THE ELEMENTS TO A VERTICAL ORIENTED BOX
		vertical_box.pack_start(horizontal_box, True, True, 0)
		# DESCRIPTION
		vertical_box.pack_start(Gtk.Label(label = synopsis))


		self.add(vertical_box)