# =================================================================
#
# Author: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2019 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import ctypes
import logging

from gribby.helpers import StructHelper

LOGGER = logging.getLogger(__name__)


class Section3(ctypes.LittleEndianStructure, StructHelper):
    """Section 3 – Time Domain Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('significance_of_reference_date_and_time', ctypes.c_uint8),
        ('type_of_calendar', ctypes.c_uint8),
        ('year', ctypes.c_uint32),
        ('month', ctypes.c_uint8),
        ('day', ctypes.c_uint8),
        ('hour', ctypes.c_uint8),
        ('minute', ctypes.c_uint8),
        ('second', ctypes.c_uint8),
        ('time_domain_template_number', ctypes.c_uint16),
        ('time_domain_template', ctypes.c_wchar_p)
    ]
