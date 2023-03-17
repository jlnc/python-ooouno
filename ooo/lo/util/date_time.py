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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class DateTime(object):
    """
    Struct Class

    represents a combined date+time value.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateTime <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateTime.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.DateTime'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.DateTime'
    """Literal Constant ``com.sun.star.util.DateTime``"""

    def __init__(self, NanoSeconds: typing.Optional[int] = 0, Seconds: typing.Optional[int] = 0, Minutes: typing.Optional[int] = 0, Hours: typing.Optional[int] = 0, Day: typing.Optional[int] = 0, Month: typing.Optional[int] = 0, Year: typing.Optional[int] = 0, IsUTC: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            NanoSeconds (int, optional): NanoSeconds value.
            Seconds (int, optional): Seconds value.
            Minutes (int, optional): Minutes value.
            Hours (int, optional): Hours value.
            Day (int, optional): Day value.
            Month (int, optional): Month value.
            Year (int, optional): Year value.
            IsUTC (bool, optional): IsUTC value.
        """
        super().__init__()

        if isinstance(NanoSeconds, DateTime):
            oth: DateTime = NanoSeconds
            self.NanoSeconds = oth.NanoSeconds
            self.Seconds = oth.Seconds
            self.Minutes = oth.Minutes
            self.Hours = oth.Hours
            self.Day = oth.Day
            self.Month = oth.Month
            self.Year = oth.Year
            self.IsUTC = oth.IsUTC
            return

        kargs = {
            "NanoSeconds": NanoSeconds,
            "Seconds": Seconds,
            "Minutes": Minutes,
            "Hours": Hours,
            "Day": Day,
            "Month": Month,
            "Year": Year,
            "IsUTC": IsUTC,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._nano_seconds = kwargs["NanoSeconds"]
        self._seconds = kwargs["Seconds"]
        self._minutes = kwargs["Minutes"]
        self._hours = kwargs["Hours"]
        self._day = kwargs["Day"]
        self._month = kwargs["Month"]
        self._year = kwargs["Year"]
        self._is_utc = kwargs["IsUTC"]


    @property
    def NanoSeconds(self) -> int:
        """
        contains the nanoseconds (0 - 999 999 999).
        """
        return self._nano_seconds
    
    @NanoSeconds.setter
    def NanoSeconds(self, value: int) -> None:
        self._nano_seconds = value

    @property
    def Seconds(self) -> int:
        """
        contains the seconds (0-59).
        """
        return self._seconds
    
    @Seconds.setter
    def Seconds(self, value: int) -> None:
        self._seconds = value

    @property
    def Minutes(self) -> int:
        """
        contains the minutes (0-59).
        """
        return self._minutes
    
    @Minutes.setter
    def Minutes(self, value: int) -> None:
        self._minutes = value

    @property
    def Hours(self) -> int:
        """
        contains the hour (0-23).
        """
        return self._hours
    
    @Hours.setter
    def Hours(self, value: int) -> None:
        self._hours = value

    @property
    def Day(self) -> int:
        """
        is the day of month (1-31 or 0 for a void date).
        """
        return self._day
    
    @Day.setter
    def Day(self, value: int) -> None:
        self._day = value

    @property
    def Month(self) -> int:
        """
        is the month of year (1-12 or 0 for a void date).
        """
        return self._month
    
    @Month.setter
    def Month(self, value: int) -> None:
        self._month = value

    @property
    def Year(self) -> int:
        """
        is the year.
        """
        return self._year
    
    @Year.setter
    def Year(self, value: int) -> None:
        self._year = value

    @property
    def IsUTC(self) -> bool:
        """
        true: time zone is UTC false: unknown time zone.
        
        **since**
        
            LibreOffice 4.1
        """
        return self._is_utc
    
    @IsUTC.setter
    def IsUTC(self, value: bool) -> None:
        self._is_utc = value


__all__ = ['DateTime']
