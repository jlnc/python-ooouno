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
# Namespace: com.sun.star.sheet
from __future__ import annotations
from abc import abstractmethod
from .x_sheet_cell_range import XSheetCellRange as XSheetCellRange_e09d0cdf

class XSheetCellCursor(XSheetCellRange_e09d0cdf):
    """
    provides advanced methods to control the position of a cursor in a spreadsheet.

    See Also:
        `API XSheetCellCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetCellCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetCellCursor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetCellCursor'

    @abstractmethod
    def collapseToCurrentArray(self) -> None:
        """
        collapses the cursor into the range of the array formula to which it is currently pointing.
        
        To get the correct result, the top left cell of the original cursor must point to any cell containing an array formula. If not, the cursor is left unchanged.
        """
        ...
    @abstractmethod
    def collapseToCurrentRegion(self) -> None:
        """
        expands the cursor into the region containing the cells to which it currently points.
        
        A region is a cell range bounded by empty cells.
        """
        ...
    @abstractmethod
    def collapseToMergedArea(self) -> None:
        """
        expands the cursor to merged cell ranges.
        
        Expands the current cursor range in a way so that all merged cell ranges intersecting the current range will fit completely. If the cursor does not point to any range with merged cells, it is left unchanged.
        """
        ...
    @abstractmethod
    def collapseToSize(self, nColumns: int, nRows: int) -> None:
        """
        changes the size of a cursor range.
        
        The top left cell of the cursor keeps unmodified.
        """
        ...
    @abstractmethod
    def expandToEntireColumns(self) -> None:
        """
        expands the cursor to include the entire columns of the cells to which it is currently pointing.
        """
        ...
    @abstractmethod
    def expandToEntireRows(self) -> None:
        """
        expands the cursor to include the entire rows of the cells to which it is currently pointing.
        """
        ...

__all__ = ['XSheetCellCursor']

