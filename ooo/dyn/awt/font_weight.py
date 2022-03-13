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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import FontWeight as FontWeight
    if hasattr(FontWeight, '_constants') and isinstance(FontWeight._constants, dict):
        FontWeight._constants['__ooo_ns__'] = 'com.sun.star.awt'
        FontWeight._constants['__ooo_full_ns__'] = 'com.sun.star.awt.FontWeight'
        FontWeight._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FontWeightEnum
        ls = [f for f in dir(FontWeight) if not callable(getattr(FontWeight, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FontWeight, name)
        FontWeightEnum = IntEnum('FontWeightEnum', _dict)
    build_enum()
else:
    from ...lo.awt.font_weight import FontWeight as FontWeight

    class FontWeightEnum(IntEnum):
        """
        Enum of Const Class FontWeight

        These values are used to specify whether a font is thin or bold.
        
        They may be expanded in future versions.
        """
        DONTKNOW = FontWeight.DONTKNOW
        """
        The font weight is not specified/known.
        """
        THIN = FontWeight.THIN
        """
        specifies a 50% font weight.
        """
        ULTRALIGHT = FontWeight.ULTRALIGHT
        """
        specifies a 60% font weight.
        """
        LIGHT = FontWeight.LIGHT
        """
        specifies a 75% font weight.
        """
        SEMILIGHT = FontWeight.SEMILIGHT
        """
        specifies a 90% font weight.
        """
        NORMAL = FontWeight.NORMAL
        """
        specifies a normal font weight.
        """
        SEMIBOLD = FontWeight.SEMIBOLD
        """
        specifies a 110% font weight.
        """
        BOLD = FontWeight.BOLD
        """
        specifies a 150% font weight.
        """
        ULTRABOLD = FontWeight.ULTRABOLD
        """
        specifies a 175% font weight.
        """
        BLACK = FontWeight.BLACK
        """
        specifies a 200% font weight.
        """

__all__ = ['FontWeight', 'FontWeightEnum']
