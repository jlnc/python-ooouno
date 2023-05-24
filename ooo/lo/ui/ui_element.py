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
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from .xui_element import XUIElement as XUIElement_820509a6
from ..util.x_updatable import XUpdatable as XUpdatable_9a420ab0

class UIElement(XComponent_98dc0ab5, XInitialization_d46c0cca, XUIElement_820509a6, XUpdatable_9a420ab0):
    """
    Service Class

    specifies a user interface element.
    
    A user interface element consists of a unique identifier and a type specifier. It provides an interface to retrieve a special purpose interface which depends on the specific user interface element type. Every user interface must be initialized before it can be used.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UIElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1UIElement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.UIElement'
    __ooo_type_name__: str = 'service'


__all__ = ['UIElement']

