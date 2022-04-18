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
# Namespace: com.sun.star.drawing.framework
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ...awt.point import Point as Point_5fb2085e
    from ...awt.rectangle import Rectangle as Rectangle_84b109e9
    from .border_type import BorderType as BorderType_4b7f0ff0
    from ...rendering.x_canvas import XCanvas as XCanvas_b19b0b7a

class XPaneBorderPainter(ABC):
    """
    Paint the border around a rectangular region, typically a pane.
    
    Calling objects have to be able to derive inner bounding boxes of the border from the outer ones and inner ones from outer ones. This conversion and the painting of the border involves three rectangles. The inner and outer bounding box of the border. This is a logical bounding box which the paint methods may paint over. The center box is the third rectangle. This is the actual border between outer and inner background color or bitmap and it is used for placing the bitmaps that are used paint the border. The inner sides and corners are places relative to this center box, i.e. when not further offsets are given then the upper left corner bitmap is painted with its lower right at the upper left of the center box.

    See Also:
        `API XPaneBorderPainter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XPaneBorderPainter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.XPaneBorderPainter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XPaneBorderPainter'

    @abstractmethod
    def addBorder(self, sPaneBorderStyleName: str, aRectangle: 'Rectangle_84b109e9', eBorderType: 'BorderType_4b7f0ff0') -> 'Rectangle_84b109e9':
        """
        Enlarge the given rectangle by the size of the specified part of the border.
        
        This method can be used to convert an inner bounding box into the center box or the outer bounding box.
        """
    @abstractmethod
    def getCalloutOffset(self, sPaneBorderStyleName: str) -> 'Point_5fb2085e':
        """
        Return the offset of a call out anchor with respect to the outer border.
        
        This value is used when the call out is realized by a fixed bitmap in order to determine the size and/or location of the outer border for a given call out.
        """
    @abstractmethod
    def paintBorder(self, sPaneBorderStyleName: str, xCanvas: 'XCanvas_b19b0b7a', aOuterBorderRectangle: 'Rectangle_84b109e9', aRepaintArea: 'Rectangle_84b109e9', sTitle: str) -> None:
        """
        Paint the border around a pane.
        """
    @abstractmethod
    def paintBorderWithCallout(self, sPaneBorderStyleName: str, xCanvas: 'XCanvas_b19b0b7a', aOuterBorderRectangle: 'Rectangle_84b109e9', aRepaintArea: 'Rectangle_84b109e9', sTitle: str, aCalloutAnchor: 'Point_5fb2085e') -> None:
        """
        Paint the border around a pane where the border includes a call out that is anchored at the given point.
        
        Most arguments have the same meaning as in the paintBorder().
        """
    @abstractmethod
    def removeBorder(self, sPaneBorderStyleName: str, aRectangle: 'Rectangle_84b109e9', eBorderType: 'BorderType_4b7f0ff0') -> 'Rectangle_84b109e9':
        """
        Shrink the given rectangle by the size of the specified part of the border.
        
        This method can be used to convert an outer bounding box into the center box or the inner bounding box.
        """

__all__ = ['XPaneBorderPainter']

