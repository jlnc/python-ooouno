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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .x_data_series import XDataSeries as XDataSeries_b8150b89
from .data.x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence_7e1a10c8


class InterpretedData(object):
    """
    Struct Class

    offers tooling to interpret different data sources in a structural and chart-type-dependent way.

    See Also:
        `API InterpretedData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1InterpretedData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.InterpretedData'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.InterpretedData'
    """Literal Constant ``com.sun.star.chart2.InterpretedData``"""

    def __init__(self, Series: typing.Optional[typing.Tuple[typing.Tuple[XDataSeries_b8150b89, ...], ...]] = (), Categories: typing.Optional[XLabeledDataSequence_7e1a10c8] = None) -> None:
        """
        Constructor

        Arguments:
            Series (typing.Tuple[typing.Tuple[XDataSeries, ...], ...], optional): Series value.
            Categories (XLabeledDataSequence, optional): Categories value.
        """
        super().__init__()

        if isinstance(Series, InterpretedData):
            oth: InterpretedData = Series
            self.Series = oth.Series
            self.Categories = oth.Categories
            return

        kargs = {
            "Series": Series,
            "Categories": Categories,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._series = kwargs["Series"]
        self._categories = kwargs["Categories"]


    @property
    def Series(self) -> typing.Tuple[typing.Tuple[XDataSeries_b8150b89, ...], ...]:
        return self._series
    
    @Series.setter
    def Series(self, value: typing.Tuple[typing.Tuple[XDataSeries_b8150b89, ...], ...]) -> None:
        self._series = value

    @property
    def Categories(self) -> XLabeledDataSequence_7e1a10c8:
        return self._categories
    
    @Categories.setter
    def Categories(self, value: XLabeledDataSequence_7e1a10c8) -> None:
        self._categories = value


__all__ = ['InterpretedData']
