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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .enhanced_custom_shape_parameter_pair import EnhancedCustomShapeParameterPair as EnhancedCustomShapeParameterPair_262914a3


class EnhancedCustomShapeTextFrame(object):
    """
    Struct Class

    specifies the coordinates used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeTextFrame <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeTextFrame.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeTextFrame'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeTextFrame'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeTextFrame``"""

    def __init__(self, TopLeft: typing.Optional[EnhancedCustomShapeParameterPair_262914a3] = UNO_NONE, BottomRight: typing.Optional[EnhancedCustomShapeParameterPair_262914a3] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            TopLeft (EnhancedCustomShapeParameterPair, optional): TopLeft value.
            BottomRight (EnhancedCustomShapeParameterPair, optional): BottomRight value.
        """
        super().__init__()

        if isinstance(TopLeft, EnhancedCustomShapeTextFrame):
            oth: EnhancedCustomShapeTextFrame = TopLeft
            self.TopLeft = oth.TopLeft
            self.BottomRight = oth.BottomRight
            return

        kargs = {
            "TopLeft": TopLeft,
            "BottomRight": BottomRight,
        }
        if kargs["TopLeft"] is UNO_NONE:
            kargs["TopLeft"] = None
        if kargs["BottomRight"] is UNO_NONE:
            kargs["BottomRight"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._top_left = kwargs["TopLeft"]
        self._bottom_right = kwargs["BottomRight"]


    @property
    def TopLeft(self) -> EnhancedCustomShapeParameterPair_262914a3:
        return self._top_left
    
    @TopLeft.setter
    def TopLeft(self, value: EnhancedCustomShapeParameterPair_262914a3) -> None:
        self._top_left = value

    @property
    def BottomRight(self) -> EnhancedCustomShapeParameterPair_262914a3:
        return self._bottom_right
    
    @BottomRight.setter
    def BottomRight(self, value: EnhancedCustomShapeParameterPair_262914a3) -> None:
        self._bottom_right = value


__all__ = ['EnhancedCustomShapeTextFrame']
