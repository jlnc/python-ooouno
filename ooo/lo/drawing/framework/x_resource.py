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
# Namespace: com.sun.star.drawing.framework
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_resource_id import XResourceId as XResourceId_5be3103d

class XResource(ABC):
    """
    Base interface that provides functionality shared by all resource types of the drawing framework.

    See Also:
        `API XResource <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XResource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.XResource'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XResource'

    @abstractmethod
    def getResourceId(self) -> XResourceId_5be3103d:
        """
        Return an XResourceId object for the called resource.
        
        The returned id unambiguously identifies the resource.
        """
        ...
    @abstractmethod
    def isAnchorOnly(self) -> bool:
        """
        Some resources must not be leafs, i.e.
        
        have to be anchor to at least one other resource. Most panes are examples for this. Views on the other hand are in most cases no anchors. So the typical pane will return TRUE and the typical view will return FALSE.
        
        The return value is used to determine whether a resource has to be deactivated when it has no children, either because none is requested or because none can be created.
        """
        ...

__all__ = ['XResource']


