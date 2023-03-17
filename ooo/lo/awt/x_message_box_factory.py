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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .message_box_type import MessageBoxType as MessageBoxType_bbcc0be4
    from .x_message_box import XMessageBox as XMessageBox_98e00a9a
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0

class XMessageBoxFactory(XInterface_8f010a43):
    """
    specifies a factory interface for creating message boxes.

    See Also:
        `API XMessageBoxFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XMessageBoxFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XMessageBoxFactory'

    @abstractmethod
    def createMessageBox(self, aParent: 'XWindowPeer_99760ab0', eType: 'MessageBoxType_bbcc0be4', nButtons: int, sTitle: str, sMessage: str) -> 'XMessageBox_98e00a9a':
        """
        creates a message box.
        
        This parameter must not be null.
        
        A combination of com.sun.star.awt.MessageBoxButtons
        
        A com.sun.star.awt.MessageBoxType.INFOBOX ignores this parameter, instead it uses a com.sun.star.awt.MessageBoxButtons.BUTTONS_OK.
        """
        ...

__all__ = ['XMessageBoxFactory']

