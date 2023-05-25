# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.xml.xpath
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..dom.x_node_list import XNodeList as XNodeList_ae540b41
    from com.sun.star.xml.xpath.XPathObjectType import XPathObjectTypeProto  # type: ignore

class XXPathObject(XInterface_8f010a43):
    """

    See Also:
        `API XXPathObject <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1xpath_1_1XXPathObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.xpath'
    __ooo_full_ns__: str = 'com.sun.star.xml.xpath.XXPathObject'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.xpath.XXPathObject'

    @abstractmethod
    def getBoolean(self) -> bool:
        """
        get value of a boolean object
        """
        ...
    @abstractmethod
    def getByte(self) -> int:
        """
        get number as byte
        """
        ...
    @abstractmethod
    def getDouble(self) -> float:
        """
        get number as double
        """
        ...
    @abstractmethod
    def getFloat(self) -> float:
        """
        get number as float
        """
        ...
    @abstractmethod
    def getHyper(self) -> int:
        """
        get number as hyper
        """
        ...
    @abstractmethod
    def getLong(self) -> int:
        """
        get number as long
        """
        ...
    @abstractmethod
    def getNodeList(self) -> XNodeList_ae540b41:
        """
        get the nodes from a node list type object
        """
        ...
    @abstractmethod
    def getObjectType(self) -> XPathObjectTypeProto:
        """
        get object type
        """
        ...
    @abstractmethod
    def getShort(self) -> int:
        """
        get number as short
        """
        ...
    @abstractmethod
    def getString(self) -> str:
        """
        get string value
        """
        ...

__all__ = ['XXPathObject']
