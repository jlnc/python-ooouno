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
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class HorizontalDimensioning(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.HorizontalDimensioning", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.HorizontalDimensioning`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.drawing.HorizontalDimensioning import AUTO as HORIZONTAL_DIMENSIONING_AUTO
        from com.sun.star.drawing.HorizontalDimensioning import CENTERED as HORIZONTAL_DIMENSIONING_CENTERED
        from com.sun.star.drawing.HorizontalDimensioning import LEFT as HORIZONTAL_DIMENSIONING_LEFT
        from com.sun.star.drawing.HorizontalDimensioning import RIGHT as HORIZONTAL_DIMENSIONING_RIGHT

        class HorizontalDimensioning(uno.Enum):
            """
            Enum Class


            See Also:
                `API HorizontalDimensioning <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a6c20b7eb17d1eb1746fddc52487581f9>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.drawing.HorizontalDimensioning', value)

            __ooo_ns__: str = 'com.sun.star.drawing'
            __ooo_full_ns__: str = 'com.sun.star.drawing.HorizontalDimensioning'
            __ooo_type_name__: str = 'enum'

            AUTO = HORIZONTAL_DIMENSIONING_AUTO
            """
            the connection point is chosen automatically,

            Set this to have the application select the best horizontal position for the text.
            """
            CENTERED = HORIZONTAL_DIMENSIONING_CENTERED
            """
            The text is positioned at the center.

            The text is positioned over the main line.
            """
            LEFT = HORIZONTAL_DIMENSIONING_LEFT
            """
            the connection line leaves the connected object to the left,

            The left edge of the text is adjusted to the left edge of the shape.

            The text is positioned to the left.
            """
            RIGHT = HORIZONTAL_DIMENSIONING_RIGHT
            """
            the connection line leaves the connected object to the right,

            The right edge of the text is adjusted to the right edge of the shape.

            The text is positioned to the right.
            """
    else:
        # keep document generators happy
        from ...lo.drawing.horizontal_dimensioning import HorizontalDimensioning as HorizontalDimensioning


__all__ = ['HorizontalDimensioning']
