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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.beans
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class MethodConcept(metaclass=UnoConstMeta, type_name="com.sun.star.beans.MethodConcept", name_space="com.sun.star.beans"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.beans.MethodConcept``"""
        pass

    class MethodConceptEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.beans.MethodConcept", name_space="com.sun.star.beans"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.beans.MethodConcept`` as Enum values"""
        pass

else:
    from com.sun.star.beans import MethodConcept as MethodConcept

    class MethodConceptEnum(IntEnum):
        """
        Enum of Const Class MethodConcept

        These constants are used to specify concepts of the introspection which apply to methods.
        
        This list is not necessarily complete; new constants may be added.
        """
        ALL = MethodConcept.ALL
        """
        This value is used to query for all methods, see XIntrospectionAccess.getMethod() and XIntrospectionAccess.getMethods()
        """
        DANGEROUS = MethodConcept.DANGEROUS
        """
        specifies methods which can result in an unstable state (i.e.
        
        deadlock, application crash, security hole, etc.) when called directly by the user.
        """
        PROPERTY = MethodConcept.PROPERTY
        """
        specifies methods which are used to set and get the value of properties/attributes.
        
        These methods have the signature type get...() , void set...() or boolean is...() .
        """
        LISTENER = MethodConcept.LISTENER
        """
        specifies methods of the listener concept.
        
        These methods have the signature add...Listener()  or remove...Listener().
        """
        ENUMERATION = MethodConcept.ENUMERATION
        """
        specifies methods of the enumeration concept.
        
        These methods have the signature create...Enumeration and return an interface that is derived from com.sun.star.container.XEnumeration. Additionally, the method com.sun.star.container.XEnumerationAccess.getElementType() belongs to this concept.
        """
        NAMECONTAINER = MethodConcept.NAMECONTAINER
        """
        specifies methods of the name container concept.
        
        These methods have the signature get...ByName(), set...ByName(), replace...ByName(), remove...ByName(), has...ByName(), or get...Names. In addition, the method com.sun.star.container.XEnumerationAccess.getElementType() belongs to this concept.
        """
        INDEXCONTAINER = MethodConcept.INDEXCONTAINER
        """
        specifies methods of the index container concept.
        
        These methods have the signature get...ByIndex(), insert...ByIndex(), replace...ByIndex(), or remove...ByIndex(). The method com.sun.star.container.XIndexAccess.getCount() also belongs to this concept.
        """

__all__ = ['MethodConcept', 'MethodConceptEnum']
