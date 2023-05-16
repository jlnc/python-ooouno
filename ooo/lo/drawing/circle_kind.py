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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from enum import Enum


class CircleKind(Enum):
    """
    Enum Class


    See Also:
        `API CircleKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a6a52201f72a50075b45fea2c19340c0e>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.CircleKind'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.CircleKind'

    ARC = 'ARC'
    """
    a circle with an open cut
    """
    CUT = 'CUT'
    """
    a circle with a cut connected by two lines
    """
    FULL = 'FULL'
    """
    a full circle
    """
    SECTION = 'SECTION'
    """
    a circle with a cut connected by a line
    """

__all__ = ['CircleKind']

