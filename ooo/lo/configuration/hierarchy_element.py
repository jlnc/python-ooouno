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
# Namespace: com.sun.star.configuration
from __future__ import annotations
from ..beans.x_property import XProperty as XProperty_99770ace
from ..beans.x_property_with_state import XPropertyWithState as XPropertyWithState_c960e6b
from ..container.x_child import XChild as XChild_a6390b07
from ..container.x_hierarchical_name import XHierarchicalName as XHierarchicalName_3a4b0f63
from ..container.x_named import XNamed as XNamed_a6520b08

class HierarchyElement(XProperty_99770ace, XPropertyWithState_c960e6b, XChild_a6390b07, XHierarchicalName_3a4b0f63, XNamed_a6520b08):
    """
    Service Class

    provides information about an element within a hierarchy.
    
    The local name and the full hierarchical name can be retrieved. Attributes detailing the role of the element can be queried. The state of the element (regarding defaults) can be accessed.
    
    Implementations of this service usually also implement service HierarchyAccess, which concerns the complementary role of providing access to subelements of the hierarchy.

    See Also:
        `API HierarchyElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1HierarchyElement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.HierarchyElement'
    __ooo_type_name__: str = 'service'


__all__ = ['HierarchyElement']

