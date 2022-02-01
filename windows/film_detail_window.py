import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FilmDetailWindow(Gtk.Window):

	def __init__(self, title, director, year, running_time, synopsis, cover):
		super().__init__(title="Details")

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(300, 300)
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
		
		# ADD THE DETAILS TO A DETAILS BOX ORIENTED VERTICALLY
		details_box.pack_start(Gtk.Label(label = title), False, False, 0)
		details_box.pack_start(Gtk.Label(label = year), False, False, 0)
		details_box.pack_start(Gtk.Label(label = running_time), False, False, 0)
		details_box.pack_start(Gtk.Label(label = director), False, False, 0)

		# ADD THE ELEMENTS TO A HORIZONTAL ORIENTED BOX
		horizontal_box.pack_start(image, True, True, 0)
		horizontal_box.pack_start(details_box, True, True, 0)

		# ADD THE ELEMENTS TO A VERTICAL ORIENTED BOX
		vertical_box.pack_start(horizontal_box, True, True, 0)
		# DESCRIPTION
		vertical_box.pack_start(Gtk.Label(label = synopsis), True, True, 0)


		self.add(vertical_box)