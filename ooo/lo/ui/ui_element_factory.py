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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from __future__ import annotations
from .xui_element_factory import XUIElementFactory as XUIElementFactory_d0280c7e

class UIElementFactory(XUIElementFactory_d0280c7e):
    """
    Service Class

    specifies a user interface element factory that can create and initialize a user interface element type.
    
    It depends on the implementation which user interface element types can be created. It is also possible that a factory is only able to create one special user interface element. User interface element factories must be registered at the single instance UIElementFactoryManager service to provide access to itself.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UIElementFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1UIElementFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.UIElementFactory'
    __ooo_type_name__: str = 'service'


__all__ = ['UIElementFactory']

