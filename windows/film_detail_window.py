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
		details_grid = Gtk.Grid()

		# COVER
		my_pixbuf = Gtk.Image.get_pixbuf(cover)
		image = Gtk.Image()
		image.set_from_pixbuf(my_pixbuf)

		# DETAILS
		title = Gtk.Label(label = title)
		year = Gtk.Label(label = year)
		running_time = Gtk.Label(label = running_time)
		director = Gtk.Label(label = director)
		
		# ADD THE DETAILS TO A DETAILS GRID
		details_grid.add(title)
		details_grid.attach_next_to(year, title, Gtk.PositionType.BOTTOM, 1, 2)
		details_grid.attach_next_to(running_time, year, Gtk.PositionType.BOTTOM, 1, 2)
		details_grid.attach_next_to(director, running_time, Gtk.PositionType.BOTTOM, 1, 2)

		# ADD THE ELEMENTS TO A HORIZONTAL ORIENTED BOX
		horizontal_box.pack_start(image, True, True, 0)
		horizontal_box.pack_start(details_grid, True, True, 0)

		# ADD THE ELEMENTS TO A VERTICAL ORIENTED BOX
		vertical_box.pack_start(horizontal_box, True, True, 0)
		# DESCRIPTION
		vertical_box.pack_start(Gtk.Label(label = synopsis), True, True, 0)


		self.add(vertical_box)