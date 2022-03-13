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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .point import Point as Point_5fb2085e


class EndPopupModeEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an end pop-up mode event.

    See Also:
        `API EndPopupModeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EndPopupModeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.EndPopupModeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.EndPopupModeEvent'
    """Literal Constant ``com.sun.star.awt.EndPopupModeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, bTearoff: typing.Optional[bool] = False, FloatingPosition: typing.Optional[Point_5fb2085e] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            bTearoff (bool, optional): bTearoff value.
            FloatingPosition (Point, optional): FloatingPosition value.
        """

        if isinstance(Source, EndPopupModeEvent):
            oth: EndPopupModeEvent = Source
            self.Source = oth.Source
            self.bTearoff = oth.bTearoff
            self.FloatingPosition = oth.FloatingPosition
            return

        kargs = {
            "Source": Source,
            "bTearoff": bTearoff,
            "FloatingPosition": FloatingPosition,
        }
        if kargs["FloatingPosition"] is UNO_NONE:
            kargs["FloatingPosition"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._b_tearoff = kwargs["bTearoff"]
        self._floating_position = kwargs["FloatingPosition"]
        inst_keys = ('bTearoff', 'FloatingPosition')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def bTearoff(self) -> bool:
        """
        specifies how the pop-up mode was ended TRUE means the window should be teared-off and positioned at FloatingPosition FALSE means the window was closed
        """
        return self._b_tearoff
    
    @bTearoff.setter
    def bTearoff(self, value: bool) -> None:
        self._b_tearoff = value

    @property
    def FloatingPosition(self) -> Point_5fb2085e:
        """
        specifies the new position of the floating window in frame coordinates if bTearoff is TRUE
        """
        return self._floating_position
    
    @FloatingPosition.setter
    def FloatingPosition(self, value: Point_5fb2085e) -> None:
        self._floating_position = value


__all__ = ['EndPopupModeEvent']
