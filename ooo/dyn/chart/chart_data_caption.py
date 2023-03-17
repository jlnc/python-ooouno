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
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ChartDataCaption(metaclass=UnoConstMeta, type_name="com.sun.star.chart.ChartDataCaption", name_space="com.sun.star.chart"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.chart.ChartDataCaption``"""
        pass

    class ChartDataCaptionEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.chart.ChartDataCaption", name_space="com.sun.star.chart"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.chart.ChartDataCaption`` as Enum values"""
        pass

else:
    from ...lo.chart.chart_data_caption import ChartDataCaption as ChartDataCaption

    class ChartDataCaptionEnum(IntFlag):
        """
        Enum of Const Class ChartDataCaption

        These values specify how the captions of data points are displayed.
        
        **since**
        
            LibreOffice 7.1
        """
        NONE = ChartDataCaption.NONE
        """
        No captions are displayed.
        """
        VALUE = ChartDataCaption.VALUE
        """
        The caption contains the value of the data point in the number format of the axis that is attached to the respective data series.
        """
        PERCENT = ChartDataCaption.PERCENT
        """
        The caption contains the value of the data point in percent of all data points of one category.
        
        That means, if a data point is the first one of a series, the percentage is calculated by using the first data points of all available series.
        """
        TEXT = ChartDataCaption.TEXT
        """
        The caption contains the category name of the category to which a data point belongs.
        """
        FORMAT = ChartDataCaption.FORMAT
        """
        The number formatter is always used for displaying the value as value.
        
        So this setting is deprecated.
        """
        SYMBOL = ChartDataCaption.SYMBOL
        """
        The symbol of data column/row is additionally displayed in the caption.
        """
        CUSTOM = ChartDataCaption.CUSTOM
        """
        The caption contains a custom text, which belongs to a data point label.
        
        **since**
        
            LibreOffice 7.1
        """
        DATA_SERIES = ChartDataCaption.DATA_SERIES
        """
        The name of the data series is additionally displayed in the caption.
        
        **since**
        
            LibreOffice 7.2
        """

__all__ = ['ChartDataCaption', 'ChartDataCaptionEnum']
