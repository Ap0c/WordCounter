# ---------- Imports ---------- #

from tkinter import Tk, Label, IntVar, Radiobutton, Entry, Text, Button
from tkinter import W, E, END
import tkinter.messagebox as message


# ---------- Setup ---------- #

PATH = 1
TEXT = 2


# ---------- Functions ---------- #

def create_window():

	"""Creates window object, sets title and resizing."""

	root = Tk()

	root.wm_title("Word Counter")
	root.wm_resizable(0, 0)

	return root


def section_headings(root, elements):

	"""Creates and positions window section headings."""

	filepath_label = Label(root, text = "FILE PATH", padx = 10, pady = 5,
		background = 'gray')

	textbox_label = Label(root, text = "TEXT ENTRY", padx = 10, pady = 5,
		background = 'gray')

	filepath_label.grid(row = 0, sticky = W+E)
	textbox_label.grid(row = 2, sticky = W+E)

	elements["filepath_label"] = filepath_label
	elements["textbox_label"] = textbox_label

	return elements


def radio_buttons(root, elements):

	"""Creates and positions radio buttons for task selection."""

	button_var = IntVar()

	path_button = Radiobutton(root, variable = button_var, value = PATH,
		background = 'gray')

	textbox_button = Radiobutton(root, variable = button_var, value = TEXT,
		background = 'gray')

	path_button.grid(row = 0, sticky = W)
	textbox_button.grid(row = 2, sticky = W)

	path_button.select()

	elements["path_button"] = path_button
	elements["textbox_button"] = textbox_button
	elements["button_var"] = button_var

	return elements


def entry_fields(root, elements):

	"""Creates and positions fields for text entry."""

	filepath = Entry(root, width = 40)
	input_text = Text(root, width = 46, highlightbackground = "gray")

	filepath.grid(row = 1, pady = 10, padx = (15, 20))
	input_text.grid(row = 3, pady = (20, 0))

	elements["filepath"] = filepath
	elements["input_text"] = input_text

	return elements


def scan_file(elements):

	"""Scans the words from file an prints the count."""

	word_count = 0

	try:

		with open(elements["filepath"].get()) as f:
			for lines in f:
				word_count = word_count + len(lines.split())

		message.showinfo("Word Count", "Word Count: %s" % word_count)

	except IOError:

		message.showinfo("File Error", "There was a problem opening the "
			"file, does it exist?. Make sure to use the radio buttons to "
			"select your input.")


def scan_text(elements):

	"""Scans the text from the box and prints the count."""

	word_count = 0

	for line in elements["input_text"].get(1.0, END).splitlines():
		word_count = word_count + len(line.split())

	message.showinfo("Word Count", "Word Count: %s" % word_count)


def count_words(root, elements, event):

	"""Counts based upon user preference."""

	if elements["button_var"].get() == PATH:
		scan_file(elements)
	elif elements["button_var"].get() == TEXT:
		scan_text(elements)
	else:
		message.showwarning("Warning", "Please selectwhether you would "
			"like to use a file path or the text box.")


def events(root, elements):

	"""Creates and configures actions based upon user events."""

	elements["filepath"].bind("<Return>", count_words)

	count_button = Button(root, text = "Count",
		command = lambda: count_words(root, elements, 0), width = 40)

	count_button.grid(row = 4, pady = 15)

	return elements


# ---------- Main ---------- #

if __name__ == '__main__':

	# Creates window and window elements dictionary.
	root = create_window()
	elements = {}

	# Fills in the window.
	elements = section_headings(root, elements)
	elements = radio_buttons(root, elements)
	elements = entry_fields(root, elements)
	elements = events(root, elements)

	# Starts the graphics loop.
	root.mainloop()
