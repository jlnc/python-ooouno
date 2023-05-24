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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ReferenceFieldSource(metaclass=UnoConstMeta, type_name="com.sun.star.text.ReferenceFieldSource", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.ReferenceFieldSource``"""
        pass

    class ReferenceFieldSourceEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.ReferenceFieldSource", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.ReferenceFieldSource`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.text import ReferenceFieldSource as ReferenceFieldSource
    else:
        # keep document generators happy
        from ...lo.text.reference_field_source import ReferenceFieldSource as ReferenceFieldSource

    class ReferenceFieldSourceEnum(IntEnum):
        """
        Enum of Const Class ReferenceFieldSource

        These constants define the type of the source of a reference field.
        """
        REFERENCE_MARK = ReferenceFieldSource.REFERENCE_MARK
        """
        The source is a reference mark.
        """
        SEQUENCE_FIELD = ReferenceFieldSource.SEQUENCE_FIELD
        """
        The source is a number sequence field.
        """
        BOOKMARK = ReferenceFieldSource.BOOKMARK
        """
        The source is a bookmark.
        """
        FOOTNOTE = ReferenceFieldSource.FOOTNOTE
        """
        The source is a footnote.
        """
        ENDNOTE = ReferenceFieldSource.ENDNOTE
        """
        The source is an endnote.
        """

__all__ = ['ReferenceFieldSource', 'ReferenceFieldSourceEnum']
