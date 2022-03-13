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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from enum import Enum


class TransliterationModules(Enum):
    """
    Enum Class

    

    See Also:
        `API TransliterationModules <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n.html#a9c57a33dd757352c82923f4c7f6cf93c>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.TransliterationModules'
    __ooo_type_name__: str = 'enum'

    END_OF_MODULE = 'END_OF_MODULE'
    """
    """
    FULLWIDTH_HALFWIDTH = 'FULLWIDTH_HALFWIDTH'
    """
    Transliterate a string from full width character to half width character.
    """
    HALFWIDTH_FULLWIDTH = 'HALFWIDTH_FULLWIDTH'
    """
    Transliterate a string from half width character to full width character.
    """
    HIRAGANA_KATAKANA = 'HIRAGANA_KATAKANA'
    """
    Transliterate a Japanese string from Hiragana to Katakana.
    """
    IGNORE_CASE = 'IGNORE_CASE'
    """
    Ignore case when comparing strings by transliteration service.
    """
    IGNORE_KANA = 'IGNORE_KANA'
    """
    Ignore Hiragana and Katakana when comparing strings by transliteration service.
    """
    IGNORE_MASK = 'IGNORE_MASK'
    """
    """
    IGNORE_WIDTH = 'IGNORE_WIDTH'
    """
    Ignore full width and half width character when comparing strings by transliteration service.
    
    Ignore full width and half width characters when comparing strings by transliteration service.
    """
    KATAKANA_HIRAGANA = 'KATAKANA_HIRAGANA'
    """
    Transliterate a Japanese string from Katakana to Hiragana.
    """
    LOWERCASE_UPPERCASE = 'LOWERCASE_UPPERCASE'
    """
    Transliterate a string from lower case to upper case.
    """
    NON_IGNORE_MASK = 'NON_IGNORE_MASK'
    """
    """
    NumToTextFormalHangul_ko = 'NumToTextFormalHangul_ko'
    """
    Transliterate an ASCII number string to formal Korean Hangul number string in spellout format.
    """
    NumToTextFormalLower_ko = 'NumToTextFormalLower_ko'
    """
    Transliterate an ASCII number string to formal Korean Hanja lower case number string in spellout format.
    """
    NumToTextFormalUpper_ko = 'NumToTextFormalUpper_ko'
    """
    Transliterate an ASCII number string to formal Korean Hanja upper case number string in spellout format.
    """
    NumToTextLower_zh_CN = 'NumToTextLower_zh_CN'
    """
    Transliterate an ASCII number string to Simplified Chinese lower case number string in spellout format.
    """
    NumToTextLower_zh_TW = 'NumToTextLower_zh_TW'
    """
    Transliterate an ASCII number string to Traditional Chinese lower case number string in spellout format.
    """
    NumToTextUpper_zh_CN = 'NumToTextUpper_zh_CN'
    """
    Transliterate an ASCII number string to Simplified Chinese upper case number string in spellout format.
    """
    NumToTextUpper_zh_TW = 'NumToTextUpper_zh_TW'
    """
    Transliterate an ASCII number string to Traditional Chinese upper case number string in spellout format.
    """
    UPPERCASE_LOWERCASE = 'UPPERCASE_LOWERCASE'
    """
    Transliterate a string from upper case to lower case.
    """
    ignoreBaFa_ja_JP = 'ignoreBaFa_ja_JP'
    """
    Ignore Katakana and Hiragana Ba/Gua and Ha/Fa in Japanese fuzzy search.
    """
    ignoreHyuByu_ja_JP = 'ignoreHyuByu_ja_JP'
    """
    Ignore Katakana and Hiragana Hyu/Fyu and Byu/Gyu in Japanese fuzzy search.
    """
    ignoreIandEfollowedByYa_ja_JP = 'ignoreIandEfollowedByYa_ja_JP'
    """
    Ignore Katakana YA/A which follows the character in either I or E row in Japanese fuzzy search.
    
    Ignore Katakana YA/A following the character in either I or E row in Japanese fuzzy search.
    """
    ignoreIterationMark_ja_JP = 'ignoreIterationMark_ja_JP'
    """
    Ignore Hiragana and Katakana iteration mark in Japanese fuzzy search.
    """
    ignoreKiKuFollowedBySa_ja_JP = 'ignoreKiKuFollowedBySa_ja_JP'
    """
    Ignore Katakana KI/KU which follows the character in SA column in Japanese fuzzy search.
    
    Ignore Katakana KI/KU following the character in SA column in Japanese fuzzy search.
    """
    ignoreMiddleDot_ja_JP = 'ignoreMiddleDot_ja_JP'
    """
    Ignore middle dot in Japanese fuzzy search.
    """
    ignoreMinusSign_ja_JP = 'ignoreMinusSign_ja_JP'
    """
    Ignore dash or minus sign in Japanese fuzzy search.
    """
    ignoreProlongedSoundMark_ja_JP = 'ignoreProlongedSoundMark_ja_JP'
    """
    Ignore Japanese prolonged sound mark in Japanese fuzzy search.
    """
    ignoreSeZe_ja_JP = 'ignoreSeZe_ja_JP'
    """
    Ignore Katakana and Hiragana Se/Sye and Ze/Je in Japanese fuzzy search.
    """
    ignoreSeparator_ja_JP = 'ignoreSeparator_ja_JP'
    """
    Ignore separator punctuations in Japanese fuzzy search.
    """
    ignoreSize_ja_JP = 'ignoreSize_ja_JP'
    """
    Ignore Japanese normal and small sized character in Japanese fuzzy search.
    """
    ignoreSpace_ja_JP = 'ignoreSpace_ja_JP'
    """
    Ignore white space characters, include space, TAB, return, etc. in Japanese fuzzy search.
    """
    ignoreTiJi_ja_JP = 'ignoreTiJi_ja_JP'
    """
    Ignore Katakana and Hiragana Tsui/Tea/Ti and Dyi/Ji in Japanese fuzzy search.
    """
    ignoreTraditionalKana_ja_JP = 'ignoreTraditionalKana_ja_JP'
    """
    Ignore Japanese traditional Katakana and Hiragana character in Japanese fuzzy search.
    
    Ignore Japanese traditional Katakana and Hiragana characters in Japanese fuzzy search.
    """
    ignoreTraditionalKanji_ja_JP = 'ignoreTraditionalKanji_ja_JP'
    """
    Ignore Japanese traditional Kanji character in Japanese fuzzy search.
    
    Ignore Japanese traditional Kanji characters in Japanese fuzzy search.
    """
    ignoreZiZu_ja_JP = 'ignoreZiZu_ja_JP'
    """
    Ignore Katakana and Hiragana Zi/Zi and Zu/Zu in Japanese fuzzy search.
    """
    largeToSmall_ja_JP = 'largeToSmall_ja_JP'
    """
    transliterate Japanese normal sized character to small sized character
    """
    smallToLarge_ja_JP = 'smallToLarge_ja_JP'
    """
    transliterate Japanese small sized character to normal sized character
    """

__all__ = ['TransliterationModules']

