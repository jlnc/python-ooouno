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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .x_office_database_document import XOfficeDatabaseDocument as XOfficeDatabaseDocument_327f0f39

class XDocumentDataSource(ABC):
    """
    simplifies the accessing of data sources and their corresponding database document.
    
    The interface can be used to access the data source of the database document.

    See Also:
        `API XDocumentDataSource <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XDocumentDataSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XDocumentDataSource'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XDocumentDataSource'

    @abstractproperty
    def DatabaseDocument(self) -> XOfficeDatabaseDocument_327f0f39:
        """
        provides access to the one and only OfficeDatabaseDocument which the data source is based on.
        
        The component returned by this attribute is an OfficeDatabaseDocument.
        
        Though there is a 1-to-1 relationship between database documents and data sources, each of the two can exist without its counterpart, but create this counterpart on request only. As a consequence, the document obtained via this attribute might be newly created, which implies that the caller is now responsible for it. In particular, the caller is responsible for calling com.sun.star.util.XCloseable.close() on the document as soon as it's not needed anymore.
        
        Additionally, if the caller does long-lasting processing on the document, it's advised to add itself as com.sun.star.util.XCloseListener to the document, to prevent closing as long as the processing lasts.
        """
        ...


__all__ = ['XDocumentDataSource']

