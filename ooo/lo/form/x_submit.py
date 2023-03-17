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
# Namespace: com.sun.star.form
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.mouse_event import MouseEvent as MouseEvent_8f430a5f
    from ..awt.x_control import XControl as XControl_7a9c098d
    from .x_submit_listener import XSubmitListener as XSubmitListener_d5950cce

class XSubmit(XInterface_8f010a43):
    """
    provides functionality to submit data from a component.
    
    Usually, this is used by com.sun.star.form.component.HTMLForms.
    
    See the HTML specification to learn about submitting forms.

    See Also:
        `API XSubmit <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XSubmit.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XSubmit'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XSubmit'

    @abstractmethod
    def addSubmitListener(self, aListener: 'XSubmitListener_d5950cce') -> None:
        """
        adds the specified listener to receive the \"approveSubmit\" event.
        """
        ...
    @abstractmethod
    def removeSubmitListener(self, aListener: 'XSubmitListener_d5950cce') -> None:
        """
        removes the specified listener.
        """
        ...
    @abstractmethod
    def submit(self, aControl: 'XControl_7a9c098d', aMouseEvt: 'MouseEvent_8f430a5f') -> None:
        """
        submits the component's data to a specified target.
        """
        ...

__all__ = ['XSubmit']

