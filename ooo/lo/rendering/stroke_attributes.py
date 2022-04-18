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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class StrokeAttributes(object):
    """
    Struct Class

    This structure contains all attributes required for path stroking.
    
    Path stroking is the process of drawing a polygon with a thick pen. The various attributes contained in this structure can be used to customize that process.

    See Also:
        `API StrokeAttributes <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1StrokeAttributes.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.StrokeAttributes'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.StrokeAttributes'
    """Literal Constant ``com.sun.star.rendering.StrokeAttributes``"""

    def __init__(self, DashArray: typing.Optional[typing.Tuple[float, ...]] = UNO_NONE, LineArray: typing.Optional[typing.Tuple[float, ...]] = UNO_NONE, StrokeWidth: typing.Optional[float] = 0.0, MiterLimit: typing.Optional[float] = 0.0, StartCapType: typing.Optional[int] = 0, EndCapType: typing.Optional[int] = 0, JoinType: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            DashArray (typing.Tuple[float, ...], optional): DashArray value.
            LineArray (typing.Tuple[float, ...], optional): LineArray value.
            StrokeWidth (float, optional): StrokeWidth value.
            MiterLimit (float, optional): MiterLimit value.
            StartCapType (int, optional): StartCapType value.
            EndCapType (int, optional): EndCapType value.
            JoinType (int, optional): JoinType value.
        """
        super().__init__()

        if isinstance(DashArray, StrokeAttributes):
            oth: StrokeAttributes = DashArray
            self.DashArray = oth.DashArray
            self.LineArray = oth.LineArray
            self.StrokeWidth = oth.StrokeWidth
            self.MiterLimit = oth.MiterLimit
            self.StartCapType = oth.StartCapType
            self.EndCapType = oth.EndCapType
            self.JoinType = oth.JoinType
            return

        kargs = {
            "DashArray": DashArray,
            "LineArray": LineArray,
            "StrokeWidth": StrokeWidth,
            "MiterLimit": MiterLimit,
            "StartCapType": StartCapType,
            "EndCapType": EndCapType,
            "JoinType": JoinType,
        }
        if kargs["DashArray"] is UNO_NONE:
            kargs["DashArray"] = None
        if kargs["LineArray"] is UNO_NONE:
            kargs["LineArray"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._dash_array = kwargs["DashArray"]
        self._line_array = kwargs["LineArray"]
        self._stroke_width = kwargs["StrokeWidth"]
        self._miter_limit = kwargs["MiterLimit"]
        self._start_cap_type = kwargs["StartCapType"]
        self._end_cap_type = kwargs["EndCapType"]
        self._join_type = kwargs["JoinType"]


    @property
    def DashArray(self) -> typing.Tuple[float, ...]:
        """
        Array of ink on and off lengths, measured in user coordinate space.
        
        The first element specifies the length of the first \"on\" segment of the dashing, the second element the length of the first \"off\" segment, and so forth. Give zero elements here for solid strokes. This array always have an even number of elements, with zero, as usual, counting as even here. Furthermore, each entry in this array must have a value that is positive (or 0.0)
        """
        return self._dash_array
    
    @DashArray.setter
    def DashArray(self, value: typing.Tuple[float, ...]) -> None:
        self._dash_array = value

    @property
    def LineArray(self) -> typing.Tuple[float, ...]:
        """
        Array of line widths and spacings for multiple-line strokes.
        
        The entries here are relative to the StrokeAttributes.StrokeWidth attribute above, i.e. the total width of all lines and spacings will always equal StrokeAttributes.StrokeWidth. The first element specifies the width of the rightmost line, when traveling from the start point of the path to the end point. The second element specifies the space between the first line and the second line, and so forth. If the array ends with a spacing, this spacing is included in the total width of the multiple-line stroke. That is, the stroke becomes asymmetric.
        """
        return self._line_array
    
    @LineArray.setter
    def LineArray(self, value: typing.Tuple[float, ...]) -> None:
        self._line_array = value

    @property
    def StrokeWidth(self) -> float:
        """
        Defines the width of the stroke, measured in user coordinate space.
        
        This value must be positive (or 0.0)
        """
        return self._stroke_width
    
    @StrokeWidth.setter
    def StrokeWidth(self, value: float) -> None:
        self._stroke_width = value

    @property
    def MiterLimit(self) -> float:
        """
        Determines the maximal length of the diagonal in mitered corners.
        
        This attribute is only used when StrokeAttributes.JoinType is set to PathJoinType.MITER. Should the length of a corner's diagonal exceed this limit, a beveled join is used instead. This value must be positive (or 0.0, which is equivalent to setting StrokeAttributes.JoinType to PathJoinType.BEVEL.
        
        Before performing the actual comparison, implementations will multiply the MiterLimit with the current StrokeWidth, such that, with phi being the angle between the two joining segments, MiterLimit=1/sin(phi/2.0).
        """
        return self._miter_limit
    
    @MiterLimit.setter
    def MiterLimit(self, value: float) -> None:
        self._miter_limit = value

    @property
    def StartCapType(self) -> int:
        """
        The start shape of the stroke.
        
        The start point is the first point of every polygon of the path poly-polygon.
        """
        return self._start_cap_type
    
    @StartCapType.setter
    def StartCapType(self, value: int) -> None:
        self._start_cap_type = value

    @property
    def EndCapType(self) -> int:
        """
        The end shape of the stroke.
        
        The end point is the last point of every polygon of the path poly-polygon.
        """
        return self._end_cap_type
    
    @EndCapType.setter
    def EndCapType(self, value: int) -> None:
        self._end_cap_type = value

    @property
    def JoinType(self) -> int:
        """
        The join shape of the stroke.
        
        After every sub-stroke, i.e. after every line or curve segment within a single path polygon, a shape of this type is inserted into the stroke to glue the segments together. Please note that distinct polygons within the path poly-polygon are not connected, and therefore also not joined via the shape specified here.
        """
        return self._join_type
    
    @JoinType.setter
    def JoinType(self, value: int) -> None:
        self._join_type = value


__all__ = ['StrokeAttributes']
