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
# Namespace: com.sun.star.mail
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XConnectionListener(XEventListener_c7230c4a):
    """
    The listener interface for connection events.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XConnectionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mail_1_1XConnectionListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mail'
    __ooo_full_ns__: str = 'com.sun.star.mail.XConnectionListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.mail.XConnectionListener'

    @abstractmethod
    def connected(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        Invoked when the connection to the mail server is established.
        """
        ...
    @abstractmethod
    def disconnected(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        Invoked when the connection to the mail server is closed.
        """
        ...

__all__ = ['XConnectionListener']

