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
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..awt.mouse_event import MouseEvent as MouseEvent_8f430a5f
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XShapeEventListener(XEventListener_c7230c4a):
    """
    Listener interface to receive shape-specific events.
    
    **since**
    
        OOo 2.4

    See Also:
        `API XShapeEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XShapeEventListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.XShapeEventListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.presentation.XShapeEventListener'

    @abstractmethod
    def click(self, xShape: XShape_8fd00a3d, aOriginalEvent: MouseEvent_8f430a5f) -> None:
        """
        Notify a clicked shape.
        
        This method notifies the listener that a shape was clicked.
        """
        ...

__all__ = ['XShapeEventListener']

