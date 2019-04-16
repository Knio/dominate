# -*- coding: utf-8 -*-

from __future__ import print_function
from .css import css


"""
HTML style class.
"""
__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with Dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''


class style(css):
    def __str__(self):
        return css.__str__(self, 0, True)


if __name__ == '__main__':
    _style = style()

    _style.display = 'inline-block'
    _style.width = '100%'
    _style.height = '200px'
    _style.border = 'solid 1px #555573'
    _style.overflow = 'hidden'
    _style.margin_top = '30px'
    _style.box_sizing = 'border-box'

    print(_style)
