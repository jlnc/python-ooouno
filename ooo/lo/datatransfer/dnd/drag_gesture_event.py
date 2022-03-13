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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_drag_source import XDragSource as XDragSource_49900fb2


class DragGestureEvent(EventObject_a3d70b03):
    """
    Struct Class

    A DragGestureEvent is passed to the method XDragGestureListener.dragGestureRecognized() when a particular XDragGestureRecognizer detects that a platform dependent drag initiating gesture has occurred on the component that it is tracking.

    See Also:
        `API DragGestureEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragGestureEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DragGestureEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DragGestureEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DragGestureEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, DragAction: typing.Optional[int] = 0, DragOriginX: typing.Optional[int] = 0, DragOriginY: typing.Optional[int] = 0, DragSource: typing.Optional[XDragSource_49900fb2] = None, Event: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DragAction (int, optional): DragAction value.
            DragOriginX (int, optional): DragOriginX value.
            DragOriginY (int, optional): DragOriginY value.
            DragSource (XDragSource, optional): DragSource value.
            Event (object, optional): Event value.
        """

        if isinstance(Source, DragGestureEvent):
            oth: DragGestureEvent = Source
            self.Source = oth.Source
            self.DragAction = oth.DragAction
            self.DragOriginX = oth.DragOriginX
            self.DragOriginY = oth.DragOriginY
            self.DragSource = oth.DragSource
            self.Event = oth.Event
            return

        kargs = {
            "Source": Source,
            "DragAction": DragAction,
            "DragOriginX": DragOriginX,
            "DragOriginY": DragOriginY,
            "DragSource": DragSource,
            "Event": Event,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._drag_action = kwargs["DragAction"]
        self._drag_origin_x = kwargs["DragOriginX"]
        self._drag_origin_y = kwargs["DragOriginY"]
        self._drag_source = kwargs["DragSource"]
        self._event = kwargs["Event"]
        inst_keys = ('DragAction', 'DragOriginX', 'DragOriginY', 'DragSource', 'Event')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def DragAction(self) -> int:
        """
        The action selected by the user.
        
        Different constants may be combined using a logical OR.
        
        It's further possible to combine the ACTION_DEFAULT with one of the other actions defined in com.sun.star.datatransfer.dnd.DNDConstants. This means the user did not press any key during the Drag and Drop operation and the action that was combined with ACTION_DEFAULT is the system default action.
        """
        return self._drag_action
    
    @DragAction.setter
    def DragAction(self, value: int) -> None:
        self._drag_action = value

    @property
    def DragOriginX(self) -> int:
        """
        The x coordinate where the drag originated in component coordinates.
        """
        return self._drag_origin_x
    
    @DragOriginX.setter
    def DragOriginX(self, value: int) -> None:
        self._drag_origin_x = value

    @property
    def DragOriginY(self) -> int:
        """
        The y coordinate where the drag originated in component coordinates.
        """
        return self._drag_origin_y
    
    @DragOriginY.setter
    def DragOriginY(self, value: int) -> None:
        self._drag_origin_y = value

    @property
    def DragSource(self) -> XDragSource_49900fb2:
        """
        The DragSource associated with this drag action.
        """
        return self._drag_source
    
    @DragSource.setter
    def DragSource(self, value: XDragSource_49900fb2) -> None:
        self._drag_source = value

    @property
    def Event(self) -> object:
        """
        The last event comprising the gesture.
        
        The initial trigger event will presumably be a com.sun.star.awt.MouseEvent event. If it is not, the implementation should either react accordingly or presume that the left mouse button was clicked.
        """
        return self._event
    
    @Event.setter
    def Event(self, value: object) -> None:
        self._event = value


__all__ = ['DragGestureEvent']
