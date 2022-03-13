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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import CalendarDisplayIndex as CalendarDisplayIndex
    if hasattr(CalendarDisplayIndex, '_constants') and isinstance(CalendarDisplayIndex._constants, dict):
        CalendarDisplayIndex._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        CalendarDisplayIndex._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.CalendarDisplayIndex'
        CalendarDisplayIndex._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CalendarDisplayIndexEnum
        ls = [f for f in dir(CalendarDisplayIndex) if not callable(getattr(CalendarDisplayIndex, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CalendarDisplayIndex, name)
        CalendarDisplayIndexEnum = IntEnum('CalendarDisplayIndexEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.calendar_display_index import CalendarDisplayIndex as CalendarDisplayIndex

    class CalendarDisplayIndexEnum(IntEnum):
        """
        Enum of Const Class CalendarDisplayIndex

        Values to be passed to XCalendar.getDisplayName().
        
        **since**
        
            LibreOffice 3.5
        """
        AM_PM = CalendarDisplayIndex.AM_PM
        """
        name of an AM/PM value
        """
        DAY = CalendarDisplayIndex.DAY
        """
        name of a day of week
        """
        MONTH = CalendarDisplayIndex.MONTH
        """
        name of a month
        """
        YEAR = CalendarDisplayIndex.YEAR
        """
        name of a year (if used for a specific calendar)
        """
        ERA = CalendarDisplayIndex.ERA
        """
        name of an era, like BC/AD
        """
        GENITIVE_MONTH = CalendarDisplayIndex.GENITIVE_MONTH
        """
        name of a possessive genitive case month
        
        **since**
        
            LibreOffice 3.5
        """
        PARTITIVE_MONTH = CalendarDisplayIndex.PARTITIVE_MONTH
        """
        name of a partitive case month
        
        **since**
        
            LibreOffice 3.5
        """

__all__ = ['CalendarDisplayIndex', 'CalendarDisplayIndexEnum']
