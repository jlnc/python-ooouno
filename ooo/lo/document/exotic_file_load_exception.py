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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ExoticFileLoadException(Exception_85530a09):
    """
    Exception Class

    An exception used to notify loading of an exotic file format.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API ExoticFileLoadException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1ExoticFileLoadException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.ExoticFileLoadException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.document.ExoticFileLoadException'
    __pyunostruct__: str = 'com.sun.star.document.ExoticFileLoadException'

    typeName: str = 'com.sun.star.document.ExoticFileLoadException'
    """Literal Constant ``com.sun.star.document.ExoticFileLoadException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, URL: typing.Optional[str] = '', FilterUIName: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            URL (str, optional): URL value.
            FilterUIName (str, optional): FilterUIName value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "URL": URL,
            "FilterUIName": FilterUIName,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._url = kwargs["URL"]
        self._filter_ui_name = kwargs["FilterUIName"]
        inst_keys = ('URL', 'FilterUIName')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def URL(self) -> str:
        """
        contains the URL of the document
        """
        return self._url
    
    @URL.setter
    def URL(self, value: str) -> None:
        self._url = value

    @property
    def FilterUIName(self) -> str:
        """
        contains the UI name of the filter
        """
        return self._filter_ui_name
    
    @FilterUIName.setter
    def FilterUIName(self, value: str) -> None:
        self._filter_ui_name = value


__all__ = ['ExoticFileLoadException']

