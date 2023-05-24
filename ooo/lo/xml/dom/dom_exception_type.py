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
# Namespace: com.sun.star.xml.dom
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.xml.dom.DOMExceptionType import DOMExceptionTypeProto

class DOMExceptionType(Enum):
    """
    Enum Class

    ENUM DOMExceptionType

    See Also:
        `API DOMExceptionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom.html#a31e3fb46d584de1cfc4b4c7640a41239>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.DOMExceptionType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.xml.dom.DOMExceptionType'

    DOMSTRING_SIZE_ERR = cast(DOMExceptionTypeProto, 'DOMSTRING_SIZE_ERR')
    """
    """
    HIERARCHY_REQUEST_ERR = cast(DOMExceptionTypeProto, 'HIERARCHY_REQUEST_ERR')
    """
    """
    INDEX_SIZE_ERR = cast(DOMExceptionTypeProto, 'INDEX_SIZE_ERR')
    """
    """
    INUSE_ATTRIBUTE_ERR = cast(DOMExceptionTypeProto, 'INUSE_ATTRIBUTE_ERR')
    """
    """
    INVALID_ACCESS_ERR = cast(DOMExceptionTypeProto, 'INVALID_ACCESS_ERR')
    """
    """
    INVALID_CHARACTER_ERR = cast(DOMExceptionTypeProto, 'INVALID_CHARACTER_ERR')
    """
    """
    INVALID_MODIFICATION_ERR = cast(DOMExceptionTypeProto, 'INVALID_MODIFICATION_ERR')
    """
    """
    INVALID_STATE_ERR = cast(DOMExceptionTypeProto, 'INVALID_STATE_ERR')
    """
    """
    NAMESPACE_ERR = cast(DOMExceptionTypeProto, 'NAMESPACE_ERR')
    """
    """
    NOT_FOUND_ERR = cast(DOMExceptionTypeProto, 'NOT_FOUND_ERR')
    """
    """
    NOT_SUPPORTED_ERR = cast(DOMExceptionTypeProto, 'NOT_SUPPORTED_ERR')
    """
    """
    NO_DATA_ALLOWED_ERR = cast(DOMExceptionTypeProto, 'NO_DATA_ALLOWED_ERR')
    """
    """
    NO_MODIFICATION_ALLOWED_ERR = cast(DOMExceptionTypeProto, 'NO_MODIFICATION_ALLOWED_ERR')
    """
    """
    SYNTAX_ERR = cast(DOMExceptionTypeProto, 'SYNTAX_ERR')
    """
    """
    WRONG_DOCUMENT_ERR = cast(DOMExceptionTypeProto, 'WRONG_DOCUMENT_ERR')
    """
    """

__all__ = ['DOMExceptionType']

