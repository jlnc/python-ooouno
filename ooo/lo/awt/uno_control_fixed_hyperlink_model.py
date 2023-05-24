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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from abc import abstractproperty
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto

class UnoControlFixedHyperlinkModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlFixedHyperlink.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlFixedHyperlinkModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlFixedHyperlinkModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlFixedHyperlinkModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """
        ...

    @abstractproperty
    def BackgroundColor(self) -> Color_68e908c5:
        """
        specifies the background color (RGB) of the control.
        """
        ...

    @abstractproperty
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...

    @abstractproperty
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @abstractproperty
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...

    @abstractproperty
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...

    @abstractproperty
    def MultiLine(self) -> bool:
        """
        specifies that the text may be displayed on more than one line.
        """
        ...

    @abstractproperty
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...

    @abstractproperty
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @abstractproperty
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @abstractproperty
    def URL(self) -> str:
        """
        specifies the URL.
        """
        ...

    @abstractproperty
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """
        ...


__all__ = ['UnoControlFixedHyperlinkModel']

