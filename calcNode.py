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


from math import tan, sqrt


class calc_node:

    def line(self):
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

        x1 = float(self.getAttribute('x1'))
        y1 = float(self.getAttribute('y1'))
        x2 = float(self.getAttribute('x2'))
        y2 = float(self.getAttribute('y2'))

        line_length = tan(sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2))
        return line_length

    def polyline(self):  # <polyline class="fil0 str0" points="775,207 693,186 695,112 765,121 "/>
        poly = self.getAttribute('points')
        polysplit = poly.split(' ')[:-1]  # ['88,391', '21,398', '21,456', '80,456', '80,513', '26,500']
        format_split = []
        for split in polysplit:
            split = split.split(',')  # ['286', '519']
            temp = [float(split[0]), float(split[1])]  # [286.0, 519.0]
            format_split.append(temp)

        line_length = 0
        for x in range(1, len(format_split)):
            x1 = format_split[x-1][0]
            y1 = format_split[x-1][1]
            x2 = format_split[x][0]
            y2 = format_split[x][1]
            line_length += tan(sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2))

        return line_length