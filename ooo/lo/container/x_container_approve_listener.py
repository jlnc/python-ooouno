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
    from .container_event import ContainerEvent as ContainerEvent_ea50e70
    from ..util.x_veto import XVeto as XVeto_68e008bc

class XContainerApproveListener(ABC):
    """
    is notified to approve changes which happen to the content of a generic container

    See Also:
        `API XContainerApproveListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XContainerApproveListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.container'
    __ooo_full_ns__: str = 'com.sun.star.container.XContainerApproveListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.container.XContainerApproveListener'

    @abstractmethod
    def approveInsertElement(self, Event: 'ContainerEvent_ea50e70') -> 'XVeto_68e008bc':
        """
        is called for the listener to approve an insertion into the container

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def approveRemoveElement(self, Event: 'ContainerEvent_ea50e70') -> 'XVeto_68e008bc':
        """
        is called for the listener to approve a removal of an element from the container

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def approveReplaceElement(self, Event: 'ContainerEvent_ea50e70') -> 'XVeto_68e008bc':
        """
        is called for the listener to approve a replacement inside the container

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """

__all__ = ['XContainerApproveListener']

