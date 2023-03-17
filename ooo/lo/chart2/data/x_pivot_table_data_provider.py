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
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2.data
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .pivot_table_field_entry import PivotTableFieldEntry as PivotTableFieldEntry_81a11104
    from .x_data_sequence import XDataSequence as XDataSequence_11f00e1f

class XPivotTableDataProvider(XInterface_8f010a43):
    """
    Data provider specific for pivot chart data.
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API XPivotTableDataProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XPivotTableDataProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.XPivotTableDataProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.data.XPivotTableDataProvider'

    @abstractmethod
    def createDataSequenceOfCategories(self) -> 'XDataSequence_11f00e1f':
        """
        creates a single data sequence of categories.
        """
        ...
    @abstractmethod
    def createDataSequenceOfLabelsByIndex(self, nIndex: int) -> 'XDataSequence_11f00e1f':
        """
        creates a single data sequence of label(s) for the given data series index.
        """
        ...
    @abstractmethod
    def createDataSequenceOfValuesByIndex(self, nIndex: int) -> 'XDataSequence_11f00e1f':
        """
        creates a single data sequence of values for the given data series index.
        """
        ...
    @abstractmethod
    def getColumnFields(self) -> 'typing.Tuple[PivotTableFieldEntry_81a11104, ...]':
        """
        names of column fields from the associated pivot table
        """
        ...
    @abstractmethod
    def getDataFields(self) -> 'typing.Tuple[PivotTableFieldEntry_81a11104, ...]':
        """
        names of data fields from the associated pivot table
        """
        ...
    @abstractmethod
    def getFieldOutputDescription(self, nDimensionIndex: int) -> str:
        """
        field output description: either \"- all -\", \"- multiple -\", or specific value
        """
        ...
    @abstractmethod
    def getPageFields(self) -> 'typing.Tuple[PivotTableFieldEntry_81a11104, ...]':
        """
        names of page fields from the associated pivot table
        """
        ...
    @abstractmethod
    def getPivotTableName(self) -> str:
        """
        get the associated pivot table name
        """
        ...
    @abstractmethod
    def getRowFields(self) -> 'typing.Tuple[PivotTableFieldEntry_81a11104, ...]':
        """
        names of row fields from the associated pivot table
        """
        ...
    @abstractmethod
    def hasPivotTable(self) -> bool:
        """
        check if the associated pivot table exists
        """
        ...
    @abstractmethod
    def setPivotTableName(self, sPivotTableName: str) -> None:
        """
        set the associated pivot table name
        """
        ...

__all__ = ['XPivotTableDataProvider']

