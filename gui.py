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
        self.filepath2 = ''
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
        submenu_file.add_command(label='Print Preview', command=self.print_preview)
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
        self.btn_print_preview = Button(frame, text='Preview', font='14', height=1, width=8, command=self.print_preview)

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
        self.btn_print_preview.grid(row=2, column=2)

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
            self.filepath2 = self.filepath
            self.update_entry(self.entry_filepath, self.filepath)
            if self.filepath:
                self.load_file()
        except FileExistsError:
            messagebox.showerror('File Error')
        except FileNotFoundError:
            messagebox.showerror('Error: File not found.')

    def print_preview(self):  # TODO: write 'plotpreview'
        if self.file:
            dimension = cal.get_dimensions(self.svgfile)
        else:
            return 0

        root = Tk()  # init Window
        root.wm_title('Preview Window')
        # preview_frame = Frame(root, height=dimension[1], width=dimension[0])
        # preview_frame.pack()


        # preview_canvas = Canvas(master=root, width=dimension[0], height=dimension[1])
        # preview_canvas.pack()
        #
        # lines = self.svgfile.getElementsByTagName('line')
        # polylines = self.svgfile.getElementsByTagName('polyline')
        # rectangles = self.svgfile.getElementsByTagName('rect')
        # ellipses = self.svgfile.getElementsByTagName('ellipse')
        # circles = self.svgfile.getElementsByTagName('circle')
        # paths = self.svgfile.getElementsByTagName('path')
        # polygons = self.svgfile.getElementsByTagName('polygon')
        #
        # for line in lines:
        #     x1 = float(line.getAttribute('x1'))
        #     y1 = float(line.getAttribute('y1'))
        #     x2 = float(line.getAttribute('x2'))
        #     y2 = float(line.getAttribute('y2'))
        #     preview_canvas.create_line(x1, y1, x2, y2)
        #
        # for polyline in polylines:
        #     poly = polyline.getAttribute('points')
        #     polysplit = poly.split(' ')[:-1]
        #     format_split = []
        #     for split in polysplit:
        #         split = split.split(',')
        #         temp = [float(split[0]), float(split[1])]
        #         format_split.append(temp)
        #
        #     for x in range(1, len(format_split)):
        #         x1 = format_split[x - 1][0]
        #         y1 = format_split[x - 1][1]
        #         x2 = format_split[x][0]
        #         y2 = format_split[x][1]
        #         preview_canvas.create_line(x1, y1, x2, y2)
        #
        # for rectangle in rectangles:
        #     x1 = float(rectangle.getAttribute('x'))
        #     y1 = float(rectangle.getAttribute('y'))
        #     x2 = x1 + float(rectangle.getAttribute('width'))
        #     y2 = y1 + float(rectangle.getAttribute('height'))
        #     preview_canvas.create_rectangle(x1, y1, x2, y2)
        #
        # for ellipse in ellipses:
        #
        #     if ellipse.getAttribute('transform'):
        #         matrix = ellipse.getAttribute('transform')
        #         print(matrix)
        #     else:
        #         x1 = float(ellipse.getAttribute('cx'))
        #         y1 = float(ellipse.getAttribute('cy'))
        #         x2 = x1 + float(ellipse.getAttribute('rx'))
        #         y2 = y1 + float(ellipse.getAttribute('ry'))
        #         preview_canvas.create_oval(x1, y1, x2, y2)


    @staticmethod
    def aboutus():
        messagebox.showinfo('About', 'SVG Calculator\nUsing Python 3.5\nWritten by: Culain and civ0')
