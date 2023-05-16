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
# Namespace: com.sun.star.linguistic2
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class LinguServiceEventFlags(metaclass=UnoConstMeta, type_name="com.sun.star.linguistic2.LinguServiceEventFlags", name_space="com.sun.star.linguistic2"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.linguistic2.LinguServiceEventFlags``"""
        pass

    class LinguServiceEventFlagsEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.linguistic2.LinguServiceEventFlags", name_space="com.sun.star.linguistic2"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.linguistic2.LinguServiceEventFlags`` as Enum values"""
        pass

else:
    from com.sun.star.linguistic2 import LinguServiceEventFlags as LinguServiceEventFlags

    class LinguServiceEventFlagsEnum(IntFlag):
        """
        Enum of Const Class LinguServiceEventFlags

        to be used in lingu-service events.
        
        These values define the flags which may be logically combined to build the event type of a com.sun.star.linguistic2.LinguServiceEvent
        
        **since**
        
            OOo 3.0.1
        """
        SPELL_CORRECT_WORDS_AGAIN = LinguServiceEventFlags.SPELL_CORRECT_WORDS_AGAIN
        """
        The spelling of previously correct words should be checked again.
        """
        SPELL_WRONG_WORDS_AGAIN = LinguServiceEventFlags.SPELL_WRONG_WORDS_AGAIN
        """
        The spelling of previously misspelled words should be checked again.
        """
        HYPHENATE_AGAIN = LinguServiceEventFlags.HYPHENATE_AGAIN
        """
        The hyphenation of words may have changed.
        """
        PROOFREAD_AGAIN = LinguServiceEventFlags.PROOFREAD_AGAIN
        """
        Request new proofreading of the document.
        
        **since**
        
            OOo 3.0.1
        """

__all__ = ['LinguServiceEventFlags', 'LinguServiceEventFlagsEnum']
