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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..table.table_sort_descriptor2 import TableSortDescriptor2 as TableSortDescriptor2_27e00ef1
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class SheetSortDescriptor2(TableSortDescriptor2_27e00ef1):
    """
    Service Class

    a description of how a cell range is to be sorted.
    
    This service extends the com.sun.star.table.TableSortDescriptor2 service with spreadsheet specific properties.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SheetSortDescriptor2 <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetSortDescriptor2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SheetSortDescriptor2'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BindFormatsToContent(self) -> bool:
        """
        specifies if cell formats are moved with the contents they belong to.
        """
        ...

    @abstractproperty
    def ContainsHeader(self) -> bool:
        """
        specifies whether the first row or column (depending on com.sun.star.table.TableSortDescriptor.Orientation) is a header which should not be sorted.
        """
        ...

    @abstractproperty
    def CopyOutputData(self) -> bool:
        """
        specifies if the sorted data should be copied to another position in the document.
        """
        ...

    @abstractproperty
    def IsUserListEnabled(self) -> bool:
        """
        specifies if a user defined sorting list is used.
        """
        ...

    @abstractproperty
    def OutputPosition(self) -> 'CellAddress_ae5f0b56':
        """
        specifies the position where sorted data are to be copied.
        
        This property is only used, if SheetSortDescriptor.CopyOutputData is TRUE.
        """
        ...

    @abstractproperty
    def UserListIndex(self) -> int:
        """
        specifies which user defined sorting list is used.
        
        This property is only used, if SheetSortDescriptor.IsUserListEnabled is TRUE.
        """
        ...



__all__ = ['SheetSortDescriptor2']

