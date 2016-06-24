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
from xml.parsers.expat import ExpatError
from calcNode import calc_node
# import exceptions


def load_svg(filename):
    try:
        svgdoc = parse(filename)
        rootnode = svgdoc.documentElement
        return rootnode
    except ExpatError:
        raise ExpatError


def calculate(filename):
    sum = 0

    try:
        svg_node = load_svg(filename)
    except:
        print("Error while loading file")
        exit()
    lines = svg_node.getElementsByTagName('line')
    polylines = svg_node.getElementsByTagName('polyline')
    rectangles = svg_node.getElementsByTagName('rect')
    ellipses = svg_node.getElementsByTagName('ellipse')
    circles = svg_node.getElementsByTagName('circle')
    paths = svg_node.getElementsByTagName('path')
    polygons = svg_node.getElementsByTagName('polygon')

    for line in lines:
        sum += calc_node.line(line)

    for polyline in polylines:
        sum += calc_node.polyline(polyline)

    return sum

    # try:
    #     dimensions = get_dimensions(svgfile)
    # except AttributeError:
    #     print("Error. Can't find Dimensions in the File")  # TODO: Popup? via messagebox

def get_dimensions(svgfile):
    height = svgfile.getAttribute('height')
    width = svgfile.getAttribute('width')
    # TODO: unit conversions
    height = height.replace('mm', '')
    width = width.replace('mm', '')
    dim = [float(width), float(height)]
    return dim

