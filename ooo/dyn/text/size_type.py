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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class SizeType(metaclass=UnoConstMeta, type_name="com.sun.star.text.SizeType", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.SizeType``"""
        pass

    class SizeTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.SizeType", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.SizeType`` as Enum values"""
        pass

else:
    from ...lo.text.size_type import SizeType as SizeType

    class SizeTypeEnum(IntEnum):
        """
        Enum of Const Class SizeType

        The height value of objects like text frames or table rows may be interpreted in different ways.
        
        The values may specify the absolute height (SIZETYPE_FIX), the minimum height (SIZETYPE_MIN), or they are ignored (SIZETYPE_VAR), in which case the real height depends on the content. This information is contained in a property called \"SizeType\".
        """
        VARIABLE = SizeType.VARIABLE
        FIX = SizeType.FIX
        MIN = SizeType.MIN
        """
        The height property determines the minimum height of the object, but the actual height will be increased if the content demands it.
        """

__all__ = ['SizeType', 'SizeTypeEnum']
