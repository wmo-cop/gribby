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

LOGGER = logging.getLogger(__name__)

# from https://gist.github.com/JonathonReinhart/b6f355f13021cd8ec5d0101e0e6675b2  # noqa


class StructHelper(object):
    def __get_value_str(self, name, fmt='{}'):
        val = getattr(self, name)
        if isinstance(val, ctypes.Array):
            val = list(val)
        return fmt.format(val)

    def __str__(self):
        result = '{}:\n'.format(self.__class__.__name__)
        maxname = max(len(name) for name, type_ in self._fields_)
        for name, type_ in self._fields_:
            # value = getattr(self, name)
            result += ' {name:<{width}}: {value}\n'.format(
                    name=name,
                    width=maxname,
                    value=self.__get_value_str(name),
                    )
        return result

    def __repr__(self):
        return '{name}({fields})'.format(
                name=self.__class__.__name__,
                fields=', '.join(
                    '{}={}'.format(name,self.__get_value_str(name, '{!r}')) for name, _ in self._fields_)  # noqa
                )

    @classmethod
    def _typeof(cls, field):
        """Get the type of a field
        Example: A._typeof(A.fld)
        Inspired by stackoverflow.com/a/6061483
        """
        for name, type_ in cls._fields_:
            if getattr(cls, name) is field:
                return type_
        raise KeyError

    @classmethod
    def read_from(cls, f):
        result = cls()
        if f.readinto(result) != ctypes.sizeof(cls):
            raise EOFError
        return result

    def get_bytes(self):
        """Get raw byte string of this structure
        ctypes.Structure implements the buffer interface, so it can be used
        directly anywhere the buffer interface is implemented.
        https://stackoverflow.com/q/1825715
        """

        return bytes(self)
