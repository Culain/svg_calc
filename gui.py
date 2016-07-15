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
        self.temp_sum = 0
        self.temp_time = 0
        self.temp_speedpercent = 100

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
        self.prozent = Entry(frame, text='100', font="14")
        self.buttonreload = Button(frame, text='reload', font="14", command=self.butreload)
        self.buttonclear = Button(frame, text='clear', font="14")

        self.textfield00.grid(row=0, column=0)
        self.textfield10.grid(row=1, column=0)
        self.textfield20.grid(row=2, column=0)
        self.prozent.grid(row=0, column=1, sticky=E)
        self.buttonreload.grid(row=3, column=0)
        self.buttonclear.grid(row=3, column=1)

        root.mainloop()  # loop to keep the Window open

    def askopenfile(self):
        try:
            self.filename = filedialog.askopenfile(mode='r', filetypes=(("SVG Datei", "*.svg"), ("All files", "*.*")))
        except:  # TODO: except only fileerror
            messagebox("Couldn't read file.")
        # TODO: Add some code here to work with the file
        # self.printmessages(self.temp_sum, self.temp_time, self.temp_speedpercent)
        self.svgfile = cal.load_svg(self.filename)
        self.printmessages()


    def plot_preview(self):  # TODO: write "plotpreview"
        pass

    def aboutus(self):
        messagebox.showinfo("About", "SVG Calculator\nUsing Python 3.5\nCoded by: Culain and civ0")

    def printmessages(self):
        if self.prozent.get() != '':
            self.temp_speedpercent = self.conv_speed_p(self.prozent.get())
        else:
            self.temp_speedpercent = 100

        if self.svgfile:
            self.temp_sum = cal.calculate(self.svgfile)  # float
        else:
            self.temp_sum = 0
        self.temp_time = cal.calculatetime(self.temp_sum)

        self.textfield10['text'] = 'The length of all Lines in this Document is: {:.2f}mm'.format(self.temp_sum)
        self.textfield20['text'] = 'Total time to print is: {:.2f} minutes at {:.2f}%'.format(self.temp_time,
                                                                                              self.temp_speedpercent)

    def butreload(self):
        self.printmessages()

    def conv_speed_p(self, input):

        try:
            y = float(input)
            return y

        except ValueError:
            pattern = r"(\d+)(,|.)?(\d*)"

            y = re.match(pattern, input)
            if y == None:
                return 0
            z = y.group().split(",")
            result = float(z[0] + "." + z[1])

            return result