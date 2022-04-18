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
# Namespace: com.sun.star.xml.csax
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xml_attribute import XMLAttribute as XMLAttribute_df0f0cdb

class XCompressedDocumentHandler(XInterface_8f010a43):
    """
    A compressed XDocumentHandler interface.
    
    All methods in this interface have the same function with methods in the XDocumentHandler interface.
    
    Because there is no interface parameter in these methods, so using this interface to transfer SAX event is thought to have better performance than using the XDocumentHandler interface, in case of when UNO C++/Java bridge is involved.

    See Also:
        `API XCompressedDocumentHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1csax_1_1XCompressedDocumentHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.csax'
    __ooo_full_ns__: str = 'com.sun.star.xml.csax.XCompressedDocumentHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.csax.XCompressedDocumentHandler'

    @abstractmethod
    def compressedCharacters(self, aChars: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedEndDocument(self) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedEndElement(self, aName: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedIgnorableWhitespace(self, aWhitespaces: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedProcessingInstruction(self, aTarget: str, aData: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedSetDocumentLocator(self, columnNumber: int, lineNumber: int, publicId: str, systemId: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedStartDocument(self) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    @abstractmethod
    def compressedStartElement(self, aName: str, aAttributes: 'typing.Tuple[XMLAttribute_df0f0cdb, ...]') -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """

__all__ = ['XCompressedDocumentHandler']

