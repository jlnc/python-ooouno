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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content_event_listener import XContentEventListener as XContentEventListener_18ea0ebd
    from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78

class XContent(XInterface_8f010a43):
    """
    specifies a content with a type and an identifier, which is able to manage listeners for events that are related to contents.

    See Also:
        `API XContent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XContent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XContent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XContent'

    @abstractmethod
    def addContentEventListener(self, Listener: 'XContentEventListener_18ea0ebd') -> None:
        """
        adds a listener for content events.
        """
        ...
    @abstractmethod
    def getContentType(self) -> str:
        """
        returns a type string, which is unique for that type of content (e.g.
        
        \"application/vnd.sun.star.hierarchy-folder\").
        """
        ...
    @abstractmethod
    def getIdentifier(self) -> 'XContentIdentifier_edc90d78':
        """
        returns the identifier of the content.
        """
        ...
    @abstractmethod
    def removeContentEventListener(self, Listener: 'XContentEventListener_18ea0ebd') -> None:
        """
        removes a listener for content events.
        """
        ...

__all__ = ['XContent']

