from Tkinter import *
import tkMessageBox

root = Tk()

root.wm_title("Word Counter") #Sets window title.
#root.geometry("300x300") #Sets window size.
root.wm_resizable(0,0) #Prevents resizing of window.

#Section headings.
filepathlabel = Label(root, text = "FILE PATH", padx = 10, pady = 5, background = 'gray')
filepathlabel.grid(row = 0, sticky = W+E)
textboxlabel = Label(root, text = "TEXT ENTRY", padx = 10, pady = 5, background = 'gray')
textboxlabel.grid(row = 2, sticky = W+E)

#Creates radio buttons for choosing input.
v = IntVar()
radbut = Radiobutton(root, variable = v, value = 1, background = 'gray')
radbut.grid(row = 0, sticky = W)
radbut2 = Radiobutton(root, variable = v, value = 2, background = 'gray')
radbut2.grid(row = 2, sticky = W)
radbut.select()

#Creates a text entry box for the file path.
filepath = Entry(root, width = 40)
filepath.grid(row = 1, pady = 10, padx = (15, 20))

#Creates a text box for simple text entry.
inputtext = Text(root, width = 46, highlightbackground = "gray")
inputtext.grid(row = 3, pady = (20, 0))

#Performs the counting of text in the file.
def count(event):

	totalwords = 0 #Variable used to store the word count.

	if v.get() == 1: #Checks the radio buttons for input selection.

		try: #Checks to see if the file exists.
			with open(filepath.get()) as f:
				for lines in f:
					totalwords =  totalwords + len(lines.split())
			tkMessageBox.showinfo("Word Count", "Word Count: %s" % totalwords) #Produces message box with word count.

		except IOError:
			tkMessageBox.showinfo("File Error", "I'm sorry, that file does not exist. Make sure to use the radio buttons to select your input.")

	elif v.get() == 2:

		for lines in inputtext.get(1.0, END).splitlines():
			totalwords = totalwords + len(lines.split())
		tkMessageBox.showinfo("Word Count", "Word Count: %s" % totalwords) #Produces message box with word count.

	else: #Should never reach this statement, included as a precaution.

		tkMessageBox.showwarning("Warning", "Please select, using the radio buttons, whether you would like to use a file path or the text box.")


filepath.bind("<Return>", count) #Activates word count on enter key press.

#Button to initialise the word counting.
countbutton = Button(root, text = "Count", command = lambda:count(0), width = 40)
countbutton.grid(row = 4, pady = 15)

root.mainloop()