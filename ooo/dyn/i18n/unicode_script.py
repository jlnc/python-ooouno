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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class UnicodeScript(metaclass=UnoEnumMeta, type_name="com.sun.star.i18n.UnicodeScript", name_space="com.sun.star.i18n"):
        """Dynamically created class that represents ``com.sun.star.i18n.UnicodeScript`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.i18n.UnicodeScript import kAlphabeticPresentation as UNICODE_SCRIPT_kAlphabeticPresentation
        from com.sun.star.i18n.UnicodeScript import kArabic as UNICODE_SCRIPT_kArabic
        from com.sun.star.i18n.UnicodeScript import kArabicPresentationA as UNICODE_SCRIPT_kArabicPresentationA
        from com.sun.star.i18n.UnicodeScript import kArabicPresentationB as UNICODE_SCRIPT_kArabicPresentationB
        from com.sun.star.i18n.UnicodeScript import kArmenian as UNICODE_SCRIPT_kArmenian
        from com.sun.star.i18n.UnicodeScript import kArrow as UNICODE_SCRIPT_kArrow
        from com.sun.star.i18n.UnicodeScript import kBasicLatin as UNICODE_SCRIPT_kBasicLatin
        from com.sun.star.i18n.UnicodeScript import kBengali as UNICODE_SCRIPT_kBengali
        from com.sun.star.i18n.UnicodeScript import kBlockElement as UNICODE_SCRIPT_kBlockElement
        from com.sun.star.i18n.UnicodeScript import kBopomofo as UNICODE_SCRIPT_kBopomofo
        from com.sun.star.i18n.UnicodeScript import kBopomofoExtended as UNICODE_SCRIPT_kBopomofoExtended
        from com.sun.star.i18n.UnicodeScript import kBoxDrawing as UNICODE_SCRIPT_kBoxDrawing
        from com.sun.star.i18n.UnicodeScript import kBraillePatterns as UNICODE_SCRIPT_kBraillePatterns
        from com.sun.star.i18n.UnicodeScript import kCJKCompatibility as UNICODE_SCRIPT_kCJKCompatibility
        from com.sun.star.i18n.UnicodeScript import kCJKCompatibilityForm as UNICODE_SCRIPT_kCJKCompatibilityForm
        from com.sun.star.i18n.UnicodeScript import kCJKCompatibilityIdeograph as UNICODE_SCRIPT_kCJKCompatibilityIdeograph
        from com.sun.star.i18n.UnicodeScript import kCJKRadicalsSupplement as UNICODE_SCRIPT_kCJKRadicalsSupplement
        from com.sun.star.i18n.UnicodeScript import kCJKSymbolPunctuation as UNICODE_SCRIPT_kCJKSymbolPunctuation
        from com.sun.star.i18n.UnicodeScript import kCJKUnifiedIdeograph as UNICODE_SCRIPT_kCJKUnifiedIdeograph
        from com.sun.star.i18n.UnicodeScript import kCJKUnifiedIdeographsExtensionA as UNICODE_SCRIPT_kCJKUnifiedIdeographsExtensionA
        from com.sun.star.i18n.UnicodeScript import kCherokee as UNICODE_SCRIPT_kCherokee
        from com.sun.star.i18n.UnicodeScript import kCombiningDiacritical as UNICODE_SCRIPT_kCombiningDiacritical
        from com.sun.star.i18n.UnicodeScript import kCombiningHalfMark as UNICODE_SCRIPT_kCombiningHalfMark
        from com.sun.star.i18n.UnicodeScript import kControlPicture as UNICODE_SCRIPT_kControlPicture
        from com.sun.star.i18n.UnicodeScript import kCurrencySymbolScript as UNICODE_SCRIPT_kCurrencySymbolScript
        from com.sun.star.i18n.UnicodeScript import kCyrillic as UNICODE_SCRIPT_kCyrillic
        from com.sun.star.i18n.UnicodeScript import kDevanagari as UNICODE_SCRIPT_kDevanagari
        from com.sun.star.i18n.UnicodeScript import kDingbat as UNICODE_SCRIPT_kDingbat
        from com.sun.star.i18n.UnicodeScript import kEnclosedAlphanumeric as UNICODE_SCRIPT_kEnclosedAlphanumeric
        from com.sun.star.i18n.UnicodeScript import kEnclosedCJKLetterMonth as UNICODE_SCRIPT_kEnclosedCJKLetterMonth
        from com.sun.star.i18n.UnicodeScript import kEthiopic as UNICODE_SCRIPT_kEthiopic
        from com.sun.star.i18n.UnicodeScript import kGeneralPunctuation as UNICODE_SCRIPT_kGeneralPunctuation
        from com.sun.star.i18n.UnicodeScript import kGeometricShape as UNICODE_SCRIPT_kGeometricShape
        from com.sun.star.i18n.UnicodeScript import kGeorgian as UNICODE_SCRIPT_kGeorgian
        from com.sun.star.i18n.UnicodeScript import kGreek as UNICODE_SCRIPT_kGreek
        from com.sun.star.i18n.UnicodeScript import kGreekExtended as UNICODE_SCRIPT_kGreekExtended
        from com.sun.star.i18n.UnicodeScript import kGujarati as UNICODE_SCRIPT_kGujarati
        from com.sun.star.i18n.UnicodeScript import kGurmukhi as UNICODE_SCRIPT_kGurmukhi
        from com.sun.star.i18n.UnicodeScript import kHalfwidthFullwidthForm as UNICODE_SCRIPT_kHalfwidthFullwidthForm
        from com.sun.star.i18n.UnicodeScript import kHangulCompatibilityJamo as UNICODE_SCRIPT_kHangulCompatibilityJamo
        from com.sun.star.i18n.UnicodeScript import kHangulJamo as UNICODE_SCRIPT_kHangulJamo
        from com.sun.star.i18n.UnicodeScript import kHangulSyllable as UNICODE_SCRIPT_kHangulSyllable
        from com.sun.star.i18n.UnicodeScript import kHebrew as UNICODE_SCRIPT_kHebrew
        from com.sun.star.i18n.UnicodeScript import kHighPrivateUseSurrogate as UNICODE_SCRIPT_kHighPrivateUseSurrogate
        from com.sun.star.i18n.UnicodeScript import kHighSurrogate as UNICODE_SCRIPT_kHighSurrogate
        from com.sun.star.i18n.UnicodeScript import kHiragana as UNICODE_SCRIPT_kHiragana
        from com.sun.star.i18n.UnicodeScript import kIPAExtension as UNICODE_SCRIPT_kIPAExtension
        from com.sun.star.i18n.UnicodeScript import kIdeographicDescriptionCharacters as UNICODE_SCRIPT_kIdeographicDescriptionCharacters
        from com.sun.star.i18n.UnicodeScript import kKanbun as UNICODE_SCRIPT_kKanbun
        from com.sun.star.i18n.UnicodeScript import kKangxiRadicals as UNICODE_SCRIPT_kKangxiRadicals
        from com.sun.star.i18n.UnicodeScript import kKannada as UNICODE_SCRIPT_kKannada
        from com.sun.star.i18n.UnicodeScript import kKatakana as UNICODE_SCRIPT_kKatakana
        from com.sun.star.i18n.UnicodeScript import kKhmer as UNICODE_SCRIPT_kKhmer
        from com.sun.star.i18n.UnicodeScript import kLao as UNICODE_SCRIPT_kLao
        from com.sun.star.i18n.UnicodeScript import kLatin1Supplement as UNICODE_SCRIPT_kLatin1Supplement
        from com.sun.star.i18n.UnicodeScript import kLatinExtendedA as UNICODE_SCRIPT_kLatinExtendedA
        from com.sun.star.i18n.UnicodeScript import kLatinExtendedAdditional as UNICODE_SCRIPT_kLatinExtendedAdditional
        from com.sun.star.i18n.UnicodeScript import kLatinExtendedB as UNICODE_SCRIPT_kLatinExtendedB
        from com.sun.star.i18n.UnicodeScript import kLetterlikeSymbol as UNICODE_SCRIPT_kLetterlikeSymbol
        from com.sun.star.i18n.UnicodeScript import kLowSurrogate as UNICODE_SCRIPT_kLowSurrogate
        from com.sun.star.i18n.UnicodeScript import kMalayalam as UNICODE_SCRIPT_kMalayalam
        from com.sun.star.i18n.UnicodeScript import kMathOperator as UNICODE_SCRIPT_kMathOperator
        from com.sun.star.i18n.UnicodeScript import kMiscSymbol as UNICODE_SCRIPT_kMiscSymbol
        from com.sun.star.i18n.UnicodeScript import kMiscTechnical as UNICODE_SCRIPT_kMiscTechnical
        from com.sun.star.i18n.UnicodeScript import kMongolian as UNICODE_SCRIPT_kMongolian
        from com.sun.star.i18n.UnicodeScript import kMyanmar as UNICODE_SCRIPT_kMyanmar
        from com.sun.star.i18n.UnicodeScript import kNoScript as UNICODE_SCRIPT_kNoScript
        from com.sun.star.i18n.UnicodeScript import kNumberForm as UNICODE_SCRIPT_kNumberForm
        from com.sun.star.i18n.UnicodeScript import kOgham as UNICODE_SCRIPT_kOgham
        from com.sun.star.i18n.UnicodeScript import kOpticalCharacter as UNICODE_SCRIPT_kOpticalCharacter
        from com.sun.star.i18n.UnicodeScript import kOriya as UNICODE_SCRIPT_kOriya
        from com.sun.star.i18n.UnicodeScript import kPrivateUse as UNICODE_SCRIPT_kPrivateUse
        from com.sun.star.i18n.UnicodeScript import kRunic as UNICODE_SCRIPT_kRunic
        from com.sun.star.i18n.UnicodeScript import kScriptCount as UNICODE_SCRIPT_kScriptCount
        from com.sun.star.i18n.UnicodeScript import kSinhala as UNICODE_SCRIPT_kSinhala
        from com.sun.star.i18n.UnicodeScript import kSmallFormVariant as UNICODE_SCRIPT_kSmallFormVariant
        from com.sun.star.i18n.UnicodeScript import kSpacingModifier as UNICODE_SCRIPT_kSpacingModifier
        from com.sun.star.i18n.UnicodeScript import kSuperSubScript as UNICODE_SCRIPT_kSuperSubScript
        from com.sun.star.i18n.UnicodeScript import kSymbolCombiningMark as UNICODE_SCRIPT_kSymbolCombiningMark
        from com.sun.star.i18n.UnicodeScript import kSyriac as UNICODE_SCRIPT_kSyriac
        from com.sun.star.i18n.UnicodeScript import kTamil as UNICODE_SCRIPT_kTamil
        from com.sun.star.i18n.UnicodeScript import kTelugu as UNICODE_SCRIPT_kTelugu
        from com.sun.star.i18n.UnicodeScript import kThaana as UNICODE_SCRIPT_kThaana
        from com.sun.star.i18n.UnicodeScript import kThai as UNICODE_SCRIPT_kThai
        from com.sun.star.i18n.UnicodeScript import kTibetan as UNICODE_SCRIPT_kTibetan
        from com.sun.star.i18n.UnicodeScript import kUnifiedCanadianAboriginalSyllabics as UNICODE_SCRIPT_kUnifiedCanadianAboriginalSyllabics
        from com.sun.star.i18n.UnicodeScript import kYiRadicals as UNICODE_SCRIPT_kYiRadicals
        from com.sun.star.i18n.UnicodeScript import kYiSyllables as UNICODE_SCRIPT_kYiSyllables

        class UnicodeScript(uno.Enum):
            """
            Enum Class


            See Also:
                `API UnicodeScript <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n.html#a47be7d1d06e067d647f387cc160d5e29>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.i18n.UnicodeScript', value)

            __ooo_ns__: str = 'com.sun.star.i18n'
            __ooo_full_ns__: str = 'com.sun.star.i18n.UnicodeScript'
            __ooo_type_name__: str = 'enum'

            kAlphabeticPresentation = UNICODE_SCRIPT_kAlphabeticPresentation
            """
            """
            kArabic = UNICODE_SCRIPT_kArabic
            """
            """
            kArabicPresentationA = UNICODE_SCRIPT_kArabicPresentationA
            """
            """
            kArabicPresentationB = UNICODE_SCRIPT_kArabicPresentationB
            """
            """
            kArmenian = UNICODE_SCRIPT_kArmenian
            """
            """
            kArrow = UNICODE_SCRIPT_kArrow
            """
            """
            kBasicLatin = UNICODE_SCRIPT_kBasicLatin
            """
            """
            kBengali = UNICODE_SCRIPT_kBengali
            """
            """
            kBlockElement = UNICODE_SCRIPT_kBlockElement
            """
            """
            kBopomofo = UNICODE_SCRIPT_kBopomofo
            """
            """
            kBopomofoExtended = UNICODE_SCRIPT_kBopomofoExtended
            """
            """
            kBoxDrawing = UNICODE_SCRIPT_kBoxDrawing
            """
            """
            kBraillePatterns = UNICODE_SCRIPT_kBraillePatterns
            """
            """
            kCJKCompatibility = UNICODE_SCRIPT_kCJKCompatibility
            """
            """
            kCJKCompatibilityForm = UNICODE_SCRIPT_kCJKCompatibilityForm
            """
            """
            kCJKCompatibilityIdeograph = UNICODE_SCRIPT_kCJKCompatibilityIdeograph
            """
            """
            kCJKRadicalsSupplement = UNICODE_SCRIPT_kCJKRadicalsSupplement
            """
            """
            kCJKSymbolPunctuation = UNICODE_SCRIPT_kCJKSymbolPunctuation
            """
            """
            kCJKUnifiedIdeograph = UNICODE_SCRIPT_kCJKUnifiedIdeograph
            """
            """
            kCJKUnifiedIdeographsExtensionA = UNICODE_SCRIPT_kCJKUnifiedIdeographsExtensionA
            """
            """
            kCherokee = UNICODE_SCRIPT_kCherokee
            """
            """
            kCombiningDiacritical = UNICODE_SCRIPT_kCombiningDiacritical
            """
            """
            kCombiningHalfMark = UNICODE_SCRIPT_kCombiningHalfMark
            """
            """
            kControlPicture = UNICODE_SCRIPT_kControlPicture
            """
            """
            kCurrencySymbolScript = UNICODE_SCRIPT_kCurrencySymbolScript
            """
            """
            kCyrillic = UNICODE_SCRIPT_kCyrillic
            """
            """
            kDevanagari = UNICODE_SCRIPT_kDevanagari
            """
            """
            kDingbat = UNICODE_SCRIPT_kDingbat
            """
            """
            kEnclosedAlphanumeric = UNICODE_SCRIPT_kEnclosedAlphanumeric
            """
            """
            kEnclosedCJKLetterMonth = UNICODE_SCRIPT_kEnclosedCJKLetterMonth
            """
            """
            kEthiopic = UNICODE_SCRIPT_kEthiopic
            """
            """
            kGeneralPunctuation = UNICODE_SCRIPT_kGeneralPunctuation
            """
            """
            kGeometricShape = UNICODE_SCRIPT_kGeometricShape
            """
            """
            kGeorgian = UNICODE_SCRIPT_kGeorgian
            """
            """
            kGreek = UNICODE_SCRIPT_kGreek
            """
            """
            kGreekExtended = UNICODE_SCRIPT_kGreekExtended
            """
            """
            kGujarati = UNICODE_SCRIPT_kGujarati
            """
            """
            kGurmukhi = UNICODE_SCRIPT_kGurmukhi
            """
            """
            kHalfwidthFullwidthForm = UNICODE_SCRIPT_kHalfwidthFullwidthForm
            """
            """
            kHangulCompatibilityJamo = UNICODE_SCRIPT_kHangulCompatibilityJamo
            """
            """
            kHangulJamo = UNICODE_SCRIPT_kHangulJamo
            """
            """
            kHangulSyllable = UNICODE_SCRIPT_kHangulSyllable
            """
            """
            kHebrew = UNICODE_SCRIPT_kHebrew
            """
            """
            kHighPrivateUseSurrogate = UNICODE_SCRIPT_kHighPrivateUseSurrogate
            """
            """
            kHighSurrogate = UNICODE_SCRIPT_kHighSurrogate
            """
            """
            kHiragana = UNICODE_SCRIPT_kHiragana
            """
            """
            kIPAExtension = UNICODE_SCRIPT_kIPAExtension
            """
            """
            kIdeographicDescriptionCharacters = UNICODE_SCRIPT_kIdeographicDescriptionCharacters
            """
            """
            kKanbun = UNICODE_SCRIPT_kKanbun
            """
            """
            kKangxiRadicals = UNICODE_SCRIPT_kKangxiRadicals
            """
            """
            kKannada = UNICODE_SCRIPT_kKannada
            """
            """
            kKatakana = UNICODE_SCRIPT_kKatakana
            """
            """
            kKhmer = UNICODE_SCRIPT_kKhmer
            """
            """
            kLao = UNICODE_SCRIPT_kLao
            """
            """
            kLatin1Supplement = UNICODE_SCRIPT_kLatin1Supplement
            """
            """
            kLatinExtendedA = UNICODE_SCRIPT_kLatinExtendedA
            """
            """
            kLatinExtendedAdditional = UNICODE_SCRIPT_kLatinExtendedAdditional
            """
            """
            kLatinExtendedB = UNICODE_SCRIPT_kLatinExtendedB
            """
            """
            kLetterlikeSymbol = UNICODE_SCRIPT_kLetterlikeSymbol
            """
            """
            kLowSurrogate = UNICODE_SCRIPT_kLowSurrogate
            """
            """
            kMalayalam = UNICODE_SCRIPT_kMalayalam
            """
            """
            kMathOperator = UNICODE_SCRIPT_kMathOperator
            """
            """
            kMiscSymbol = UNICODE_SCRIPT_kMiscSymbol
            """
            """
            kMiscTechnical = UNICODE_SCRIPT_kMiscTechnical
            """
            """
            kMongolian = UNICODE_SCRIPT_kMongolian
            """
            """
            kMyanmar = UNICODE_SCRIPT_kMyanmar
            """
            """
            kNoScript = UNICODE_SCRIPT_kNoScript
            """
            """
            kNumberForm = UNICODE_SCRIPT_kNumberForm
            """
            """
            kOgham = UNICODE_SCRIPT_kOgham
            """
            """
            kOpticalCharacter = UNICODE_SCRIPT_kOpticalCharacter
            """
            """
            kOriya = UNICODE_SCRIPT_kOriya
            """
            """
            kPrivateUse = UNICODE_SCRIPT_kPrivateUse
            """
            """
            kRunic = UNICODE_SCRIPT_kRunic
            """
            """
            kScriptCount = UNICODE_SCRIPT_kScriptCount
            """
            """
            kSinhala = UNICODE_SCRIPT_kSinhala
            """
            """
            kSmallFormVariant = UNICODE_SCRIPT_kSmallFormVariant
            """
            """
            kSpacingModifier = UNICODE_SCRIPT_kSpacingModifier
            """
            """
            kSuperSubScript = UNICODE_SCRIPT_kSuperSubScript
            """
            """
            kSymbolCombiningMark = UNICODE_SCRIPT_kSymbolCombiningMark
            """
            """
            kSyriac = UNICODE_SCRIPT_kSyriac
            """
            """
            kTamil = UNICODE_SCRIPT_kTamil
            """
            """
            kTelugu = UNICODE_SCRIPT_kTelugu
            """
            """
            kThaana = UNICODE_SCRIPT_kThaana
            """
            """
            kThai = UNICODE_SCRIPT_kThai
            """
            """
            kTibetan = UNICODE_SCRIPT_kTibetan
            """
            """
            kUnifiedCanadianAboriginalSyllabics = UNICODE_SCRIPT_kUnifiedCanadianAboriginalSyllabics
            """
            """
            kYiRadicals = UNICODE_SCRIPT_kYiRadicals
            """
            """
            kYiSyllables = UNICODE_SCRIPT_kYiSyllables
            """
            """
    else:
        # keep document generators happy
        from ...lo.i18n.unicode_script import UnicodeScript as UnicodeScript


__all__ = ['UnicodeScript']
