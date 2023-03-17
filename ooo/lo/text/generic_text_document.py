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
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..document.office_document import OfficeDocument as OfficeDocument_fecd0df2
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from ..style.x_style_families_supplier import XStyleFamiliesSupplier as XStyleFamiliesSupplier_4c5a1020
from .x_bookmarks_supplier import XBookmarksSupplier as XBookmarksSupplier_ffa50e22
from .x_chapter_numbering_supplier import XChapterNumberingSupplier as XChapterNumberingSupplier_6bb310e7
from .x_document_indexes_supplier import XDocumentIndexesSupplier as XDocumentIndexesSupplier_5b991088
from .x_endnotes_supplier import XEndnotesSupplier as XEndnotesSupplier_f19c0db9
from .x_footnotes_supplier import XFootnotesSupplier as XFootnotesSupplier_1050e3a
from .x_page_printable import XPagePrintable as XPagePrintable_c8670c43
from .x_reference_marks_supplier import XReferenceMarksSupplier as XReferenceMarksSupplier_49d81006
from .x_text_document import XTextDocument as XTextDocument_bd4b0c09
from .x_text_embedded_objects_supplier import XTextEmbeddedObjectsSupplier as XTextEmbeddedObjectsSupplier_9dd211f2
from .x_text_fields_supplier import XTextFieldsSupplier as XTextFieldsSupplier_d5d0e75
from .x_text_frames_supplier import XTextFramesSupplier as XTextFramesSupplier_db70e7c
from .x_text_graphic_objects_supplier import XTextGraphicObjectsSupplier as XTextGraphicObjectsSupplier_8df111a6
from .x_text_sections_supplier import XTextSectionsSupplier as XTextSectionsSupplier_2ce60f66
from .x_text_tables_supplier import XTextTablesSupplier as XTextTablesSupplier_d9f0e79
from ..tiledrendering.x_tiled_renderable import XTiledRenderable as XTiledRenderable_7efc1116
from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81
from ..util.x_replaceable import XReplaceable as XReplaceable_b0750b6e
from ..util.x_searchable import XSearchable as XSearchable_a4e80b08
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class GenericTextDocument(OfficeDocument_fecd0df2, XPropertySet_bc180bfa, XMultiServiceFactory_191e0eb6, XStyleFamiliesSupplier_4c5a1020, XBookmarksSupplier_ffa50e22, XChapterNumberingSupplier_6bb310e7, XDocumentIndexesSupplier_5b991088, XEndnotesSupplier_f19c0db9, XFootnotesSupplier_1050e3a, XPagePrintable_c8670c43, XReferenceMarksSupplier_49d81006, XTextDocument_bd4b0c09, XTextEmbeddedObjectsSupplier_9dd211f2, XTextFieldsSupplier_d5d0e75, XTextFramesSupplier_db70e7c, XTextGraphicObjectsSupplier_8df111a6, XTextSectionsSupplier_2ce60f66, XTextTablesSupplier_d9f0e79, XTiledRenderable_7efc1116, XNumberFormatsSupplier_3afb0fb7, XRefreshable_b0d60b81, XReplaceable_b0750b6e, XSearchable_a4e80b08):
    """
    Service Class

    A text document is a model component which contains text structured by paragraphs.
    
    Each paragraph and each portion of text can be fitted with some attributes (technically properties).
    
    It's declared as generic text document, because its function is needed by different derived services (TextDocument/WebDocument/GlobalDocument).
    
    In addition, all text objects can be searched.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API GenericTextDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1GenericTextDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.GenericTextDocument'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CharLocale(self) -> 'Locale_70d308fa':
        """
        contains the identifier of the default locale of the document.
        """
        ...

    @abstractproperty
    def CharacterCount(self) -> int:
        """
        contains the count of all characters in the document.
        """
        ...

    @abstractproperty
    def IndexAutoMarkFileURL(self) -> str:
        """
        specifies the concordance file taken into account when creating an index.
        
        When no concordance file should be used the string is empty. Used for text documents only.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @abstractproperty
    def ParagraphCount(self) -> int:
        """
        contains the count of all paragraphs in the document.
        """
        ...

    @abstractproperty
    def RecordChanges(self) -> bool:
        """
        specifies if change recording is active.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @abstractproperty
    def TwoDigitYear(self) -> int:
        """
        specifies the first 4 digit year to be used when years are given in 2 digits.
        
        Example: if set to 1930 Oct-12-29 will be interpreted as Oct-12-2029 Oct-12-30 will be interpreted as Oct-12-1930 Oct-12-02 will be interpreted as Oct-12-2002
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @abstractproperty
    def WordCount(self) -> int:
        """
        contains the count of all words in the document.
        """
        ...

    @abstractproperty
    def WordSeparator(self) -> str:
        """
        contains a string that consists of characters that mark the separation of words in counting the words in a document.
        
        I.e. slash and backslash. Whitespace (tab stop, space, paragraph break, line break) always separate words.
        """
        ...



__all__ = ['GenericTextDocument']

