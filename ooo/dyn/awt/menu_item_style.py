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
# Namespace: com.sun.star.awt
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class MenuItemStyle(metaclass=UnoConstMeta, type_name="com.sun.star.awt.MenuItemStyle", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.MenuItemStyle``"""
        pass

    class MenuItemStyleEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.MenuItemStyle", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.MenuItemStyle`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import MenuItemStyle as MenuItemStyle
    else:
        # keep document generators happy
        from ...lo.awt.menu_item_style import MenuItemStyle as MenuItemStyle

    class MenuItemStyleEnum(IntFlag):
        """
        Enum of Const Class MenuItemStyle

        These values are used to specify the properties of a menu item.
        """
        CHECKABLE = MenuItemStyle.CHECKABLE
        """
        specifies an item which can be checked independently.
        """
        RADIOCHECK = MenuItemStyle.RADIOCHECK
        """
        specifies an item which can be checked dependent on the neighbouring items.
        """
        AUTOCHECK = MenuItemStyle.AUTOCHECK
        """
        specifies to check this item automatically on select.
        """

__all__ = ['MenuItemStyle', 'MenuItemStyleEnum']
