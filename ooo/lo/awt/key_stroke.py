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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class KeyStroke(object):
    """
    Struct Class

    Describes a key stroke for hotkeys etc.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API KeyStroke <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1KeyStroke.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.KeyStroke'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.KeyStroke'
    """Literal Constant ``com.sun.star.awt.KeyStroke``"""

    def __init__(self, Modifiers: typing.Optional[int] = 0, KeyCode: typing.Optional[int] = 0, KeyChar: typing.Optional[str] = '\u0000', KeyFunc: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Modifiers (int, optional): Modifiers value.
            KeyCode (int, optional): KeyCode value.
            KeyChar (str, optional): KeyChar value.
            KeyFunc (int, optional): KeyFunc value.
        """
        super().__init__()

        if isinstance(Modifiers, KeyStroke):
            oth: KeyStroke = Modifiers
            self.Modifiers = oth.Modifiers
            self.KeyCode = oth.KeyCode
            self.KeyChar = oth.KeyChar
            self.KeyFunc = oth.KeyFunc
            return

        kargs = {
            "Modifiers": Modifiers,
            "KeyCode": KeyCode,
            "KeyChar": KeyChar,
            "KeyFunc": KeyFunc,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._modifiers = kwargs["Modifiers"]
        self._key_code = kwargs["KeyCode"]
        self._key_char = kwargs["KeyChar"]
        self._key_func = kwargs["KeyFunc"]


    @property
    def Modifiers(self) -> int:
        """
        contains the modifier keys which were pressed while the event occurred.
        
        Zero or more constants from the group com.sun.star.awt.KeyModifier.
        """
        return self._modifiers
    
    @Modifiers.setter
    def Modifiers(self, value: int) -> None:
        self._modifiers = value

    @property
    def KeyCode(self) -> int:
        """
        contains the integer code representing the key of the event.
        
        This is a constant from the constant group com.sun.star.awt.Key.
        """
        return self._key_code
    
    @KeyCode.setter
    def KeyCode(self, value: int) -> None:
        self._key_code = value

    @property
    def KeyChar(self) -> str:
        """
        contains the Unicode character generated by this event or 0.
        """
        return self._key_char
    
    @KeyChar.setter
    def KeyChar(self, value: str) -> None:
        self._key_char = value

    @property
    def KeyFunc(self) -> int:
        """
        contains the function type of the key event.
        
        This is a constant from the constant group com.sun.star.awt.KeyFunction.
        """
        return self._key_func
    
    @KeyFunc.setter
    def KeyFunc(self, value: int) -> None:
        self._key_func = value


__all__ = ['KeyStroke']
