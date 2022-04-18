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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XRecentFunctions(XInterface_8f010a43):
    """
    provides access to a list of recently used functions.

    See Also:
        `API XRecentFunctions <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XRecentFunctions.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XRecentFunctions'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XRecentFunctions'

    @abstractmethod
    def getMaxRecentFunctions(self) -> int:
        """
        returns the maximum number of entries that will be stored as recently used functions.
        """
    @abstractmethod
    def getRecentFunctionIds(self) -> 'typing.Tuple[int, ...]':
        """
        returns a sequence of those functions that were most recently used.
        
        The functions are represented by their identifiers.
        """
    @abstractmethod
    def setRecentFunctionIds(self, aRecentFunctionIds: 'typing.Tuple[int, ...]') -> None:
        """
        sets the list of those functions that were most recently used.
        
        The functions are represented by their identifiers.
        """

__all__ = ['XRecentFunctions']

