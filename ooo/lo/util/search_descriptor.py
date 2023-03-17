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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
from abc import abstractproperty
from .x_search_descriptor import XSearchDescriptor as XSearchDescriptor_ef600d93

class SearchDescriptor(XSearchDescriptor_ef600d93):
    """
    Service Class

    describes what and how to search within a container.
    
    **since**
    
        LibreOffice 5.2

    See Also:
        `API SearchDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1SearchDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.SearchDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SearchBackwards(self) -> bool:
        """
        If TRUE, the search is done backwards in the document.
        """
        ...

    @abstractproperty
    def SearchCaseSensitive(self) -> bool:
        """
        If TRUE, the case of the letters is important for the match.
        """
        ...

    @abstractproperty
    def SearchRegularExpression(self) -> bool:
        """
        If TRUE, the search string is evaluated as a regular expression.
        
        SearchRegularExpression, SearchWildcard and SearchSimilarity are mutually exclusive, only one can be TRUE at the same time.
        """
        ...

    @abstractproperty
    def SearchSimilarity(self) -> bool:
        """
        If TRUE, a \"similarity search\" is performed.
        
        In the case of a similarity search, the following properties specify the kind of similarity:
        
        SearchRegularExpression, SearchWildcard and SearchSimilarity are mutually exclusive, only one can be TRUE at the same time.
        """
        ...

    @abstractproperty
    def SearchSimilarityAdd(self) -> int:
        """
        specifies the number of characters that must be added to match the search pattern.
        """
        ...

    @abstractproperty
    def SearchSimilarityExchange(self) -> int:
        """
        This property specifies the number of characters that must be replaced to match the search pattern.
        """
        ...

    @abstractproperty
    def SearchSimilarityRelax(self) -> bool:
        """
        If TRUE, all similarity rules are applied together.
        
        In the case of a relaxed similarity search, the following properties are applied together:
        """
        ...

    @abstractproperty
    def SearchSimilarityRemove(self) -> int:
        """
        This property specifies the number of characters that may be ignored to match the search pattern.
        """
        ...

    @abstractproperty
    def SearchStyles(self) -> bool:
        """
        If TRUE, it is searched for positions where the paragraph style with the name of the search pattern is applied.
        """
        ...

    @abstractproperty
    def SearchWildcard(self) -> bool:
        """
        If TRUE, the search string is evaluated as a wildcard pattern.
        
        Wildcards are '*' (asterisk) for any sequence of characters, including an empty sequence, and '?' (question mark) for exactly one character. Escape character is '\\' (U+005C REVERSE SOLIDUS) aka backslash, it escapes the special meaning of a question mark, asterisk or escape character that follows immediately after the escape character.
        
        SearchRegularExpression, SearchWildcard and SearchSimilarity are mutually exclusive, only one can be TRUE at the same time.
        
        **since**
        
            LibreOffice 5.2
        """
        ...

    @abstractproperty
    def SearchWords(self) -> bool:
        """
        If TRUE, only complete words will be found.
        """
        ...



__all__ = ['SearchDescriptor']

