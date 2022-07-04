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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.beans
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class PropertyConcept(metaclass=UnoConstMeta, type_name="com.sun.star.beans.PropertyConcept", name_space="com.sun.star.beans"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.beans.PropertyConcept``"""
        pass

    class PropertyConceptEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.beans.PropertyConcept", name_space="com.sun.star.beans"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.beans.PropertyConcept`` as Enum values"""
        pass

else:
    from ...lo.beans.property_concept import PropertyConcept as PropertyConcept

    class PropertyConceptEnum(IntEnum):
        """
        Enum of Const Class PropertyConcept

        These constants are used to specify concepts of the introspection which apply to properties and to the methods which represent attributes.
        
        This list is not necessarily complete; new constants may be added.
        """
        ALL = PropertyConcept.ALL
        """
        This value is used to query for all properties.
        
        See XIntrospectionAccess.getProperty() and XIntrospectionAccess.getProperties()
        """
        DANGEROUS = PropertyConcept.DANGEROUS
        """
        specifies that the change or retrieval of this property directly by the user can result in an unstable state (deadlock, application crash, security hole, etc.)
        """
        PROPERTYSET = PropertyConcept.PROPERTYSET
        """
        specifies all properties which are reachable by XPropertySet, XFastPropertySet or XMultiPropertySet.
        """
        ATTRIBUTES = PropertyConcept.ATTRIBUTES
        """
        specifies all properties which are actually attributes of interfaces.
        """
        METHODS = PropertyConcept.METHODS
        """
        specifies all properties which are represented by getter or setter methods.
        
        These methods have the signature type get...(), void set...() or boolean is...().
        """

__all__ = ['PropertyConcept', 'PropertyConceptEnum']
