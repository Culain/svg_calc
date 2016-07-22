# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import cal


class Gui:
    def __init__(self):
        self.filename = ""  # init Variable
        self.svgfile = ""
        self.temp_time = 0
        self.length = 0
        self.speedpercent = 100.0
        self.temp_speedpercent = 100.0

        root = Tk()  # init Window
        root.wm_title("SVG-File Calculator")
        frame = Frame(root)
        frame.grid()

        menu = Menu(root)  # Menu
        root.config(menu=menu)
        submenu_file = Menu(menu)
        submenu_help = Menu(menu)
        # =============== File
        menu.add_cascade(label="File", menu=submenu_file)
        submenu_file.add_command(label="Open", command=self.askopenfile)
        submenu_file.add_command(label="Print Preview", command=self.plot_preview)
        submenu_file.add_separator()
        submenu_file.add_command(label="Exit", command=frame.quit)
        # ================ Help
        menu.add_cascade(label="Help", menu=submenu_help)
        submenu_help.add_command(label="About", command=self.aboutus)
        # ================

        self.textfield00 = Label(frame, text='Cuttingspeed in percent: ', font="14")
        self.textfield10 = Label(frame, text="nothing calculated yet", font="14")  # height=20, width=64)
        self.textfield20 = Label(frame, text='nothing calculated yet', font="14")
        self.percent = Entry(frame, text='100.0', font="14")
        self.buttonreload = Button(frame, text='reload', font="14", command=self.butreload)
        self.buttonclear = Button(frame, text='clear', font="14", command=self.butclear)

        self.textfield00.grid(row=0, column=0)
        self.textfield10.grid(row=1, column=0)
        self.textfield20.grid(row=2, column=0)
        self.percent.grid(row=0, column=1, sticky=E)
        self.buttonreload.grid(row=3, column=0)
        self.buttonclear.grid(row=3, column=1)

        # if root.focus_get() != ".":
        self.percent.focus_set()

        root.bind("<Return>", lambda x: self.butreload())
        # root.bind("<Return>", lambda y: print(root.focus_get()))

        root.mainloop()  # loop to keep the Window open

    def askopenfile(self):
        try:
            self.filename = filedialog.askopenfile(mode='r', filetypes=(("SVG Datei", "*.svg"), ("All files", "*.*")))
        except FileExistsError:  # TODO: except only fileerror
            # messagebox()
            print("Couldn't read file.")
        except FileNotFoundError:
            print("File not found.")
        # self.printmessages(self.temp_sum, self.temp_time, self.speedpercent)
        self.svgfile = cal.load_svg(self.filename)
        self.length = cal.calculate(self.svgfile)
        self.printmessages()

    def plot_preview(self):  # TODO: write "plotpreview"
        pass

    @staticmethod
    def aboutus():
        messagebox.showinfo("About", "SVG Calculator\nUsing Python 3.5\nCoded by: Culain and civ0")

    def printmessages(self):
        self.temp_speedpercent = self.speedpercent

        if self.percent.get() != '':  # error?
            self.speedpercent = self.conv_speed_p(self.percent.get())
        else:
            self.speedpercent = 100.0

        self.percent.delete(0, END)
        self.percent.insert(0, self.speedpercent)

        self.temp_time = cal.calculatetime(self.length, self.speedpercent)

        self.textfield10['text'] = 'The length of all Lines in this Document is: {:.2f}mm'.format(self.length)
        self.textfield20['text'] = 'Total time to print is: {:.2f} minutes at {:.2f}%'.format(self.temp_time,
                                                                                              self.speedpercent)

    def butreload(self):
        self.printmessages()

    def conv_speed_p(self, percentinput):

        try:
            y = float(percentinput)
            return y

        except ValueError:
            pattern = r"(\d*)(,|.)?(\d*)"
            y = re.match(pattern, percentinput)
            print(y.string)

            if not y:
                return 0
            result = y.string.replace(",", ".")

            try:
                return float(result)
            except ValueError:
                return self.temp_speedpercent

    def butclear(self):
        self.filename = ""  # init Variable
        self.svgfile = ""
        self.length = 0
        self.temp_time = 0
        self.speedpercent = 100.0
        self.printmessages()
