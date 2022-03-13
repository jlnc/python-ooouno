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
# Namespace: com.sun.star.awt.grid
import typing
from abc import abstractmethod, abstractproperty
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...util.x_cloneable import XCloneable as XCloneable_99d00aa3

class XGridDataModel(XComponent_98dc0ab5, XCloneable_99d00aa3):
    """
    An instance of this interface is used by the UnoControlGrid to retrieve the content data that is displayed in the actual control.
    
    If you do not need your own model implementation, you can also use the DefaultGridDataModel.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridDataModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridDataModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XGridDataModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridDataModel'

    @abstractmethod
    def getCellData(self, Column: int, RowIndex: int) -> object:
        """
        retrieves the data for a given cell

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getCellToolTip(self, Column: int, RowIndex: int) -> object:
        """
        retrieves the tool tip to be displayed when the mouse hovers over a given cell
        
        At the moment, only string tool tips are supported.
        
        If VOID is returned here, the cell's content will be displayed as tip, but only if it does not fit into the cell.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getRowData(self, RowIndex: int) -> 'typing.Tuple[object, ...]':
        """
        retrieves the data for a complete row
        
        This method is provided for performance and convenience reasons, it delivers the same result as subsequent calls to getCellData() would.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getRowHeading(self, RowIndex: int) -> object:
        """
        retrieves the heading of a given row
        
        A grid control will usually paint a row's title in the header column of the respective row.
        
        At the moment, only strings are supported as row headings.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractproperty
    def ColumnCount(self) -> int:
        """
        denotes the number of columns for which the model can provide data
        """

    @abstractproperty
    def RowCount(self) -> int:
        """
        denotes the number of rows for which the model can provide data
        """


__all__ = ['XGridDataModel']

