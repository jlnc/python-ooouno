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
# Namespace: com.sun.star.chart


class DataLabelPlacement(object):
    """
    Const Class

    These values specify where the captions/labels of data points are displayed.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API DataLabelPlacement <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1DataLabelPlacement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.DataLabelPlacement'
    __ooo_type_name__: str = 'const'

    AVOID_OVERLAP = 0
    CENTER = 1
    TOP = 2
    TOP_LEFT = 3
    LEFT = 4
    BOTTOM_LEFT = 5
    BOTTOM = 6
    BOTTOM_RIGHT = 7
    RIGHT = 8
    TOP_RIGHT = 9
    INSIDE = 10
    OUTSIDE = 11
    NEAR_ORIGIN = 12
    CUSTOM = 13

__all__ = ['DataLabelPlacement']
