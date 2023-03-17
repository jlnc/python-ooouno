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
# Namespace: com.sun.star.embed
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class Actions(metaclass=UnoConstMeta, type_name="com.sun.star.embed.Actions", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.Actions``"""
        pass

    class ActionsEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.Actions", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.Actions`` as Enum values"""
        pass

else:
    from ...lo.embed.actions import Actions as Actions

    class ActionsEnum(IntFlag):
        """
        Enum of Const Class Actions

        This constant set contains possible actions that could be approved by ActionsApproval implementation.
        """
        PREVENT_CLOSE = Actions.PREVENT_CLOSE
        """
        \"Prevent Close\" - throws veto exception if target object is going to close.
        
        Usually a com.sun.star.util.XCloseListener implementation could use this constant to request approval to throw veto exception.
        """
        PREVENT_TERMINATION = Actions.PREVENT_TERMINATION
        """
        \"Prevent Termination\" - throws veto exception if target object is going to terminate.
        
        Usually a com.sun.star.frame.XTerminateListener implementation could use this constant to request approval to throw veto exception.
        """

__all__ = ['Actions', 'ActionsEnum']
