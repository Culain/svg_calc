from tkinter import *
# from tkinter import filedialog


class Gui:
    def __init__(self):
        self.file = ""
        root = Tk()
        root.wm_title("SVG-File Calculator")

        frame = Frame(root)
        frame.grid()

        menu = Menu(root)
        root.config(menu=menu)

        submenu = Menu(menu)
        menu.add_cascade(label="File", menu=submenu)
        submenu.add_command(label="Open ", command=self.askopenfile)
        submenu.add_command(label="Print Preview", command=self.plot_preview)
        submenu.add_separator()
        submenu.add_command(label="Exit", command=frame.quit)

        root.mainloop()

    def askopenfile(self):
        pass

    def plot_preview(self):
        pass
