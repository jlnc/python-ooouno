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
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from abc import abstractmethod
from .data.x_data_provider import XDataProvider as XDataProvider_122f0e31
if typing.TYPE_CHECKING:
    from .data.x_data_sequence import XDataSequence as XDataSequence_11f00e1f

class XInternalDataProvider(XDataProvider_122f0e31):
    """
    An internal DataProvider that has more access to data than a plain DataProvider.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XInternalDataProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XInternalDataProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XInternalDataProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XInternalDataProvider'

    @abstractmethod
    def appendSequence(self) -> None:
        """
        same as insertSequence with nAfterIndex being the largest current index of the data, i.e.
        
        (size - 1)
        """
        ...
    @abstractmethod
    def deleteComplexCategoryLevel(self, nLevel: int) -> None:
        """
        deletes an additional sequence for categories at nLevel>=1; categories at level 0 are always present and cannot be deleted
        
        **since**
        
            OOo 3.3
        """
        ...
    @abstractmethod
    def deleteDataPointForAllSequences(self, nAtIndex: int) -> None:
        """
        """
        ...
    @abstractmethod
    def deleteSequence(self, nAtIndex: int) -> None:
        """
        """
        ...
    @abstractmethod
    def getDataByRangeRepresentation(self, aRange: str) -> typing.Tuple[object, ...]:
        """
        """
        ...
    @abstractmethod
    def hasDataByRangeRepresentation(self, aRange: str) -> bool:
        """
        """
        ...
    @abstractmethod
    def insertComplexCategoryLevel(self, nLevel: int) -> None:
        """
        insert an additional sequence for categories nLevel>=1; categories at level 0 are always present and cannot be inserted or deleted
        
        **since**
        
            OOo 3.3
        """
        ...
    @abstractmethod
    def insertDataPointForAllSequences(self, nAfterIndex: int) -> None:
        """
        """
        ...
    @abstractmethod
    def insertSequence(self, nAfterIndex: int) -> None:
        """
        """
        ...
    @abstractmethod
    def registerDataSequenceForChanges(self, xSeq: XDataSequence_11f00e1f) -> None:
        """
        If range representations of data sequences change due to internal structural changes, they must be registered at the data provider.
        
        Sequences that are directly retrieved via the methods of the XDataProvider interface are already registered. If a labeled data sequence was created by cloning an existing one, it has to be explicitly registered via this method.
        """
        ...
    @abstractmethod
    def setDataByRangeRepresentation(self, aRange: str, aNewData: typing.Tuple[object, ...]) -> None:
        """
        """
        ...
    @abstractmethod
    def swapDataPointWithNextOneForAllSequences(self, nAtIndex: int) -> None:
        """
        """
        ...

__all__ = ['XInternalDataProvider']

