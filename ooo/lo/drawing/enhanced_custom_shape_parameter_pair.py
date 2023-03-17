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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter_d6171317


class EnhancedCustomShapeParameterPair(object):
    """
    Struct Class

    specifies the coordinates used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeParameterPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameterPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeParameterPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeParameterPair'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeParameterPair``"""

    def __init__(self, First: typing.Optional[EnhancedCustomShapeParameter_d6171317] = UNO_NONE, Second: typing.Optional[EnhancedCustomShapeParameter_d6171317] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            First (EnhancedCustomShapeParameter, optional): First value.
            Second (EnhancedCustomShapeParameter, optional): Second value.
        """
        super().__init__()

        if isinstance(First, EnhancedCustomShapeParameterPair):
            oth: EnhancedCustomShapeParameterPair = First
            self.First = oth.First
            self.Second = oth.Second
            return

        kargs = {
            "First": First,
            "Second": Second,
        }
        if kargs["First"] is UNO_NONE:
            kargs["First"] = None
        if kargs["Second"] is UNO_NONE:
            kargs["Second"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._first = kwargs["First"]
        self._second = kwargs["Second"]


    @property
    def First(self) -> EnhancedCustomShapeParameter_d6171317:
        return self._first
    
    @First.setter
    def First(self, value: EnhancedCustomShapeParameter_d6171317) -> None:
        self._first = value

    @property
    def Second(self) -> EnhancedCustomShapeParameter_d6171317:
        return self._second
    
    @Second.setter
    def Second(self, value: EnhancedCustomShapeParameter_d6171317) -> None:
        self._second = value


__all__ = ['EnhancedCustomShapeParameterPair']
