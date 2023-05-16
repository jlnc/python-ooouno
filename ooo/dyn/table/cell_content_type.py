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
# Namespace: com.sun.star.table
# Libre Office Version: 7.4
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class CellContentType(metaclass=UnoEnumMeta, type_name="com.sun.star.table.CellContentType", name_space="com.sun.star.table"):
        """Dynamically created class that represents ``com.sun.star.table.CellContentType`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.table.CellContentType import EMPTY as CELL_CONTENT_TYPE_EMPTY
    from com.sun.star.table.CellContentType import FORMULA as CELL_CONTENT_TYPE_FORMULA
    from com.sun.star.table.CellContentType import TEXT as CELL_CONTENT_TYPE_TEXT
    from com.sun.star.table.CellContentType import VALUE as CELL_CONTENT_TYPE_VALUE


    class CellContentType(uno.Enum):
        """
        Enum Class


        See Also:
            `API CellContentType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#affea688ab9e00781fa35d8a790d10f0e>`_
        """
        __ooo_ns__: str = 'com.sun.star.table'
        __ooo_full_ns__: str = 'com.sun.star.table.CellContentType'
        __ooo_type_name__: str = 'enum'

        @property
        def typeName(self) -> str:
            return 'com.sun.star.table.CellContentType'

        EMPTY = CELL_CONTENT_TYPE_EMPTY
        """
        cell is empty.
        """
        FORMULA = CELL_CONTENT_TYPE_FORMULA
        """
        cell contains a formula.
        """
        TEXT = CELL_CONTENT_TYPE_TEXT
        """
        cell contains text.
        """
        VALUE = CELL_CONTENT_TYPE_VALUE
        """
        cell contains a constant value.
        """

__all__ = ['CellContentType']

