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
# Libre Office Version: 7.3
# Namespace: com.sun.star.document
from abc import abstractmethod
from .x_document_properties import XDocumentProperties as XDocumentProperties_4c31102b

class DocumentProperties(XDocumentProperties_4c31102b):
    """
    Service Class

    provides document-specific information such as the author, creation date, and user-defined fields.
    
    This service replaces the deprecated DocumentInfo and StandaloneDocumentInfo services.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DocumentProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1DocumentProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.DocumentProperties'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self) -> None:
        """
        constructs default-initialized instance
        """


__all__ = ['DocumentProperties']

