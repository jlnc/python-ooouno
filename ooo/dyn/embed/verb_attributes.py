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
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.embed import VerbAttributes as VerbAttributes
    if hasattr(VerbAttributes, '_constants') and isinstance(VerbAttributes._constants, dict):
        VerbAttributes._constants['__ooo_ns__'] = 'com.sun.star.embed'
        VerbAttributes._constants['__ooo_full_ns__'] = 'com.sun.star.embed.VerbAttributes'
        VerbAttributes._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global VerbAttributesEnum
        ls = [f for f in dir(VerbAttributes) if not callable(getattr(VerbAttributes, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(VerbAttributes, name)
        VerbAttributesEnum = IntFlag('VerbAttributesEnum', _dict)
    build_enum()
else:
    from ...lo.embed.verb_attributes import VerbAttributes as VerbAttributes

    class VerbAttributesEnum(IntFlag):
        """
        Enum of Const Class VerbAttributes

        The constant set specifies possible attributes of a verb.
        """
        MS_VERBATTR_NEVERDIRTIES = VerbAttributes.MS_VERBATTR_NEVERDIRTIES
        """
        Execution of the verb with this attribute must not modify the object.
        """
        MS_VERBATTR_ONCONTAINERMENU = VerbAttributes.MS_VERBATTR_ONCONTAINERMENU
        """
        indicates that the verb should appear in the object's menu.
        """

__all__ = ['VerbAttributes', 'VerbAttributesEnum']
