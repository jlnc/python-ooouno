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
# Namespace: com.sun.star.datatransfer.clipboard
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..x_transferable import XTransferable as XTransferable_2d800f38


class ClipboardEvent(EventObject_a3d70b03):
    """
    Struct Class

    A clipboard uses this object to notify its listeners of content changes.

    See Also:
        `API ClipboardEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1ClipboardEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.clipboard'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.clipboard.ClipboardEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.clipboard.ClipboardEvent'
    """Literal Constant ``com.sun.star.datatransfer.clipboard.ClipboardEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Contents: typing.Optional[XTransferable_2d800f38] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Contents (XTransferable, optional): Contents value.
        """

        if isinstance(Source, ClipboardEvent):
            oth: ClipboardEvent = Source
            self.Source = oth.Source
            self.Contents = oth.Contents
            return

        kargs = {
            "Source": Source,
            "Contents": Contents,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._contents = kwargs["Contents"]
        inst_keys = ('Contents',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Contents(self) -> XTransferable_2d800f38:
        """
        The current content of the clipboard.
        """
        return self._contents
    
    @Contents.setter
    def Contents(self, value: XTransferable_2d800f38) -> None:
        self._contents = value


__all__ = ['ClipboardEvent']
