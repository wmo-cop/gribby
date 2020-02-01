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


class Section0(ctypes.LittleEndianStructure, StructHelper):
    """Section 0 - Indicator Section"""

    _pack_ = 1

    _fields_ = [
        ('signature', ctypes.c_char * 4),
        ('reserved', ctypes.c_char * 2),
        ('master_tables_version_number', ctypes.c_uint8),
        ('edition', ctypes.c_uint8),
        ('length', ctypes.c_uint64)
    ]


class Section1(ctypes.LittleEndianStructure, StructHelper):
    """Section 1 - Originator Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('centre', ctypes.c_uint16),
        ('subcentre', ctypes.c_uint16),
        ('local_tables_version_number', ctypes.c_uint8),
        ('identification_of_project', ctypes.c_uint8),
        ('production_status', ctypes.c_uint8),
        ('originator_local_template_number', ctypes.c_uint16),
        ('length_of_originator_local_template', ctypes.c_uint16),
        ('originator_local_template', ctypes.c_wchar_p),
        ('project_local_template_number', ctypes.c_uint16),
        ('length_of_project_local_template', ctypes.c_uint16),
        ('project_local_template', ctypes.c_wchar_p)
    ]


class Section2(ctypes.LittleEndianStructure, StructHelper):
    """Section 2 – Repetitions and Index Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('total_number_of_repetitions', ctypes.c_uint16),
        ('distinct_section3_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section4_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section5_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section6_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section7_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section8_greater_than_7_bytes', ctypes.c_uint16),
        ('distinct_section9_greater_than_7_bytes', ctypes.c_uint16),
        ('index_template_number', ctypes.c_uint16),
        ('length_of_index_template_number', ctypes.c_uint16),
        ('index_template', ctypes.c_wchar_p)
    ]


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


class Section4(ctypes.LittleEndianStructure, StructHelper):
    """Section 4 – Horizontal Domain Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('number_of_points_in_domain', ctypes.c_uint32),
        ('horizontal_domain_template_number', ctypes.c_uint16),
        ('horizontal_domain_template', ctypes.c_wchar_p)
    ]


class Section5(ctypes.LittleEndianStructure, StructHelper):
    """Section 5 – Vertical Domain Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('vertical_domain_template_number', ctypes.c_uint16),
        ('vertical_domain_template', ctypes.c_wchar_p)
    ]


class Section6(ctypes.LittleEndianStructure, StructHelper):
    """Section 6 – Generating Process Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('generating_process_template_number', ctypes.c_uint16),
        ('generating_process_template', ctypes.c_wchar_p)
    ]


class Section7(ctypes.LittleEndianStructure, StructHelper):
    """Section 7 – Observable Property Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('observable_property_template_number', ctypes.c_uint16),
        ('observable_property_template', ctypes.c_wchar_p)
    ]


class Section8(ctypes.LittleEndianStructure, StructHelper):
    """Section 8 – Data Representation Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('number_of_data_values_encoded_in_section_10', ctypes.c_uint32),
        ('data_representation_template_number', ctypes.c_uint16),
        ('data_representation_template', ctypes.c_wchar_p)
    ]


class Section9(ctypes.LittleEndianStructure, StructHelper):
    """Section 9 – Overlay Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('section_unique_identifier', ctypes.c_uint16),
        ('overlay_template_number', ctypes.c_uint16),
        ('overlay_template', ctypes.c_wchar_p)
    ]


class Section10(ctypes.LittleEndianStructure, StructHelper):
    """Section 10 – Data Section"""

    _pack_ = 1

    _fields_ = [
        ('length', ctypes.c_uint32),
        ('number_of_section', ctypes.c_uint8),
        ('data', ctypes.c_wchar_p)
    ]


class Section11(ctypes.LittleEndianStructure, StructHelper):
    """Section 11 – End section"""

    _pack_ = 1

    _fields_ = [
        ('signature', ctypes.c_char * 4)
    ]
