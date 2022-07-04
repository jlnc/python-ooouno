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
# Namespace: com.sun.star.container
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_container_approve_listener import XContainerApproveListener as XContainerApproveListener_c6d812e9

class XContainerApproveBroadcaster(ABC):
    """
    allows containers to implement a vetoing mechanism for insertion, removal, and replacement of their elements.

    See Also:
        `API XContainerApproveBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XContainerApproveBroadcaster.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.XContainerApproveBroadcaster'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.container.XContainerApproveBroadcaster'

    @abstractmethod
    def addContainerApproveListener(self, Listener: 'XContainerApproveListener_c6d812e9') -> None:
        """
        adds a listener which can veto changes in the container's content
        """
        ...
    @abstractmethod
    def removeContainerApproveListener(self, Listener: 'XContainerApproveListener_c6d812e9') -> None:
        """
        removes a previously added listener
        """
        ...

__all__ = ['XContainerApproveBroadcaster']

