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
# Namespace: com.sun.star.animations
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.animations import AnimationNodeType as AnimationNodeType
    if hasattr(AnimationNodeType, '_constants') and isinstance(AnimationNodeType._constants, dict):
        AnimationNodeType._constants['__ooo_ns__'] = 'com.sun.star.animations'
        AnimationNodeType._constants['__ooo_full_ns__'] = 'com.sun.star.animations.AnimationNodeType'
        AnimationNodeType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global AnimationNodeTypeEnum
        ls = [f for f in dir(AnimationNodeType) if not callable(getattr(AnimationNodeType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(AnimationNodeType, name)
        AnimationNodeTypeEnum = IntEnum('AnimationNodeTypeEnum', _dict)
    build_enum()
else:
    from ...lo.animations.animation_node_type import AnimationNodeType as AnimationNodeType

    class AnimationNodeTypeEnum(IntEnum):
        """
        Enum of Const Class AnimationNodeType

        This constants defines a type for an animation node.
        
        It can be used to quickly identify semantic blocks inside an animation hierarchy.
        
        **since**
        
            LibreOffice 7.1
        """
        CUSTOM = AnimationNodeType.CUSTOM
        """
        Defines a custom time node.
        """
        PAR = AnimationNodeType.PAR
        """
        Defines a parallel time container.
        """
        SEQ = AnimationNodeType.SEQ
        """
        Defines a sequence time container.
        """
        ITERATE = AnimationNodeType.ITERATE
        """
        Defines an iterate time container.
        """
        ANIMATE = AnimationNodeType.ANIMATE
        """
        Defines a generic attribute animation.
        """
        SET = AnimationNodeType.SET
        """
        Defines a simple mean of just setting the value of an attribute for a specified duration.
        """
        ANIMATEMOTION = AnimationNodeType.ANIMATEMOTION
        """
        Defines a move animation along a path.
        """
        ANIMATECOLOR = AnimationNodeType.ANIMATECOLOR
        """
        Defines an animation of a color attribute.
        """
        ANIMATETRANSFORM = AnimationNodeType.ANIMATETRANSFORM
        """
        Defines an animation of a transformation attribute.
        """
        TRANSITIONFILTER = AnimationNodeType.TRANSITIONFILTER
        """
        Defines an animation of a filter behavior.
        """
        AUDIO = AnimationNodeType.AUDIO
        """
        Defines an audio effect.
        """
        COMMAND = AnimationNodeType.COMMAND
        """
        Defines a command effect.
        """
        ANIMATEPHYSICS = AnimationNodeType.ANIMATEPHYSICS
        """
        Defines a physics animation.
        
        **since**
        
            LibreOffice 7.1
        """

__all__ = ['AnimationNodeType', 'AnimationNodeTypeEnum']
