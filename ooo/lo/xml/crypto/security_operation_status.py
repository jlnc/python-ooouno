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
# Namespace: com.sun.star.xml.crypto
# Libre Office Version: 7.4
from enum import Enum


class SecurityOperationStatus(Enum):
    """
    Enum Class

    

    See Also:
        `API SecurityOperationStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto.html#ab5d887eb5da1173b766d96d0d863d1dc>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.SecurityOperationStatus'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.xml.crypto.SecurityOperationStatus'

    ASSERTION = 'ASSERTION'
    """
    """
    CERT_HAS_EXPIRED = 'CERT_HAS_EXPIRED'
    """
    """
    CERT_ISSUER_FAILED = 'CERT_ISSUER_FAILED'
    """
    """
    CERT_NOT_FOUND = 'CERT_NOT_FOUND'
    """
    """
    CERT_NOT_YET_VALID = 'CERT_NOT_YET_VALID'
    """
    """
    CERT_REVOKED = 'CERT_REVOKED'
    """
    """
    CERT_VERIFY_FAILED = 'CERT_VERIFY_FAILED'
    """
    """
    CRYPTO_FAILED = 'CRYPTO_FAILED'
    """
    """
    DATA_NOT_MATCH = 'DATA_NOT_MATCH'
    """
    """
    DISABLED = 'DISABLED'
    """
    """
    DSIG_INVALID_REFERENCE = 'DSIG_INVALID_REFERENCE'
    """
    """
    DSIG_NO_REFERENCES = 'DSIG_NO_REFERENCES'
    """
    """
    ENGINE_FAILED = 'ENGINE_FAILED'
    """
    The following constants are derived from XMLSec error definitions, as following:
    
    XMLSEC_ERRORS_R_XMLSEC_FAILED XMLSEC_ERRORS_R_MALLOC_FAILED XMLSEC_ERRORS_R_STRDUP_FAILED XMLSEC_ERRORS_R_CRYPTO_FAILED XMLSEC_ERRORS_R_XML_FAILED XMLSEC_ERRORS_R_XSLT_FAILED XMLSEC_ERRORS_R_IO_FAILED XMLSEC_ERRORS_R_DISABLED XMLSEC_ERRORS_R_NOT_IMPLEMENTED XMLSEC_ERRORS_R_INVALID_SIZE XMLSEC_ERRORS_R_INVALID_DATA XMLSEC_ERRORS_R_INVALID_RESULT XMLSEC_ERRORS_R_INVALID_TYPE XMLSEC_ERRORS_R_INVALID_OPERATION XMLSEC_ERRORS_R_INVALID_STATUS XMLSEC_ERRORS_R_INVALID_FORMAT XMLSEC_ERRORS_R_DATA_NOT_MATCH XMLSEC_ERRORS_R_INVALID_NODE XMLSEC_ERRORS_R_INVALID_NODE_CONTENT XMLSEC_ERRORS_R_INVALID_NODE_ATTRIBUTE XMLSEC_ERRORS_R_MISSING_NODE_ATTRIBUTE XMLSEC_ERRORS_R_NODE_ALREADY_PRESENT XMLSEC_ERRORS_R_UNEXPECTED_NODE XMLSEC_ERRORS_R_NODE_NOT_FOUND XMLSEC_ERRORS_R_INVALID_TRANSFORM XMLSEC_ERRORS_R_INVALID_TRANSFORM_KEY XMLSEC_ERRORS_R_INVALID_URI_TYPE XMLSEC_ERRORS_R_TRANSFORM_SAME_DOCUMENT_REQUIRED XMLSEC_ERRORS_R_TRANSFORM_DISABLED XMLSEC_ERRORS_R_INVALID_KEY_DATA XMLSEC_ERRORS_R_KEY_DATA_NOT_FOUND XMLSEC_ERRORS_R_KEY_DATA_ALREADY_EXIST XMLSEC_ERRORS_R_INVALID_KEY_DATA_SIZE XMLSEC_ERRORS_R_KEY_NOT_FOUND XMLSEC_ERRORS_R_KEYDATA_DISABLED XMLSEC_ERRORS_R_MAX_RETRIEVALS_LEVEL XMLSEC_ERRORS_R_MAX_RETRIEVAL_TYPE_MISMATCH XMLSEC_ERRORS_R_MAX_ENCKEY_LEVEL XMLSEC_ERRORS_R_CERT_VERIFY_FAILED XMLSEC_ERRORS_R_CERT_NOT_FOUND XMLSEC_ERRORS_R_CERT_REVOKED XMLSEC_ERRORS_R_CERT_ISSUER_FAILED XMLSEC_ERRORS_R_CERT_NOT_YET_VALID XMLSEC_ERRORS_R_CERT_HAS_EXPIRED XMLSEC_ERRORS_R_DSIG_NO_REFERENCES XMLSEC_ERRORS_R_DSIG_INVALID_REFERENCE XMLSEC_ERRORS_R_ASSERTION XMLSEC_ERRORS_MAX_NUMBER
    """
    INVALID_DATA = 'INVALID_DATA'
    """
    """
    INVALID_FORMAT = 'INVALID_FORMAT'
    """
    """
    INVALID_KEY_DATA = 'INVALID_KEY_DATA'
    """
    """
    INVALID_KEY_DATA_SIZE = 'INVALID_KEY_DATA_SIZE'
    """
    """
    INVALID_NODE = 'INVALID_NODE'
    """
    """
    INVALID_NODE_ATTRIBUTE = 'INVALID_NODE_ATTRIBUTE'
    """
    """
    INVALID_NODE_CONTENT = 'INVALID_NODE_CONTENT'
    """
    """
    INVALID_OPERATION = 'INVALID_OPERATION'
    """
    """
    INVALID_RESULT = 'INVALID_RESULT'
    """
    """
    INVALID_SIZE = 'INVALID_SIZE'
    """
    """
    INVALID_STATUS = 'INVALID_STATUS'
    """
    """
    INVALID_TRANSFORM = 'INVALID_TRANSFORM'
    """
    """
    INVALID_TRANSFORM_KEY = 'INVALID_TRANSFORM_KEY'
    """
    """
    INVALID_TYPE = 'INVALID_TYPE'
    """
    """
    INVALID_URI_TYPE = 'INVALID_URI_TYPE'
    """
    """
    IO_FAILED = 'IO_FAILED'
    """
    """
    KEYDATA_DISABLED = 'KEYDATA_DISABLED'
    """
    """
    KEY_DATA_ALREADY_EXIST = 'KEY_DATA_ALREADY_EXIST'
    """
    """
    KEY_DATA_NOT_FOUND = 'KEY_DATA_NOT_FOUND'
    """
    """
    KEY_NOT_FOUND = 'KEY_NOT_FOUND'
    """
    """
    MALLOC_FAILED = 'MALLOC_FAILED'
    """
    """
    MAX_ENCKEY_LEVEL = 'MAX_ENCKEY_LEVEL'
    """
    """
    MAX_RETRIEVALS_LEVEL = 'MAX_RETRIEVALS_LEVEL'
    """
    """
    MAX_RETRIEVAL_TYPE_MISMATCH = 'MAX_RETRIEVAL_TYPE_MISMATCH'
    """
    """
    MISSING_NODE_ATTRIBUTE = 'MISSING_NODE_ATTRIBUTE'
    """
    """
    NODE_ALREADY_PRESENT = 'NODE_ALREADY_PRESENT'
    """
    """
    NODE_NOT_FOUND = 'NODE_NOT_FOUND'
    """
    """
    NOT_IMPLEMENTED = 'NOT_IMPLEMENTED'
    """
    """
    OPERATION_SUCCEEDED = 'OPERATION_SUCCEEDED'
    """
    """
    RUNTIMEERROR_FAILED = 'RUNTIMEERROR_FAILED'
    """
    """
    STRDUP_FAILED = 'STRDUP_FAILED'
    """
    """
    TRANSFORM_DISABLED = 'TRANSFORM_DISABLED'
    """
    """
    TRANSFORM_SAME_DOCUMENT_REQUIRED = 'TRANSFORM_SAME_DOCUMENT_REQUIRED'
    """
    """
    UNEXPECTED_NODE = 'UNEXPECTED_NODE'
    """
    """
    UNKNOWN = 'UNKNOWN'
    """
    """
    XML_FAILED = 'XML_FAILED'
    """
    """
    XSLT_FAILED = 'XSLT_FAILED'
    """
    """

__all__ = ['SecurityOperationStatus']

