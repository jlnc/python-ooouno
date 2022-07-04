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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class FetchResult(object):
    """
    Struct Class

    contains data of several rows of a ContentResultSet.
    
    This struct is returned from XFetchProvider.fetch(), for example.

    See Also:
        `API FetchResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1FetchResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.FetchResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.FetchResult'
    """Literal Constant ``com.sun.star.ucb.FetchResult``"""

    def __init__(self, Rows: typing.Optional[typing.Tuple[object, ...]] = (), StartIndex: typing.Optional[int] = 0, Orientation: typing.Optional[bool] = False, FetchError: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Rows (typing.Tuple[object, ...], optional): Rows value.
            StartIndex (int, optional): StartIndex value.
            Orientation (bool, optional): Orientation value.
            FetchError (int, optional): FetchError value.
        """
        super().__init__()

        if isinstance(Rows, FetchResult):
            oth: FetchResult = Rows
            self.Rows = oth.Rows
            self.StartIndex = oth.StartIndex
            self.Orientation = oth.Orientation
            self.FetchError = oth.FetchError
            return

        kargs = {
            "Rows": Rows,
            "StartIndex": StartIndex,
            "Orientation": Orientation,
            "FetchError": FetchError,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._rows = kwargs["Rows"]
        self._start_index = kwargs["StartIndex"]
        self._orientation = kwargs["Orientation"]
        self._fetch_error = kwargs["FetchError"]


    @property
    def Rows(self) -> typing.Tuple[object, ...]:
        """
        contains the demanded data.
        
        One any contains the data of one whole row. Those methods which use this struct have to specify, what the any has to contain.
        """
        return self._rows
    
    @Rows.setter
    def Rows(self, value: typing.Tuple[object, ...]) -> None:
        self._rows = value

    @property
    def StartIndex(self) -> int:
        """
        indicates the index of the first row contained in FetchResult.Rows in the original result set.
        
        So if FetchResult.StartIndex equals 3, the first element in the sequence FetchResult.Rows contains the data of the index 3 in the original result set.
        
        The following rows are one after the other, but the direction depends on the value of FetchResult.Direction
        """
        return self._start_index
    
    @StartIndex.setter
    def StartIndex(self, value: int) -> None:
        self._start_index = value

    @property
    def Orientation(self) -> bool:
        """
        indicates the orientation in which the rows are fetched and set into the sequence FetchResult.Rows.
        
        When FetchResult.Orientation equals TRUE, the rows in FetchResult.Rows are ordered in the same way as in the original result set.
        """
        return self._orientation
    
    @Orientation.setter
    def Orientation(self, value: bool) -> None:
        self._orientation = value

    @property
    def FetchError(self) -> int:
        """
        indicates whether and which error has occurred, while fetching.
        
        The value may contain zero or more constants of the FetchError constants group.
        """
        return self._fetch_error
    
    @FetchError.setter
    def FetchError(self, value: int) -> None:
        self._fetch_error = value


__all__ = ['FetchResult']
