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
    from .x_data_sequence import XDataSequence as XDataSequence_11f00e1f

class XLabeledDataSequence(XInterface_8f010a43):
    """
    allows access to a one-dimensional sequence of data.
    
    The data that is stored in this container may contain different types.

    See Also:
        `API XLabeledDataSequence <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XLabeledDataSequence.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.XLabeledDataSequence'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.data.XLabeledDataSequence'

    @abstractmethod
    def getLabel(self) -> 'XDataSequence_11f00e1f':
        """
        returns an XDataSequence containing the label for the labeled sequence.
        """
        ...
    @abstractmethod
    def getValues(self) -> 'XDataSequence_11f00e1f':
        """
        returns an XDataSequence containing the actual data.
        """
        ...
    @abstractmethod
    def setLabel(self, xSequence: 'XDataSequence_11f00e1f') -> None:
        """
        sets a new XDataSequence containing the label for the labeled sequence.
        """
        ...
    @abstractmethod
    def setValues(self, xSequence: 'XDataSequence_11f00e1f') -> None:
        """
        sets a new XDataSequence containing the actual data.
        """
        ...

__all__ = ['XLabeledDataSequence']

