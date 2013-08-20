"""Uses the split function on each line in text file, this produces a list
of words in that line. It then takes the length of the list to get the word
count for that line. This is added to total word count for each line processed."""

from Tkinter import *
import tkMessageBox

root = Tk()

#Sets attributes of the main window.
root.wm_title("Word Counter") #Sets window title.
#root.geometry("300x300") #Sets window size.
root.wm_resizable(0,0) #Prevents resizing of window.

#Instructions on use.
instructions = Label(root, text = "Please provide the file path below, then press \nthe button or hit enter to get the word count.", padx = 10, pady = 5)
instructions.grid(row = 0)

#Creates a text entry box for the file path.
filepath = Entry(root, width = 40)
filepath.grid(row = 1, pady = 10, padx = 20)

#Performs the counting of text in the file.
def count(event):
	totalwords = 0

	with open(filepath.get()) as f:
		for lines in f:
			totalwords =  totalwords + len(lines.split())

	tkMessageBox.showinfo("Word Count", "Word Count: %s" % totalwords) #Produces message box with word count.

filepath.bind("<Return>", count) #Activates word count on enter key press.

countbutton = Button(root, text = "Count", command = lambda:count(0))
countbutton.grid(row = 2, pady = 15)

root.mainloop()