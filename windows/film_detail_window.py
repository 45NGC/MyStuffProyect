import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FilmDetailWindow(Gtk.Window):

	def __init__(self, title, director, year, running_time, description, cover):
		super().__init__(title="Details")

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(300, 450)
		self.set_position(Gtk.WindowPosition.CENTER)

		# WINDOW ELEMENTS

		# TITLE
		title = Gtk.Label(label = title)

		# COVER
		extracted_pixbuf = Gtk.Image.get_pixbuf(cover)
		#Introduce the extracted pixbuf in a gtk image variable and show it
		cover_gtk = Gtk.Image()
		cover_gtk.set_from_pixbuf(extracted_pixbuf)

		# DESCRIPTION
		descripcion = Gtk.Label(label = description)
		
		# ADD THE ELEMENTS TO A VERTICAL ORIENTED BOX
		box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		box.pack_start(title, True, True, 0)
		box.pack_start(cover_gtk, True, True, 0)
		box.pack_start(descripcion, True, True, 0)
		self.add(box)