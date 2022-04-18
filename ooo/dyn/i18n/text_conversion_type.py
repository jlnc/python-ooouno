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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import TextConversionType as TextConversionType
    if hasattr(TextConversionType, '_constants') and isinstance(TextConversionType._constants, dict):
        TextConversionType._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        TextConversionType._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.TextConversionType'
        TextConversionType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global TextConversionTypeEnum
        ls = [f for f in dir(TextConversionType) if not callable(getattr(TextConversionType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(TextConversionType, name)
        TextConversionTypeEnum = IntEnum('TextConversionTypeEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.text_conversion_type import TextConversionType as TextConversionType

    class TextConversionTypeEnum(IntEnum):
        """
        Enum of Const Class TextConversionType

        These constants specify the conversion type to be used with XTextConversion.
        
        **since**
        
            OOo 1.1.2
        """
        TO_HANGUL = TextConversionType.TO_HANGUL
        """
        Conversion from Hanja to Hangul.
        """
        TO_HANJA = TextConversionType.TO_HANJA
        """
        Conversion from Hangul to Hanja.
        """
        TO_SCHINESE = TextConversionType.TO_SCHINESE
        """
        Conversion from Traditional to Simplified Chinese.
        """
        TO_TCHINESE = TextConversionType.TO_TCHINESE
        """
        Conversion from Simplified to Traditional Chinese.
        """

__all__ = ['TextConversionType', 'TextConversionTypeEnum']
