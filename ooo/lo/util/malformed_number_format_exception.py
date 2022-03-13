# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class MalformedNumberFormatException(Exception_85530a09):
    """
    Exception Class

    is thrown when a NumberFormat string is syntactically incorrect.

    See Also:
        `API MalformedNumberFormatException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1util_1_1MalformedNumberFormatException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.MalformedNumberFormatException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.util.MalformedNumberFormatException'
    __pyunostruct__: str = 'com.sun.star.util.MalformedNumberFormatException'

    typeName: str = 'com.sun.star.util.MalformedNumberFormatException'
    """Literal Constant ``com.sun.star.util.MalformedNumberFormatException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, CheckPos: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            CheckPos (int, optional): CheckPos value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "CheckPos": CheckPos,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._check_pos = kwargs["CheckPos"]
        inst_keys = ('CheckPos',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def CheckPos(self) -> int:
        """
        contains the character position in the string where the malformation begins.
        """
        return self._check_pos
    
    @CheckPos.setter
    def CheckPos(self, value: int) -> None:
        self._check_pos = value


