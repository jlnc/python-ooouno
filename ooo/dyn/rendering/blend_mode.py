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
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import BlendMode as BlendMode
    if hasattr(BlendMode, '_constants') and isinstance(BlendMode._constants, dict):
        BlendMode._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        BlendMode._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.BlendMode'
        BlendMode._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global BlendModeEnum
        ls = [f for f in dir(BlendMode) if not callable(getattr(BlendMode, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(BlendMode, name)
        BlendModeEnum = IntEnum('BlendModeEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.blend_mode import BlendMode as BlendMode

    class BlendModeEnum(IntEnum):
        """
        Enum of Const Class BlendMode

        These constants determine some extra ways how the primitive color is combined with the background.
        
        Please refer to the PDF specification for explanations of this constants.
        """
        NORMAL = BlendMode.NORMAL
        MULTIPLY = BlendMode.MULTIPLY
        SCREEN = BlendMode.SCREEN
        OVERLAY = BlendMode.OVERLAY
        DARKEN = BlendMode.DARKEN
        LIGHTEN = BlendMode.LIGHTEN
        COLOR_DODGE = BlendMode.COLOR_DODGE
        COLOR_BURN = BlendMode.COLOR_BURN
        HARD_LIGHT = BlendMode.HARD_LIGHT
        SOFT_LIGHT = BlendMode.SOFT_LIGHT
        DIFFERENCE = BlendMode.DIFFERENCE
        EXCLUSION = BlendMode.EXCLUSION
        HUE = BlendMode.HUE
        SATURATION = BlendMode.SATURATION
        COLOR = BlendMode.COLOR
        LUMINOSITY = BlendMode.LUMINOSITY

__all__ = ['BlendMode', 'BlendModeEnum']
