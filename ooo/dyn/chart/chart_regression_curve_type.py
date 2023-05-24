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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class ChartRegressionCurveType(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartRegressionCurveType", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartRegressionCurveType`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.chart.ChartRegressionCurveType import EXPONENTIAL as CHART_REGRESSION_CURVE_TYPE_EXPONENTIAL
        from com.sun.star.chart.ChartRegressionCurveType import LINEAR as CHART_REGRESSION_CURVE_TYPE_LINEAR
        from com.sun.star.chart.ChartRegressionCurveType import LOGARITHM as CHART_REGRESSION_CURVE_TYPE_LOGARITHM
        from com.sun.star.chart.ChartRegressionCurveType import NONE as CHART_REGRESSION_CURVE_TYPE_NONE
        from com.sun.star.chart.ChartRegressionCurveType import POLYNOMIAL as CHART_REGRESSION_CURVE_TYPE_POLYNOMIAL
        from com.sun.star.chart.ChartRegressionCurveType import POWER as CHART_REGRESSION_CURVE_TYPE_POWER

        class ChartRegressionCurveType(uno.Enum):
            """
            Enum Class


            See Also:
                `API ChartRegressionCurveType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a00d1bb45d8b0a2aac5e07cde2f18302b>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.chart.ChartRegressionCurveType', value)

            __ooo_ns__: str = 'com.sun.star.chart'
            __ooo_full_ns__: str = 'com.sun.star.chart.ChartRegressionCurveType'
            __ooo_type_name__: str = 'enum'

            EXPONENTIAL = CHART_REGRESSION_CURVE_TYPE_EXPONENTIAL
            """
            displays an exponential regression curve.
            """
            LINEAR = CHART_REGRESSION_CURVE_TYPE_LINEAR
            """
            displays a linear regression curve.
            """
            LOGARITHM = CHART_REGRESSION_CURVE_TYPE_LOGARITHM
            """
            displays a linear logarithmic regression curve.
            """
            NONE = CHART_REGRESSION_CURVE_TYPE_NONE
            """
            error indicators are not displayed.

            displays no regression curve.

            no chart legend is displayed.

            displays no error indicators.
            """
            POLYNOMIAL = CHART_REGRESSION_CURVE_TYPE_POLYNOMIAL
            """
            displays a polynomial regression curve.
            """
            POWER = CHART_REGRESSION_CURVE_TYPE_POWER
            """
            displays a regression curve using a power function.

            displays a moving average regression curve.
            """
    else:
        # keep document generators happy
        from ...lo.chart.chart_regression_curve_type import ChartRegressionCurveType as ChartRegressionCurveType


__all__ = ['ChartRegressionCurveType']
