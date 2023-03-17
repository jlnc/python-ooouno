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
# Namespace: com.sun.star.inspection
import typing
from abc import abstractmethod
from .x_property_control_observer import XPropertyControlObserver as XPropertyControlObserver_cc6d132a
if typing.TYPE_CHECKING:
    from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2

class XPropertyControlContext(XPropertyControlObserver_cc6d132a):
    """
    specifies the interface of the context of an XPropertyControl.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XPropertyControlContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyControlContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.XPropertyControlContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.inspection.XPropertyControlContext'

    @abstractmethod
    def activateNextControl(self, CurrentControl: 'XPropertyControl_3f260fe2') -> None:
        """
        instructs the XPropertyControlContext to active the next control
        """
        ...

__all__ = ['XPropertyControlContext']

