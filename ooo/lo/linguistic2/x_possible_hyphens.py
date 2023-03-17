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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.linguistic2
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XPossibleHyphens(XInterface_8f010a43):
    """
    Gives information about a word's possible hyphenation points.
    
    Example: In German pre-spelling-reform you may have the following: getWord: Dampfschiffahrt getPossibleHyphens: Dampf=schiff=fahrt getOrigHyphensPositions: 4, 9 That is \"Dampfschiffahrt\" can be hyphenated after the \"pf\" (4) and between the double \"ff\" (9). And if you are going to hyphenate it at position 9 you will get an additional \"f\" before the hyphen character.

    See Also:
        `API XPossibleHyphens <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XPossibleHyphens.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XPossibleHyphens'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XPossibleHyphens'

    @abstractmethod
    def getHyphenationPositions(self) -> uno.ByteSequence:
        """
        """
        ...
    @abstractmethod
    def getLocale(self) -> 'Locale_70d308fa':
        """
        """
        ...
    @abstractmethod
    def getPossibleHyphens(self) -> str:
        """
        """
        ...
    @abstractmethod
    def getWord(self) -> str:
        """
        """
        ...

__all__ = ['XPossibleHyphens']

