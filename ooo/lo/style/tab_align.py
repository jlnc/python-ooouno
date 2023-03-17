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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.style
# Libre Office Version: 7.4
from enum import Enum


class TabAlign(Enum):
    """
    Enum Class

    

    See Also:
        `API TabAlign <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a806c06853615662029f86b19111fe0a2>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.TabAlign'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.style.TabAlign'

    CENTER = 'CENTER'
    """
    set the horizontal alignment to the center between the margins from the container object
    
    The text range is centered between the previous tabulator (or the left border, if none) and this tabulator.
    
    adjusted to the center
    """
    DECIMAL = 'DECIMAL'
    """
    The decimal point of the text range to the left of this tabulator is aligned to the position of this tabulator.
    """
    DEFAULT = 'DEFAULT'
    """
    The default alignment for tabulators is applied.
    """
    LEFT = 'LEFT'
    """
    set the horizontal alignment to the left margin from the container object
    
    The text range is left-aligned between the previous tabulator (or the left border, if none) and this tabulator.
    
    adjusted to the left border
    
    The page style is only used for left pages.
    """
    RIGHT = 'RIGHT'
    """
    set the horizontal alignment to the right margin from the container object
    
    The text range is right-aligned between the previous tabulator (or the left border, if none) and this tabulator.
    
    adjusted to the right border
    
    The page style is only used for right pages.
    """

__all__ = ['TabAlign']

