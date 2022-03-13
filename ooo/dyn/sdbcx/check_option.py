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
# Namespace: com.sun.star.sdbcx
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdbcx import CheckOption as CheckOption
    if hasattr(CheckOption, '_constants') and isinstance(CheckOption._constants, dict):
        CheckOption._constants['__ooo_ns__'] = 'com.sun.star.sdbcx'
        CheckOption._constants['__ooo_full_ns__'] = 'com.sun.star.sdbcx.CheckOption'
        CheckOption._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CheckOptionEnum
        ls = [f for f in dir(CheckOption) if not callable(getattr(CheckOption, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CheckOption, name)
        CheckOptionEnum = IntEnum('CheckOptionEnum', _dict)
    build_enum()
else:
    from ...lo.sdbcx.check_option import CheckOption as CheckOption

    class CheckOptionEnum(IntEnum):
        """
        Enum of Const Class CheckOption

        determines the check option for a view.
        """
        NONE = CheckOption.NONE
        """
        indicates that no value checking is applied during updates of view data.
        """
        CASCADE = CheckOption.CASCADE
        """
        indicates that the value checking is applied for the view and all base views.
        """
        LOCAL = CheckOption.LOCAL
        """
        indicates that the value checking is applied only for the view.
        """

__all__ = ['CheckOption', 'CheckOptionEnum']
