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
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XModuleUIConfigurationManager(XInterface_8f010a43):
    """
    specifies specific functions of a module based user interface configuration manager interface.
    
    A module user interface configuration manager supports, unlike a document based ui configuration manager, two layers of configuration settings data:
    
    **since**
    
        OOo 2.0

    See Also:
        `API XModuleUIConfigurationManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XModuleUIConfigurationManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XModuleUIConfigurationManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XModuleUIConfigurationManager'

    @abstractmethod
    def getDefaultSettings(self, ResourceURL: str) -> 'XIndexAccess_f0910d6d':
        """
        retrieves the settings from the default layer of the user interface configuration manager if it has a default layer.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def isDefaultSettings(self, ResourceURL: str) -> bool:
        """
        determine if the settings of a user interface element is part of the default layer of the user interface configuration manager.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XModuleUIConfigurationManager']

