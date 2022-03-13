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
# Namespace: com.sun.star.awt
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import FontType as FontType
    if hasattr(FontType, '_constants') and isinstance(FontType._constants, dict):
        FontType._constants['__ooo_ns__'] = 'com.sun.star.awt'
        FontType._constants['__ooo_full_ns__'] = 'com.sun.star.awt.FontType'
        FontType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FontTypeEnum
        ls = [f for f in dir(FontType) if not callable(getattr(FontType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FontType, name)
        FontTypeEnum = IntFlag('FontTypeEnum', _dict)
    build_enum()
else:
    from ...lo.awt.font_type import FontType as FontType

    class FontTypeEnum(IntFlag):
        """
        Enum of Const Class FontType

        These values are used to specify the technology of the font representation.
        
        They may be expanded in future versions.
        """
        DONTKNOW = FontType.DONTKNOW
        """
        The type of the font is not known.
        """
        RASTER = FontType.RASTER
        """
        specifies a raster font.
        """
        DEVICE = FontType.DEVICE
        """
        specifies a device font.
        """
        SCALABLE = FontType.SCALABLE
        """
        specifies a scalable font.
        """

__all__ = ['FontType', 'FontTypeEnum']
