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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.xml
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class UserDefinedAttributesSupplier(ABC):
    """
    Service Class

    A component that supports this service preserves XML attributes, unknown by its parser, that belong to the XML element representing it (the component).
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API UserDefinedAttributesSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1UserDefinedAttributesSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.UserDefinedAttributesSupplier'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def UserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        This container holds the AttributeData elements that represent uninterpreted XML attributes.
        
        The idea behind this property is that a parser can stow away all attributes that it cannot handle by itself on reading an XML file. When the file is stored again, the unknown attributes can be written back without loss.
        
        The com.sun.star.container.XNameContainer supports the service AttributeContainer.
        """
        ...



__all__ = ['UserDefinedAttributesSupplier']

