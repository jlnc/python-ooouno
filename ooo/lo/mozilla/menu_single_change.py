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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class MenuSingleChange(object):
    """
    Struct Class

    Explains a change for a menu item.

    See Also:
        `API MenuSingleChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mozilla_1_1MenuSingleChange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.MenuSingleChange'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.mozilla.MenuSingleChange'
    """Literal Constant ``com.sun.star.mozilla.MenuSingleChange``"""

    def __init__(self, ID: typing.Optional[int] = 0, ChangeID: typing.Optional[int] = 0, Change: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            ID (int, optional): ID value.
            ChangeID (int, optional): ChangeID value.
            Change (object, optional): Change value.
        """
        super().__init__()

        if isinstance(ID, MenuSingleChange):
            oth: MenuSingleChange = ID
            self.ID = oth.ID
            self.ChangeID = oth.ChangeID
            self.Change = oth.Change
            return

        kargs = {
            "ID": ID,
            "ChangeID": ChangeID,
            "Change": Change,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._id = kwargs["ID"]
        self._change_id = kwargs["ChangeID"]
        self._change = kwargs["Change"]


    @property
    def ID(self) -> int:
        """
        unique ID of this menu item
        """
        return self._id
    
    @ID.setter
    def ID(self, value: int) -> None:
        self._id = value

    @property
    def ChangeID(self) -> int:
        """
        ID identifying the type of change in the any type change.
        """
        return self._change_id
    
    @ChangeID.setter
    def ChangeID(self, value: int) -> None:
        self._change_id = value

    @property
    def Change(self) -> object:
        """
        value of change
        """
        return self._change
    
    @Change.setter
    def Change(self, value: object) -> None:
        self._change = value


__all__ = ['MenuSingleChange']
