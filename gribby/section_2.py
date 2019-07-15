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


class Section2(ctypes.LittleEndianStructure, StructHelper):
    """Section 2 – Repetitions and Index Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('total_number_of_repetitions', ctypes.c_uint16),
        ('distinct_section3_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section4_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section5_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section6_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section7_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section8_greater_than_7_bytes ', ctypes.c_uint16),
        ('distinct_section9_greater_than_7_bytes ', ctypes.c_uint16),
        ('index_template_number', ctypes.c_uint16),
        ('length_of_index_template_number', ctypes.c_uint16),
        ('index_template', ctypes.c_wchar_p)
    ]
