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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractproperty
from .base_frame import BaseFrame as BaseFrame_8f020a33
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
    from ..drawing.point_sequence_sequence import PointSequenceSequence as PointSequenceSequence_5c591070
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from .graphic_crop import GraphicCrop as GraphicCrop_a58e0b1f
    from com.sun.star.drawing.ColorMode import ColorModeProto  # type: ignore

class TextGraphicObject(BaseFrame_8f020a33):
    """
    Service Class

    specifies a graphic which can be embedded in Text.

    See Also:
        `API TextGraphicObject <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextGraphicObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextGraphicObject'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ActualSize(self) -> Size_576707ef:
        """
        contains the original size of the bitmap in the graphic object.
        """
        ...

    @abstractproperty
    def AdjustBlue(self) -> int:
        """
        changes the display of the blue color channel.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def AdjustContrast(self) -> int:
        """
        changes the display of contrast.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def AdjustGreen(self) -> int:
        """
        changes the display of the green color channel.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def AdjustLuminance(self) -> int:
        """
        changes the display of the luminance.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def AdjustRed(self) -> int:
        """
        changes the display of the red color channel.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def ContentProtected(self) -> bool:
        """
        determines if the content is protected against changes from the user interface.
        """
        ...

    @abstractproperty
    def ContourOutside(self) -> bool:
        """
        the text flows only around the contour of the object.
        """
        ...

    @abstractproperty
    def ContourPolyPolygon(self) -> PointSequenceSequence_5c591070:
        """
        contains the contour of the object as PolyPolygon.
        """
        ...

    @abstractproperty
    def Gamma(self) -> float:
        """
        determines the gamma value of the graphic.
        """
        ...

    @abstractproperty
    def Graphic(self) -> XGraphic_a4da0afc:
        """
        contains the background graphic of the object.
        """
        ...

    @abstractproperty
    def GraphicColorMode(self) -> ColorModeProto:
        """
        contains the ColorMode as com.sun.star.drawing.ColorMode.
        """
        ...

    @abstractproperty
    def GraphicCrop(self) -> GraphicCrop_a58e0b1f:
        """
        contains the cropping of the object.
        """
        ...

    @abstractproperty
    def GraphicFilter(self) -> str:
        """
        contains the name of the filter of the background graphic of the object.
        """
        ...

    @abstractproperty
    def GraphicIsInverted(self) -> bool:
        """
        determines if the graphic is display in inverted colors.
        
        It contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def GraphicURL(self) -> str:
        """
        contains the URL of the background graphic of the object
        
        Note the new behaviour since it was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When a URL is set, then it will load the image and set the Graphic property.
        """
        ...

    @abstractproperty
    def HoriMirroredOnEvenPages(self) -> bool:
        """
        determines if the object is horizontally mirrored on even pages.
        """
        ...

    @abstractproperty
    def HoriMirroredOnOddPages(self) -> bool:
        """
        determines if the object is horizontally mirrored on odd pages.
        """
        ...

    @abstractproperty
    def ImageMap(self) -> XIndexContainer_1c040ebe:
        """
        returns the client-side image map if one is assigned to the object.
        """
        ...

    @abstractproperty
    def SurroundContour(self) -> bool:
        """
        determines if the text wraps around the contour of the object.
        """
        ...

    @abstractproperty
    def Transparency(self) -> int:
        """
        contains percentage values between -100 and +100.
        """
        ...

    @abstractproperty
    def VertMirrored(self) -> bool:
        """
        determines if the object is mirrored vertically.
        """
        ...


__all__ = ['TextGraphicObject']