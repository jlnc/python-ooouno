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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.smarttags
import typing
from abc import abstractmethod, abstractproperty
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
if typing.TYPE_CHECKING:
    from ..frame.x_controller import XController as XController_b00e0b8f
    from ..i18n.x_break_iterator import XBreakIterator as XBreakIterator_bf270bcf
    from ..lang.locale import Locale as Locale_70d308fa
    from .smart_tag_recognizer_mode import SmartTagRecognizerMode as SmartTagRecognizerMode_9179119e
    from ..text.x_text_markup import XTextMarkup as XTextMarkup_a5d60b3a

class XSmartTagRecognizer(XInitialization_d46c0cca):
    """
    provides access to a smart tag recognizer.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XSmartTagRecognizer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1smarttags_1_1XSmartTagRecognizer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.smarttags'
    __ooo_full_ns__: str = 'com.sun.star.smarttags.XSmartTagRecognizer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.smarttags.XSmartTagRecognizer'

    @abstractmethod
    def displayPropertyPage(self, nSmartTagIndex: int, aLocale: 'Locale_70d308fa') -> None:
        """
        launches the property page for a smart tag type.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getDescription(self, aLocale: 'Locale_70d308fa') -> str:
        """
        obtains a detailed description of this recognizer component.
        """
    @abstractmethod
    def getName(self, aLocale: 'Locale_70d308fa') -> str:
        """
        obtains a name that describes this recognizer component.
        """
    @abstractmethod
    def getSmartTagDownloadURL(self, nSmartTagIndex: int) -> str:
        """
        obtains the URL that can be used to download new or updated recognizers.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getSmartTagName(self, nSmartTagIndex: int) -> str:
        """
        obtains the name of one specific smart tag type supported by this recognizer component.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def hasPropertyPage(self, nSmartTagIndex: int, aLocale: 'Locale_70d308fa') -> bool:
        """
        indicates whether there is a property page for a smart tag type.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def recognize(self, aText: str, nStart: int, nLength: int, eDataType: 'SmartTagRecognizerMode_9179119e', aLocale: 'Locale_70d308fa', xTextMarkup: 'XTextMarkup_a5d60b3a', aApplicationName: str, xController: 'XController_b00e0b8f', xTokenizer: 'XBreakIterator_bf270bcf') -> None:
        """
        recognizes smart tags.
        """
    @abstractproperty
    def SmartTagCount(self) -> int:
        """
        The number of smart tag types supported by this recognizer component.
        """


__all__ = ['XSmartTagRecognizer']

