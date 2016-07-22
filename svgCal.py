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

"""
__version__ = 0.7
__last_update__ = 2016/07/23
__author__ = "Culain aka. lordfwahfnah", "civ0\"
"""

import gui


# import exceptions
# from sys import platform
# from xml.parsers.expat import ExpatError


def main():
    """  # Debug foo
    filename = ''
    sum = 0
    if platform.startswith('win32'):
        filename = 'svgFiles\\test.svg'
        # filename = 'svgFiles\\corrupt.svg'
    elif platform.startswith('linux'):
        filename = 'svgFiles/test.svg'

    try:
        sum = cal.calculate(filename)
    except ExpatError:
        print("Error while reading the file")
        exit()
    print(sum)

    # res = cal.calculate(svgfile)
    # print(res)
    """

    # noinspection PyUnusedLocal
    o_gui = gui.Gui()  # ===GUI stuff=== uncomment to disable


if __name__ == '__main__':
    main()
