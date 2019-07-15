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
from io import StringIO
import logging
import sys

__version__ = '0.1.0'

LOGGER = logging.getLogger(__name__)

LOGGER.debug('System byte order: {}'.format(sys.byteorder))


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

        self.sections = []

    def validate(self):
        """
        Validates a `gribby.GRIB` object

        :raises: `gribby.InvalidDataError`

        :returns: void
        """

        if len(self.sections) < 12:
            raise InvalidDataError('not enough sections')

    def write(self):
        """
        Write GRIB data to file handle or BytesIO

        :returns: void
        """

        total_length = 0

        if self.ioobj is None:
            msg = 'file handle required'
            LOGGER.error(msg)
            raise RuntimeError(msg)

        LOGGER.debug('calculating total length')
        for section in self.sections:
            LOGGER.debug(section)
            total_length += ctypes.sizeof(section)

        LOGGER.debug('total length: {}'.format(total_length))
        self.sections[0].length = total_length

        for counter, section in enumerate(self.sections):
            if 0 < counter < 12:
                section.number_of_section = counter
            LOGGER.debug('Writing Section {}'.format(counter))
            self.ioobj.write(section.get_bytes())

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
