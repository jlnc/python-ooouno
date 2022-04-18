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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from enum import Enum


class FillMode(Enum):
    """
    Enum Class

    

    See Also:
        `API FillMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a75a9acd74effffae38daed55136b0980>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FillMode'
    __ooo_type_name__: str = 'enum'

    FILL_DATE_DAY = 'FILL_DATE_DAY'
    """
    for every new value a single day is added.
    """
    FILL_DATE_MONTH = 'FILL_DATE_MONTH'
    """
    for every new value one month is added (day keeps unchanged).
    """
    FILL_DATE_WEEKDAY = 'FILL_DATE_WEEKDAY'
    """
    for every new value a single day is added, but Saturdays and Sundays are skipped.
    """
    FILL_DATE_YEAR = 'FILL_DATE_YEAR'
    """
    for every new value one year is added (day and month keep unchanged).
    """

__all__ = ['FillMode']

