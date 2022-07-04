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
# Namespace: com.sun.star.datatransfer.dnd
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .drop_target_drag_enter_event import DropTargetDragEnterEvent as DropTargetDragEnterEvent_3a2d14e5
    from .drop_target_drag_event import DropTargetDragEvent as DropTargetDragEvent_d60612e7
    from .drop_target_drop_event import DropTargetDropEvent as DropTargetDropEvent_d69e12fe
    from .drop_target_event import DropTargetEvent as DropTargetEvent_8d651169

class XDropTargetListener(XEventListener_c7230c4a):
    """
    This interface is the callback interface used by the drop target object to provide notification of Drag and Drop operations that involve the subject drop target.
    
    Methods of this interface may be implemented to provide \"drag under\" visual feedback to the user throughout the Drag and Drop operation.

    See Also:
        `API XDropTargetListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDropTargetListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.XDropTargetListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.XDropTargetListener'

    @abstractmethod
    def dragEnter(self, dtdee: 'DropTargetDragEnterEvent_3a2d14e5') -> None:
        """
        Called when a drag operation has encountered the drop target.
        """
        ...
    @abstractmethod
    def dragExit(self, dte: 'DropTargetEvent_8d651169') -> None:
        """
        The drag operation has departed the drop target without dropping.
        """
        ...
    @abstractmethod
    def dragOver(self, dtde: 'DropTargetDragEvent_d60612e7') -> None:
        """
        Called when a drag operation is ongoing on the drop target.
        """
        ...
    @abstractmethod
    def drop(self, dtde: 'DropTargetDropEvent_d69e12fe') -> None:
        """
        The drag operation has terminated with a drop on this drop target.
        
        NOTE: The implementation has to wait until the method XDropTargetDropContext.dropComplete() is called before releasing the data for the drop operation. This should occur before returning from drop in a normal flow of operation. Also, the implementor of XDropTargetListener should not assume the DropTargetDropEvent to be meaningful after returning from the XDropTargetListener.drop() method.
        """
        ...
    @abstractmethod
    def dropActionChanged(self, dtde: 'DropTargetDragEvent_d60612e7') -> None:
        """
        Called when the user has modified the drop gesture.
        """
        ...

__all__ = ['XDropTargetListener']

