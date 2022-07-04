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
# Namespace: com.sun.star.document
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class LinkUpdateModes(metaclass=UnoConstMeta, type_name="com.sun.star.document.LinkUpdateModes", name_space="com.sun.star.document"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.document.LinkUpdateModes``"""
        pass

    class LinkUpdateModesEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.document.LinkUpdateModes", name_space="com.sun.star.document"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.document.LinkUpdateModes`` as Enum values"""
        pass

else:
    from ...lo.document.link_update_modes import LinkUpdateModes as LinkUpdateModes

    class LinkUpdateModesEnum(IntEnum):
        """
        Enum of Const Class LinkUpdateModes

        """
        NEVER = LinkUpdateModes.NEVER
        """
        never update links
        """
        MANUAL = LinkUpdateModes.MANUAL
        """
        update links when confirmed on request during loading the document
        """
        AUTO = LinkUpdateModes.AUTO
        """
        automatic update on load
        """
        GLOBAL_SETTING = LinkUpdateModes.GLOBAL_SETTING
        """
        use the setting that is configured in your installed application.
        
        This may be one of the above behaviors.
        """

__all__ = ['LinkUpdateModes', 'LinkUpdateModesEnum']
