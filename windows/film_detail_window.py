import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class FilmDetailWindow(Gtk.Window):

	def __init__(self, title, director, year, running_time, synopsis, cover_path):
		super().__init__(title="Details")

		# WINDOW PROPERTIES
		self.set_border_width(15)
		self.set_default_size(300, 300)
		self.set_resizable(False)
		self.set_position(Gtk.WindowPosition.CENTER)

		# WINDOW ELEMENTS
		horizontal_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 40)
		vertical_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 40)
		details_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 40)

		# COVER
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = cover_path, width=350, height=350, preserve_aspect_ratio=True)
		image = Gtk.Image.new_from_pixbuf(pixbuf)


		# DETAILS
		details = Gtk.Label()
		details.set_text('Title : '+title+'\n\n\nYear : '+str(year)+'\n\n\nDirector : '+director+'\n\n\nRunning time : '+str(running_time)+' min.')
		details.set_line_wrap(True)
		details.set_justify(Gtk.Justification.LEFT)

		# DESCRIPTION
		synopsis = Gtk.Label(label = synopsis)
		synopsis.set_line_wrap(True)
		synopsis.set_max_width_chars(140)
		
		# ADD THE DETAILS TO A VERTICAL BOX
		details_box.pack_start(details, True, True, 0)
		
		# ADD THE details_box AND THE image TO A HORIZONTAL ORIENTED BOX
		horizontal_box.pack_start(details_box, True, True, 0)
		horizontal_box.pack_start(image, True, True, 0)

		# ADD THE ELEMENTS TO A VERTICAL ORIENTED BOX
		vertical_box.pack_start(horizontal_box, True, True, 0)
		vertical_box.pack_start(synopsis, True, True, 0)

		self.add(vertical_box)