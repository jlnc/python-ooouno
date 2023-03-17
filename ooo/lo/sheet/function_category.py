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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet


class FunctionCategory(object):
    """
    Const Class

    used to specify the category of a spreadsheet function.

    See Also:
        `API FunctionCategory <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FunctionCategory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FunctionCategory'
    __ooo_type_name__: str = 'const'

    DATABASE = 1
    """
    specifies a database function.
    """
    DATETIME = 2
    """
    specifies a function that calculates with dates and/or times.
    """
    FINANCIAL = 3
    """
    specifies a financial function.
    """
    INFORMATION = 4
    """
    specifies a function that returns information about the cell, the cell contents or the current formula.
    """
    LOGICAL = 5
    """
    specifies a boolean function.
    """
    MATHEMATICAL = 6
    """
    specifies a common mathematical function
    """
    MATRIX = 7
    """
    specifies a matrix function.
    """
    STATISTICAL = 8
    """
    specifies a statistical function
    """
    SPREADSHEET = 9
    """
    specifies a function that returns information using the spreadsheet contents or specific cell positions.
    """
    TEXT = 10
    """
    specifies a text function.
    """
    ADDIN = 11
    """
    specifies a common add-in function.
    """

__all__ = ['FunctionCategory']
