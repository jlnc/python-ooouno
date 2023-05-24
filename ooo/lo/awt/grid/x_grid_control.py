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
# Namespace: com.sun.star.awt.grid
from __future__ import annotations
from abc import abstractmethod, ABC

class XGridControl(ABC):
    """
    An interface to a control that displays a tabular data.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XGridControl'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridControl'

    @abstractmethod
    def getColumnAtPoint(self, X: int, Y: int) -> int:
        """
        retrieves the column which a given point belongs to
        """
        ...
    @abstractmethod
    def getCurrentColumn(self) -> int:
        """
        returns the column index of the currently active cell
        
        If the grid control's does not contain any cells (which happens if the grid column model does not contain any columns, or if grid data model does not contain any rows), then -1 is returned.
        """
        ...
    @abstractmethod
    def getCurrentRow(self) -> int:
        """
        returns the row index of the currently active cell
        
        If the grid control's does not contain any cells (which happens if the grid column model does not contain any columns, or if grid data model does not contain any rows), then -1 is returned.
        """
        ...
    @abstractmethod
    def getRowAtPoint(self, X: int, Y: int) -> int:
        """
        retrieves the row which a given point belongs to
        """
        ...
    @abstractmethod
    def goToCell(self, ColumnIndex: int, RowIndex: int) -> None:
        """
        moves the cursor to the given cell

        Raises:
            : ````
            com.sun.star.util.VetoException: ``VetoException``
        """
        ...

__all__ = ['XGridControl']

