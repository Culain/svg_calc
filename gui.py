from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Gui:
    def __init__(self):
        self.svgfile = ""  # init Variable

        root = Tk()  # init Window
        root.wm_title("SVG-File Calculator")
        frame = Frame(root)
        frame.grid()

        menu = Menu(root)  # Menu
        root.config(menu=menu)
        submenu = Menu(menu)
        menu.add_cascade(label="File", menu=submenu)
        submenu.add_command(label="Open ", command=self.askopenfile)
        submenu.add_command(label="Print Preview", command=self.plot_preview)
        submenu.add_separator()
        submenu.add_command(label="Exit", command=frame.quit)

        root.mainloop()  # loop to keep the Window open

    def askopenfile(self):
        try:
            self.svgfile = filedialog.askopenfile(mode='r', filetypes=(("SVG Datei", "*.svg"), ("All files", "*.*")))
        except:
            messagebox("Error", "Couldn't read file.")

    def plot_preview(self):
        pass
