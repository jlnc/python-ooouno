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
# Namespace: com.sun.star.script
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
    from .x_all_listener import XAllListener as XAllListener_c91b0c54

class XEventAttacher(XInterface_8f010a43):
    """
    makes it possible to attach script events given by a sequence of ScriptEventDescriptor structures to a given interface.

    See Also:
        `API XEventAttacher <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XEventAttacher.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XEventAttacher'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XEventAttacher'

    @abstractmethod
    def attachListener(self, xTarget: 'XInterface_8f010a43', xAllListener: 'XAllListener_c91b0c54', aHelper: object, aListenerType: str, aAddListenerParam: str) -> 'XEventListener_c7230c4a':
        """
        registers the given \"AllListener\" object as a listener at the given interface by creating a suitable listener adapter and calling the \"addListener\" method corresponding to the \"ListenerType\".

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.IntrospectionException: ``IntrospectionException``
            com.sun.star.script.CannotCreateAdapterException: ``CannotCreateAdapterException``
            com.sun.star.lang.ServiceNotRegisteredException: ``ServiceNotRegisteredException``
        """
        ...
    @abstractmethod
    def attachSingleEventListener(self, xTarget: 'XInterface_8f010a43', xAllListener: 'XAllListener_c91b0c54', aHelper: object, aListenerType: str, aAddListenerParam: str, aEventMethod: str) -> 'XEventListener_c7230c4a':
        """
        registers an object as a listener at the given interface by creating a suitable listener adapter and calling the method which corresponds to the listener type.
        
        Only the event corresponding to the given event method will be delegated to xAllListener.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.IntrospectionException: ``IntrospectionException``
            com.sun.star.script.CannotCreateAdapterException: ``CannotCreateAdapterException``
            com.sun.star.lang.ServiceNotRegisteredException: ``ServiceNotRegisteredException``
        """
        ...
    @abstractmethod
    def removeListener(self, xTarget: 'XInterface_8f010a43', aListenerType: str, aRemoveListenerParam: str, xToRemoveListener: 'XEventListener_c7230c4a') -> None:
        """
        removes a listener object as a listener from the given interface.
        
        This method can and should be used as a contrary method to the two attach methods.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.IntrospectionException: ``IntrospectionException``
        """
        ...

__all__ = ['XEventAttacher']

