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
# Namespace: com.sun.star.linguistic2
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.linguistic2 import SpellFailure as SpellFailure
    if hasattr(SpellFailure, '_constants') and isinstance(SpellFailure._constants, dict):
        SpellFailure._constants['__ooo_ns__'] = 'com.sun.star.linguistic2'
        SpellFailure._constants['__ooo_full_ns__'] = 'com.sun.star.linguistic2.SpellFailure'
        SpellFailure._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global SpellFailureEnum
        ls = [f for f in dir(SpellFailure) if not callable(getattr(SpellFailure, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(SpellFailure, name)
        SpellFailureEnum = IntEnum('SpellFailureEnum', _dict)
    build_enum()
else:
    from ...lo.linguistic2.spell_failure import SpellFailure as SpellFailure

    class SpellFailureEnum(IntEnum):
        """
        Enum of Const Class SpellFailure

        these define the various return types for spell checking to fail verification.
        
        A value of this type is part of the com.sun.star.linguistic2.XSpellAlternatives interface which is the return type for an unsuccessful spelling attempt.
        """
        IS_NEGATIVE_WORD = SpellFailure.IS_NEGATIVE_WORD
        """
        The word is a negative one, that is, it should not be used.
        """
        CAPTION_ERROR = SpellFailure.CAPTION_ERROR
        """
        The capitalization of the word is wrong.
        """
        SPELLING_ERROR = SpellFailure.SPELLING_ERROR
        """
        The spelling of the word is wrong (or at least not known to be correct).
        """

__all__ = ['SpellFailure', 'SpellFailureEnum']
