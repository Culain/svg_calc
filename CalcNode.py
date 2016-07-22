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

from math import tan, sqrt, pi
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path


class CalcNode:

    def __init__(self):
        pass

    def line(self):
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

        x1 = float(self.getAttribute('x1'))
        y1 = float(self.getAttribute('y1'))
        x2 = float(self.getAttribute('x2'))
        y2 = float(self.getAttribute('y2'))

        line_length = tan(sqrt((x2 - x1)**2 + (y2 - y1)**2))
        return abs(line_length)

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
            line_length += sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return abs(line_length)

    def rectangle(self):  # <rect class="fil0 str0" x="492" y="538" width="32.6813" height="27.0933"/>
        x = float(self.getAttribute('width'))
        y = float(self.getAttribute('height'))

        line_length = x * 2 + y * 2

        return abs(line_length)

    def ellipses(self):  # <ellipse class="fil0 str0" cx="580" cy="553" rx="24" ry="13"/>
        rx = float(self.getAttribute('rx'))
        ry = float(self.getAttribute('ry'))

        h = (rx - ry)**2 / (rx + ry)**2
        line_length = pi * (rx + ry) * (1 + 3 * h / (10 + ((4 - 3*h)**0.5)))

        return abs(line_length)

    def circles(self):  # <circle class="fil0 str0" cx="671" cy="562" r="16"/>
        r = float(self.getAttribute('r'))

        line_length = pi * 2 * r

        return abs(line_length)

    def polygons(self):  # <polygon class="fil0 str0" points="441,539 452,546 462,552 458,563 454,574 441,574 429,574 425,563 421,552 431,546 "/>
        line_length = CalcNode.polyline(self)  # Same calculation

        return abs(line_length)

    def paths(self):  # <path class="fil1" d="M625 453l0 -19 3 0 0 2c1,-2 4,-3 6,-3 1,0 2,0 3,1 1,0 2,1 3,...6l0 10 -3 0z"/>
        parsed_path = parse_path(self.getAttribute("d"))
        line_length = parsed_path.length(error=1e-5)  # Error for faster calculation / lower accuracy

        return abs(line_length)