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


from xml.dom.minidom import parse

from CalcNode import CalcNode


def load_svg(filename):
    svgdoc = parse(filename)
    rootnode = svgdoc.documentElement

    return rootnode


def calculate(svg_node):
    temp_sum = 0

    if not svg_node:
        return -1

    lines = svg_node.getElementsByTagName('line')
    polylines = svg_node.getElementsByTagName('polyline')
    rectangles = svg_node.getElementsByTagName('rect')
    ellipses = svg_node.getElementsByTagName('ellipse')
    circles = svg_node.getElementsByTagName('circle')
    paths = svg_node.getElementsByTagName('path')
    polygons = svg_node.getElementsByTagName('polygon')

    for line in lines:
        temp_sum += CalcNode.line(line)

    for polyline in polylines:
        temp_sum += CalcNode.polyline(polyline)

    for rectangle in rectangles:
        temp_sum += CalcNode.rectangle(rectangle)

    for ellipse in ellipses:
        temp_sum += CalcNode.ellipses(ellipse)

    for circle in circles:
        temp_sum += CalcNode.circles(circle)

    for polygon in polygons:
        temp_sum += CalcNode.polygons(polygon)

    for path in paths:
        temp_sum += CalcNode.paths(path)

    return temp_sum


def calculatetime(length, percent):
    speed = 1524  # mm/sec
    length = length  # Umwandlung in mm
    timetoprint = length / (speed * (percent / 100))  # v = s/t  | s/v = t
    truetimetoprint = timetoprint

    return truetimetoprint

    # try:
    #     dimensions = get_dimensions(svgfile)
    # except AttributeError:
    #     print("Error. Can't find Dimensions in the File")  # TODO: Popup? via messagebox


def get_dimensions(svgfile):
    height = svgfile.getAttribute('height')
    width = svgfile.getAttribute('width')
    # TODO: unit conversions
    height = float(height.replace('mm', ''))
    width = float(width.replace('mm', ''))
    dim = [width, height]
    return dim
