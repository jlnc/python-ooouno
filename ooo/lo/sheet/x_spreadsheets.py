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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from abc import abstractmethod
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class XSpreadsheets(XNameContainer_cb90e47):
    """
    provides methods to access the spreadsheets by name and to insert, copy, remove and rearrange spreadsheets.

    See Also:
        `API XSpreadsheets <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSpreadsheets.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSpreadsheets'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSpreadsheets'

    @abstractmethod
    def copyByName(self, aName: str, aCopy: str, nDestination: int) -> None:
        """
        copies a sheet within the collection.
        """
        ...
    @abstractmethod
    def insertNewByName(self, aName: str, nPosition: int) -> None:
        """
        inserts a new sheet into the collection.
        """
        ...
    @abstractmethod
    def moveByName(self, aName: str, nDestination: int) -> None:
        """
        moves a sheet within the collection.
        """
        ...

__all__ = ['XSpreadsheets']

