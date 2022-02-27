import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    
    def __init__(self):

        super().__init__(title="2FA Prettifier")
        self.set_border_width(10)
        #self.set_size_request(400,200)

        entry = Gtk.Entry()
        entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "input-dialpad-symbolic")
        submit = Gtk.Button(label="Prettify")
        output = Gtk.Label(label="XXXX XXXX XXXX XXXX")
        submit.connect("clicked", self.on_button_clicked, entry, output)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        grid.add(entry)
        grid.attach_next_to(submit, entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(output, 0, 2, 2, 1)

        self.add(grid)

    def on_button_clicked(self, widget, entry, label):
        code = entry.get_text()
        code = code.replace(" ", "")
        code = ' '.join([code[i:i+4] for i in range(0, len(code), 4)]).upper()
        label.set_text(code)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


# OLD CODE

# # 2 Factor Authentication Code Prettifier
# # Turns a mess of numbers and letters into XXXX XXXX XXXX XXXX


# # Tries to import copy module
# try:
#     import pyperclip
#     copy = True

# except:
#     print("PYPERCLIP IS NOT INSTALLED, INSTALLING IT THROUGH PIP IS ADVISED")
#     copy = False


# # Prettifier subroutine
# def prettify(code):

#     # Removes any spaces
#     code = code.replace(" ", "")

#     # Splits the string into parts of 4 and joins them with spaces
#     return ' '.join([code[i:i+4] for i in range(0, len(code), 4)]).upper()


# # Input
# print("2FA PRETTIFIER\n")
# code = input("Please enter 2FA seed: ")


# # Output
# code = prettify(code)
# print("\nThe new code is:")
# print(code)


# # Autocopy if possible
# if copy:
#     pyperclip.copy(code)
#     print("\nCode copied to clipboard\n")
# else:
#     print("\nCode not copied to clipboard\n")