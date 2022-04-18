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
# Namespace: com.sun.star.animations
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class TimeFilterPair(object):
    """
    Struct Class


    See Also:
        `API TimeFilterPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1animations_1_1TimeFilterPair.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.TimeFilterPair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.animations.TimeFilterPair'
    """Literal Constant ``com.sun.star.animations.TimeFilterPair``"""

    def __init__(self, Time: typing.Optional[float] = 0.0, Progress: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Time (float, optional): Time value.
            Progress (float, optional): Progress value.
        """
        super().__init__()

        if isinstance(Time, TimeFilterPair):
            oth: TimeFilterPair = Time
            self.Time = oth.Time
            self.Progress = oth.Progress
            return

        kargs = {
            "Time": Time,
            "Progress": Progress,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._time = kwargs["Time"]
        self._progress = kwargs["Progress"]


    @property
    def Time(self) -> float:
        return self._time
    
    @Time.setter
    def Time(self, value: float) -> None:
        self._time = value

    @property
    def Progress(self) -> float:
        return self._progress
    
    @Progress.setter
    def Progress(self, value: float) -> None:
        self._progress = value


__all__ = ['TimeFilterPair']
