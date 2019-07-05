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

from datetime import datetime, time
from io import StringIO
import logging
from struct import pack
import sys

from gribby import section_0, section_11

__version__ = '0.1.0'

LOGGER = logging.getLogger(__name__)

LOGGER.debug('System byte order: {}'.format(sys.byteorder))


def _get_value_type(field, value):
    """
    derive true type from data value
    :param field: fieldname of value
    :param value: value to be evaluated
    :returns: value with appropriate typing
    """

    field2 = field.lower()
    value2 = None

    if value == '':  # empty
        return None

    if field2 == 'date':
        value2 = datetime.strptime(value, '%Y-%m-%d').date()
    elif field2 == 'time':
        hour, minute, second = [int(v) for v in value.split(':')]
        value2 = time(hour, minute, second)
    else:
        try:
            if '.' in value:  # float?
                value2 = float(value)
            elif len(value) > 1 and value.startswith('0'):
                value2 = value
            else:  # int?
                value2 = int(value)
        except ValueError:  # string (default)?
            value2 = value

    return value2


class GRIB(object):
    """GRIB object model"""

    def __init__(self, ioobj=None, version=3, filename=None):
        """
        Initialize a GRIB object

        :param ioobj: file or binary stream
        :param version: GRIB version (default=3)

        :returns: gribby.GRIB instance
        """

        self.ioobj = ioobj
        """file or io object"""

        self.version = version
        """GRIB version"""

        self.filename = filename
        """filename (optional)"""

        self.sections = []
        """sections composing a GRIB message"""

        self.sections = [
            section_0.Section0(),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            section_11.Section11()
        ]

    def _write(self):
        """write to binary IO stream"""

        LOGGER.debug('Writing Section 0')
        self.ioobj.write(pack('<4s', bytes(self.sections[0].signature,
                                           'utf8')))
        self.ioobj.write(pack('<2x'))
        self.ioobj.write(pack('<i',
                         self.sections[0].master_tables_version_number))
        self.ioobj.write(pack('<i', self.sections[0].edition))

        self.ioobj.write(pack('<4s', b''))
        LOGGER.debug('Writing Section 11')
        self.ioobj.write(pack('<4s', bytes(self.sections[11].signature,
                                           'utf8')))

        self.ioobj.seek(0, 2)
        message_length = self.ioobj.tell()

        LOGGER.debug('Writing Section 0 total message length')
        self.ioobj.seek(8)
        self.ioobj.write(pack('>Q', message_length))

    def __repr__(self):
        return '<GRIB (filename: {})>'.format(self.filename)


class InvalidDataError(Exception):
    """Exception stub for format reading errors"""
    pass


def dump(filename):
    """
    Write a GRIB file to disk

    :param filename: filename

    :returns: `bool` of result
    """

    raise NotImplementedError()


def load(filename):
    """
    Parse GRIB data from from file

    :param filename: filename

    :returns: `gribby.GRIB`
    """

    with open(filename, 'rb') as ff:
        return GRIB(ff, filename=filename)


def loads(buf):
    """
    Parse GRIB data from stream

    :param buf: binary representation of GRIB data

    :returns: `gribby.GRIB`
    """

    s = StringIO(buf)
    return GRIB(s)


if __name__ == '__main':
    with open('file_.grib3', 'wb') as fh:
        g = GRIB(fh)
        g._write()

        print(g.__dict__)
