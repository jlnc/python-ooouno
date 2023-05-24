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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from .x_controller import XController as XController_b00e0b8f
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..ui.x_sidebar_provider import XSidebarProvider as XSidebarProvider_c69c0c43

class XController2(XController_b00e0b8f):
    """
    extends the XController interface
    
    **since**
    
        OOo 3.0

    See Also:
        `API XController2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XController2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XController2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XController2'

    @abstractmethod
    def getSidebar(self) -> XSidebarProvider_c69c0c43:
        """
        get the sidebar if exists
        
        **since**
        
            LibreOffice 5.1
        """
        ...
    @abstractproperty
    def CreationArguments(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        denotes the arguments used to create the instance.
        
        Usually, controllers are created via XModel2.createViewController(), where the caller can pass not only a controller name, but also arguments parameterizing the to-be-created instance. Those arguments used at creation time can subsequently be retrieved using the CreationArguments member.
        """
        ...

    @abstractproperty
    def ComponentWindow(self) -> XWindow_713b0924:
        """
        denotes the \"root window\" of the controller.
        
        If the controller is plugged into a frame, this window acts as the frame's ComponentWindow.
        """
        ...

    @abstractproperty
    def ViewControllerName(self) -> str:
        """
        specifies the view name of the controller.
        
        A view name is a logical name, which can be used to create views of the same type. The name is meaningful only in conjunction with XModel2.createViewController()
        """
        ...


__all__ = ['XController2']

