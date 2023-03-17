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
# Namespace: com.sun.star.style
from abc import abstractmethod
from ..container.x_named import XNamed as XNamed_a6520b08

class XStyle(XNamed_a6520b08):
    """
    specifies a template for a style (aka style sheet).

    See Also:
        `API XStyle <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.XStyle'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.style.XStyle'

    @abstractmethod
    def getParentStyle(self) -> str:
        """
        """
        ...
    @abstractmethod
    def isInUse(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def isUserDefined(self) -> bool:
        """
        identifies a style as defined by the user.
        """
        ...
    @abstractmethod
    def setParentStyle(self, aParentStyle: str) -> None:
        """
        sets the name of the parent style.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XStyle']

