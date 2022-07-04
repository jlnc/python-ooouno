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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..table.cell_hori_justify import CellHoriJustify as CellHoriJustify_e0470d10
    from ..table.cell_orientation import CellOrientation as CellOrientation_e0e40d1c
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..table.table_border import TableBorder as TableBorder_aedf0b56
    from ..table.table_border2 import TableBorder2 as TableBorder2_ba670b88
    from ..util.color import Color as Color_68e908c5

class TableAutoFormatField(XPropertySet_bc180bfa):
    """
    Service Class

    represents a field in an AutoFormat.
    
    A field contains all cell properties for a specific position in an AutoFormat.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TableAutoFormatField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1TableAutoFormatField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TableAutoFormatField'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CellBackColor(self) -> 'Color_68e908c5':
        """
        contains the cell background color.
        """
        ...

    @abstractproperty
    def CharColor(self) -> 'Color_68e908c5':
        """
        contains the value of the text color.
        """
        ...

    @abstractproperty
    def CharContoured(self) -> bool:
        """
        is TRUE if the characters are contoured.
        """
        ...

    @abstractproperty
    def CharCrossedOut(self) -> bool:
        """
        is TRUE if the characters are crossed out.
        """
        ...

    @abstractproperty
    def CharFontCharSet(self) -> str:
        """
        contains the value of the character set of the western font.
        """
        ...

    @abstractproperty
    def CharFontCharSetAsian(self) -> str:
        """
        contains the value of the character set of the Asian font.
        """
        ...

    @abstractproperty
    def CharFontCharSetComplex(self) -> str:
        """
        contains the value of the character set of the complex font.
        """
        ...

    @abstractproperty
    def CharFontFamily(self) -> str:
        """
        contains the value of the western font family.
        """
        ...

    @abstractproperty
    def CharFontFamilyAsian(self) -> str:
        """
        contains the value of the Asian font family.
        """
        ...

    @abstractproperty
    def CharFontFamilyComplex(self) -> str:
        """
        contains the value of the complex font family.
        """
        ...

    @abstractproperty
    def CharFontName(self) -> str:
        """
        specifies the name of the western font.
        """
        ...

    @abstractproperty
    def CharFontNameAsian(self) -> str:
        """
        specifies the name of the Asian font.
        """
        ...

    @abstractproperty
    def CharFontNameComplex(self) -> str:
        """
        specifies the name of the complex font.
        """
        ...

    @abstractproperty
    def CharFontPitch(self) -> str:
        """
        contains the value of the pitch of the western font.
        """
        ...

    @abstractproperty
    def CharFontPitchAsian(self) -> str:
        """
        contains the value of the pitch of the Asian font.
        """
        ...

    @abstractproperty
    def CharFontPitchComplex(self) -> str:
        """
        contains the value of the pitch of the complex font.
        """
        ...

    @abstractproperty
    def CharFontStyleName(self) -> str:
        """
        specifies the name of the western font style.
        """
        ...

    @abstractproperty
    def CharFontStyleNameAsian(self) -> str:
        """
        specifies the name of the Asian font style.
        """
        ...

    @abstractproperty
    def CharFontStyleNameComplex(self) -> str:
        """
        specifies the name of the complex font style.
        """
        ...

    @abstractproperty
    def CharHeight(self) -> float:
        """
        contains the height of characters of the western font in point.
        """
        ...

    @abstractproperty
    def CharHeightAsian(self) -> float:
        """
        contains the height of characters of the Asian font in point.
        """
        ...

    @abstractproperty
    def CharHeightComplex(self) -> float:
        """
        contains the height of characters of the complex font in point.
        """
        ...

    @abstractproperty
    def CharPosture(self) -> 'FontSlant_849509ed':
        """
        contains the value of the posture of characters of the western font.
        """
        ...

    @abstractproperty
    def CharPostureAsian(self) -> 'FontSlant_849509ed':
        """
        contains the value of the posture of characters of the Asian font.
        """
        ...

    @abstractproperty
    def CharPostureComplex(self) -> 'FontSlant_849509ed':
        """
        contains the value of the posture of characters of the complex font.
        """
        ...

    @abstractproperty
    def CharShadowed(self) -> bool:
        """
        is TRUE if the characters are shadowed.
        """
        ...

    @abstractproperty
    def CharUnderline(self) -> int:
        """
        contains the value for the character underline.
        """
        ...

    @abstractproperty
    def CharWeight(self) -> float:
        """
        contains the value for the weight of characters of the western font.
        """
        ...

    @abstractproperty
    def CharWeightAsian(self) -> float:
        """
        contains the value for the weight of characters of the Asian font.
        """
        ...

    @abstractproperty
    def CharWeightComplex(self) -> float:
        """
        contains the value for the weight of characters of the complex font.
        """
        ...

    @abstractproperty
    def HoriJustify(self) -> 'CellHoriJustify_e0470d10':
        """
        specifies the horizontal alignment of the cell contents.
        """
        ...

    @abstractproperty
    def IsCellBackgroundTransparent(self) -> bool:
        """
        is TRUE if the cell background is transparent.
        
        In this case the TableAutoFormatField.CellBackColor value is not used.
        """
        ...

    @abstractproperty
    def IsTextWrapped(self) -> bool:
        """
        is TRUE if text breaks automatically at cell borders.
        """
        ...

    @abstractproperty
    def Orientation(self) -> 'CellOrientation_e0e40d1c':
        """
        contains the orientation of the cell contents (i.e.
        
        top-to-bottom or stacked).
        """
        ...

    @abstractproperty
    def ParaBottomMargin(self) -> int:
        """
        contains the margin between cell contents and bottom border (in 1/100 mm).
        """
        ...

    @abstractproperty
    def ParaLeftMargin(self) -> int:
        """
        contains the margin between cell contents and left border (in 1/100 mm).
        """
        ...

    @abstractproperty
    def ParaRightMargin(self) -> int:
        """
        contains the margin between cell contents and right border (in 1/100 mm).
        """
        ...

    @abstractproperty
    def ParaTopMargin(self) -> int:
        """
        contains the margin between cell contents and top border (in 1/100 mm).
        """
        ...

    @abstractproperty
    def RotateAngle(self) -> int:
        """
        contains the rotation angle of the cell contents.
        """
        ...

    @abstractproperty
    def RotateReference(self) -> int:
        """
        contains the reference edge of the cell rotation.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
        ...

    @abstractproperty
    def ShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        contains a description of the shadow.
        """
        ...

    @abstractproperty
    def TableBorder(self) -> 'TableBorder_aedf0b56':
        """
        property containing a description of the cell border.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @abstractproperty
    def TableBorder2(self) -> 'TableBorder2_ba670b88':
        """
        property containing a description of the cell border.
        
        Preferred over com.sun.star.table.TableBorder TableBorder.
        
        **since**
        
            LibreOffice 3.6
        """
        ...

    @abstractproperty
    def VertJustify(self) -> int:
        """
        specifies the vertical alignment of the cell contents.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
        ...



__all__ = ['TableAutoFormatField']

