from tkinter import Tk, BOTH
from tkinter.ttk import Frame
# Tk is used to create a root window, Frame container for other widgets.

class Example(Frame):  
	def __init__(self):
		super().__init__()
# __init__ constructor calls the constructor of the inherited class, Frame
		self.initUI()
# creation of the UI taken by initUI method


	def initUI(self):

		self.master.title("Simple")
# title method used to give the root window(Tk) a window title, by using master attribute.
		self.pack(fill=BOTH, expand=1)
# pack method: horizontal and vertical boxes for widgets, expanding in both directions, 
# taking all of root. self is Tk root window.


def main():
	root = Tk()
# root window created.	
	root.geometry("250x150+300+300")
# size of window, in format ("width x height + x coords + y coords")
	app = Example()
# instance of the application class (line 5)
	root.mainloop()
# last stage - mainloop. Starts event handling - receives events from the window system and sends
# them to the app widgets


if __name__ == '__main__':
	main()