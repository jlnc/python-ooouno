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
# Namespace: com.sun.star.configuration.backend
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .template_identifier import TemplateIdentifier as TemplateIdentifier_2aaa14b5

class XUpdateHandler(XInterface_8f010a43):
    """
    receives a description of a configuration update or layer as a sequence of events.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XUpdateHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XUpdateHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.XUpdateHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XUpdateHandler'

    @abstractmethod
    def addOrReplaceNode(self, aName: str, aAttributes: int) -> None:
        """
        receives notification that a node is started as a new item.
        
        The current node must be a set and a preexisting item (if any) must be removable.
        
        The new item will be created from the default template of the set.
        
        Subsequent calls describe the difference from the template of properties, items or members of the node until a matching call to XUpdateHandler.endNode() is encountered.
        
        The value is a combination of NodeAttribute flags. Note that NodeAttribute.FUSE has an impact on the semantics of this method.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def addOrReplaceNodeFromTemplate(self, aName: str, aAttributes: int, aTemplate: 'TemplateIdentifier_2aaa14b5') -> None:
        """
        receives notification that a node is started as a new item based on a particular template.
        
        The current node must be a set and a preexisting item (if any) must be removable.
        
        Subsequent calls describe the difference from the template of properties or members of the node until a matching call to XUpdateHandler.endNode() is encountered.
        
        The value is a combination of NodeAttribute flags. Note that NodeAttribute.FUSE has an impact on the semantics of this method.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def addOrReplaceProperty(self, aName: str, aAttributes: int, aType: object) -> None:
        """
        receives notification that a property having a value of VOID is added to the current node.
        
        The current node must be extensible and a preexisting property (if any) must be removable in this layer.
        
        The value is a combination of NodeAttribute flags and may also contain the SchemaAttribute.REQUIRED flag.
        
        NodeAttribute.MANDATORY need not be set, as dynamic properties always are mandatory in subsequent layers.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def addOrReplacePropertyWithValue(self, aName: str, aAttributes: int, aValue: object) -> None:
        """
        receives notification that a property having a non-NULL value is added to the current node.
        
        The current node must be extensible and a preexisting property (if any) must be removable in this layer.
        
        The value is a combination of NodeAttribute flags and may also contain the SchemaAttribute.REQUIRED flag.
        
        NodeAttribute.MANDATORY need not be set, as dynamic properties always are mandatory in subsequent layers.
        
        The value also determines the type. Therefore the value must not be VOID.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def endNode(self) -> None:
        """
        receives notification that a node modification is complete.
        
        Must match the last open call to XUpdateHandler.modifyNode(), XUpdateHandler.addOrReplaceNode() or XUpdateHandler.addOrReplaceNodeFromTemplate().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def endProperty(self) -> None:
        """
        receives notification that a property modification is complete.
        
        Must match the last open call to XUpdateHandler.modifyProperty().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def endUpdate(self) -> None:
        """
        receives notification that the current update description is complete.
        
        Must match a previous call to XUpdateHandler.startUpdate().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def modifyNode(self, aName: str, aAttributes: int, aAttributeMask: int, bReset: bool) -> None:
        """
        receives notification that a modification of a node is started.
        
        Subsequent calls describe changes to properties and items or members of the node until a matching call to XUpdateHandler.endNode() is encountered.
        
        The value is a combination of NodeAttribute flags.
        
        Only attributes which are selected in aAttributeMask are changed.
        
        The value is a combination of NodeAttribute flags.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def modifyProperty(self, aName: str, aAttributes: int, aAttributeMask: int, aType: object) -> None:
        """
        receives notification that modification of an existing property is started.
        
        Subsequent calls describe changes to the value(s) of the property until a matching call to XUpdateHandler.endProperty() is encountered.
        
        The value is a combination of NodeAttribute flags.
        
        Only attributes which are selected in aAttributeMask are changed.
        
        NodeAttribute.MANDATORY need not be set and can't be removed, as dynamic properties always are mandatory in subsequent layers.
        
        The value is a combination of NodeAttribute flags.
        
        A VOID type can be used to signify that the type is unknown and should not be recorded.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def removeNode(self, aName: str) -> None:
        """
        receives notification that an item is to be dropped from a set.
        
        The current node must be a set and the item must be removable.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def removeProperty(self, aName: str) -> None:
        """
        receives notification that a property is dropped from the current node.
        
        The current node must be extensible and the property removable.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def resetProperty(self, aName: str) -> None:
        """
        receives notification that a property is reset to its default state.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def resetPropertyValue(self) -> None:
        """
        receives notification that the value of the current property should be reset to its default.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def resetPropertyValueForLocale(self, aLocale: str) -> None:
        """
        receives notification that the value of the current property for a specific locale should be reset to its default.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def setPropertyValue(self, aValue: object) -> None:
        """
        receives notification about a change to the value of the current property.
        
        The value must match the type of the existing property. If the property does not have the SchemaAttribute.REQUIRED flag set, the value can be VOID.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def setPropertyValueForLocale(self, aValue: object, aLocale: str) -> None:
        """
        receives notification about a change to the value of the current property for a specific locale.
        
        The value must match the type of the existing property. If the property does not have the SchemaAttribute.REQUIRED flag set, the value can be VOID.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def startUpdate(self) -> None:
        """
        receives notification that an update or description is started.
        
        Some implementations can only detect this when executing XUpdateHandler.endUpdate()

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XUpdateHandler']

