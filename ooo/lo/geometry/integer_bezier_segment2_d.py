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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class IntegerBezierSegment2D(object):
    """
    Struct Class

    This structure contains the relevant data for a cubic Bezier curve.
    
    The data is stored integer-valued. The last point of the segment is taken from the first point of the following segment, and thus not included herein. That is, when forming a polygon out of cubic Bezier segments, each two consecutive IntegerBezierSegment2Ds define the actual curve, with the very last segment providing only the end point of the last curve, and the remaining members ignored.
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerBezierSegment2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerBezierSegment2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.IntegerBezierSegment2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.IntegerBezierSegment2D'
    """Literal Constant ``com.sun.star.geometry.IntegerBezierSegment2D``"""

    def __init__(self, Px: typing.Optional[int] = 0, Py: typing.Optional[int] = 0, C1x: typing.Optional[int] = 0, C1y: typing.Optional[int] = 0, C2x: typing.Optional[int] = 0, C2y: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Px (int, optional): Px value.
            Py (int, optional): Py value.
            C1x (int, optional): C1x value.
            C1y (int, optional): C1y value.
            C2x (int, optional): C2x value.
            C2y (int, optional): C2y value.
        """
        super().__init__()

        if isinstance(Px, IntegerBezierSegment2D):
            oth: IntegerBezierSegment2D = Px
            self.Px = oth.Px
            self.Py = oth.Py
            self.C1x = oth.C1x
            self.C1y = oth.C1y
            self.C2x = oth.C2x
            self.C2y = oth.C2y
            return

        kargs = {
            "Px": Px,
            "Py": Py,
            "C1x": C1x,
            "C1y": C1y,
            "C2x": C2x,
            "C2y": C2y,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._px = kwargs["Px"]
        self._py = kwargs["Py"]
        self._c1x = kwargs["C1x"]
        self._c1y = kwargs["C1y"]
        self._c2x = kwargs["C2x"]
        self._c2y = kwargs["C2y"]


    @property
    def Px(self) -> int:
        """
        The x coordinate of the start point.
        """
        return self._px
    
    @Px.setter
    def Px(self, value: int) -> None:
        self._px = value

    @property
    def Py(self) -> int:
        """
        The y coordinate of the start point.
        """
        return self._py
    
    @Py.setter
    def Py(self, value: int) -> None:
        self._py = value

    @property
    def C1x(self) -> int:
        """
        The x coordinate of the first control point.
        """
        return self._c1x
    
    @C1x.setter
    def C1x(self, value: int) -> None:
        self._c1x = value

    @property
    def C1y(self) -> int:
        """
        The y coordinate of the first control point.
        """
        return self._c1y
    
    @C1y.setter
    def C1y(self, value: int) -> None:
        self._c1y = value

    @property
    def C2x(self) -> int:
        """
        The x coordinate of the second control point.
        """
        return self._c2x
    
    @C2x.setter
    def C2x(self, value: int) -> None:
        self._c2x = value

    @property
    def C2y(self) -> int:
        """
        The y coordinate of the second control point.
        """
        return self._c2y
    
    @C2y.setter
    def C2y(self, value: int) -> None:
        self._c2y = value


__all__ = ['IntegerBezierSegment2D']
