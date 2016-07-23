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
        self.filename = ''  # init Variable
        self.filepath = ''
        self.svgfile = ''
        self.file = None
        self.length = 0
        self.time = 0
        self.speedpercent = 100.0

        root = Tk()  # init Window
        root.wm_title('SVG-File Calculator')
        frame = Frame(root)
        frame.grid()

        menu = Menu(root)  # Menu
        root.config(menu=menu)
        submenu_file = Menu(menu)
        submenu_help = Menu(menu)
        # =============== File
        menu.add_cascade(label='File', menu=submenu_file)
        submenu_file.add_command(label='Open', command=self.browse_file)
        submenu_file.add_command(label='Print Preview', command=self.plot_preview)
        submenu_file.add_separator()
        submenu_file.add_command(label='Exit', command=frame.quit)
        # ================ Help
        menu.add_cascade(label='Help', menu=submenu_help)
        submenu_help.add_command(label='About', command=self.aboutus)
        # ================

        self.txt_filepath = Label(frame, text='File', font='14')
        self.txt_speed_percent = Label(frame, text='Cuttingspeed in percent', font='14')
        self.txt_placeholder1 = Label(frame, text='', font='14')
        self.txt_result_length = Label(frame, text='Calculated length', font='14')
        self.txt_result_time = Label(frame, text='Calculated time', font='14')
        self.txt_result_length_out = Label(frame, text='-', font='14')
        self.txt_result_time_out = Label(frame, text='-', font='14')
        self.entry_filepath = Entry(frame, font='14', width=60)
        self.entry_speed_percent = Entry(frame, font='14')
        self.entry_speed_percent.insert(0, '100.0')
        self.btn_open_file = Button(frame, text='Browse', font='14', height=1, width=8, command=self.browse_file)
        self.btn_calculate = Button(frame, text='Calculate', font='14', height=1, width=8, command=self.update_gui)

        self.txt_filepath.grid(row=0, column=0, sticky=W)
        self.txt_speed_percent.grid(row=1, column=0, sticky=W)
        self.txt_placeholder1.grid(row=2, column=0, columnspan=3)
        self.txt_result_length.grid(row=3, column=0, sticky=W)
        self.txt_result_time.grid(row=4, column=0, sticky=W)
        self.txt_result_length_out.grid(row=3, column=1, sticky=W)
        self.txt_result_time_out.grid(row=4, column=1, sticky=W)
        self.entry_filepath.grid(row=0, column=1, sticky=W+E)
        self.entry_speed_percent.grid(row=1, column=1, sticky=W+E)
        self.btn_open_file.grid(row=0, column=2)
        self.btn_calculate.grid(row=1, column=2)

        self.entry_filepath.bind('<Return>', self.load_file)
        self.entry_speed_percent.bind('<Return>', self.update_gui)
        self.entry_filepath.bind('<KP_Enter>', self.load_file)
        self.entry_speed_percent.bind('<KP_Enter>', self.update_gui)
        root.bind('<Escape>', lambda x: frame.quit())

        root.mainloop()  # loop to keep the Window open

    @staticmethod
    def update_entry(entry, text):
        entry.delete(0, END)
        entry.insert(0, text)

    def update_gui(self):
        try:
            pattern = r'(\d*)(,|.)?(\d*)'
            user_input = self.entry_speed_percent.get()
            tmp = re.match(pattern, user_input)
            res = tmp.string.replace(',', '.')
            res_float = float(res)
            if 0 < res_float <= 100:
                self.speedpercent = res_float
                self.update_entry(self.entry_speed_percent, self.speedpercent)
            else:
                self.update_entry(self.entry_speed_percent, self.speedpercent)
        except ValueError:
            self.update_entry(self.entry_speed_percent, self.speedpercent)
            return 0
        self.time = cal.calculatetime(self.length, self.speedpercent)
        self.txt_result_time_out.configure(text='{:.2f} minutes'.format(self.time))

    def load_file(self):
        try:
            self.filepath = self.entry_filepath.get()
            self.file = open(self.filepath, 'r')
            self.svgfile = cal.load_svg(self.file)
            self.length = cal.calculate(self.svgfile)
            self.txt_result_length_out.configure(text='{:.2f}mm'.format(self.length))
            self.update_gui()
        except FileExistsError:
            messagebox.showerror('File Error')
        except FileNotFoundError:
            messagebox.showerror('Error: File not found.')

    def browse_file(self):
        try:
            self.filepath = filedialog.askopenfilename(title='Select file', filetypes=(('SVG-Files', '*.svg'), ('All files', '*.*')))
            self.update_entry(self.entry_filepath, self.filepath)
            if self.filepath:
                self.load_file()
        except FileExistsError:
            messagebox.showerror('File Error')
        except FileNotFoundError:
            messagebox.showerror('Error: File not found.')

    def plot_preview(self):  # TODO: write 'plotpreview'
        pass

    @staticmethod
    def aboutus():
        messagebox.showinfo('About', 'SVG Calculator\nUsing Python 3.5\nWritten by: Culain and civ0')
