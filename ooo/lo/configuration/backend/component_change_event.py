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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ComponentChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    This event is fired when a change becomes effective on the source of the event.

    See Also:
        `API ComponentChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1configuration_1_1backend_1_1ComponentChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.ComponentChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.configuration.backend.ComponentChangeEvent'
    """Literal Constant ``com.sun.star.configuration.backend.ComponentChangeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Component: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Component (str, optional): Component value.
        """

        if isinstance(Source, ComponentChangeEvent):
            oth: ComponentChangeEvent = Source
            self.Source = oth.Source
            self.Component = oth.Component
            return

        kargs = {
            "Source": Source,
            "Component": Component,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._component = kwargs["Component"]
        inst_keys = ('Component',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Component(self) -> str:
        """
        The name of the Component that changed.
        """
        return self._component
    
    @Component.setter
    def Component(self, value: str) -> None:
        self._component = value


__all__ = ['ComponentChangeEvent']
