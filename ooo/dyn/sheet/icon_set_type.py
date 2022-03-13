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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import IconSetType as IconSetType
    if hasattr(IconSetType, '_constants') and isinstance(IconSetType._constants, dict):
        IconSetType._constants['__ooo_ns__'] = 'com.sun.star.sheet'
        IconSetType._constants['__ooo_full_ns__'] = 'com.sun.star.sheet.IconSetType'
        IconSetType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global IconSetTypeEnum
        ls = [f for f in dir(IconSetType) if not callable(getattr(IconSetType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(IconSetType, name)
        IconSetTypeEnum = IntEnum('IconSetTypeEnum', _dict)
    build_enum()
else:
    from ...lo.sheet.icon_set_type import IconSetType as IconSetType

    class IconSetTypeEnum(IntEnum):
        """
        Enum of Const Class IconSetType

        """
        ICONSET_3ARROWS = IconSetType.ICONSET_3ARROWS
        ICONSET_3ARROWS_GRAY = IconSetType.ICONSET_3ARROWS_GRAY
        ICONSET_3FLAGS = IconSetType.ICONSET_3FLAGS
        ICONSET_3TRAFFICLIGHTS1 = IconSetType.ICONSET_3TRAFFICLIGHTS1
        ICONSET_3TRAFFICLIGHTS2 = IconSetType.ICONSET_3TRAFFICLIGHTS2
        ICONSET_3SIGNS = IconSetType.ICONSET_3SIGNS
        ICONSET_3SYMBOLS = IconSetType.ICONSET_3SYMBOLS
        ICONSET_3SYMBOLS2 = IconSetType.ICONSET_3SYMBOLS2
        ICONSET_3SMILIES = IconSetType.ICONSET_3SMILIES
        ICONSET_3COLOR_SIMILIES = IconSetType.ICONSET_3COLOR_SIMILIES
        ICONSET_4ARROWS = IconSetType.ICONSET_4ARROWS
        ICONSET_4ARROWS_GRAY = IconSetType.ICONSET_4ARROWS_GRAY
        ICONSET_4RED_TO_BLACK = IconSetType.ICONSET_4RED_TO_BLACK
        ICONSET_4RATING = IconSetType.ICONSET_4RATING
        ICONSET_4TRAFFICLIGHTS = IconSetType.ICONSET_4TRAFFICLIGHTS
        ICONSET_5ARROWS = IconSetType.ICONSET_5ARROWS
        ICONSET_5ARROWS_GRAY = IconSetType.ICONSET_5ARROWS_GRAY
        ICONSET_5RATINGS = IconSetType.ICONSET_5RATINGS
        ICONSET_5QUARTERS = IconSetType.ICONSET_5QUARTERS

__all__ = ['IconSetType', 'IconSetTypeEnum']
