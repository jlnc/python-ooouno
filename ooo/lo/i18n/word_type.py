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


class WordType(object):
    """
    Const Class

    Constants to specify the type of words.
    
    Used with XBreakIterator.nextWord(), XBreakIterator.previousWord(), XBreakIterator.getWordBoundary(), XBreakIterator.getWordType(), XBreakIterator.isBeginWord(), XBreakIterator.isEndWord()

    See Also:
        `API WordType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1WordType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.WordType'
    __ooo_type_name__: str = 'const'

    ANY_WORD = 0
    """
    Any \"words\" - words in the meaning of same character types, collection of alphanumeric characters, or collection of non-alphanumeric characters.
    """
    ANYWORD_IGNOREWHITESPACES = 1
    """
    Any \"words\" - words in the meaning of same character types, collection of alphanumeric characters, or collection of non-alphanumeric characters except blanks.
    """
    DICTIONARY_WORD = 2
    """
    \"words\" - in the meaning of a collection of alphanumeric characters and some punctuations, like dot for abbreviation.
    """
    WORD_COUNT = 3
    """
    The mode for counting words, it will combine punctuations and spaces as word trail.
    """

__all__ = ['WordType']
