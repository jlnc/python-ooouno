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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class ElementChange(object):
    """
    Struct Class

    This structure describes a single change that is part of a batch of changes.

    See Also:
        `API ElementChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1ElementChange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.ElementChange'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.ElementChange'
    """Literal Constant ``com.sun.star.util.ElementChange``"""

    def __init__(self, Accessor: typing.Optional[object] = None, Element: typing.Optional[object] = None, ReplacedElement: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Accessor (object, optional): Accessor value.
            Element (object, optional): Element value.
            ReplacedElement (object, optional): ReplacedElement value.
        """
        super().__init__()

        if isinstance(Accessor, ElementChange):
            oth: ElementChange = Accessor
            self.Accessor = oth.Accessor
            self.Element = oth.Element
            self.ReplacedElement = oth.ReplacedElement
            return

        kargs = {
            "Accessor": Accessor,
            "Element": Element,
            "ReplacedElement": ReplacedElement,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._accessor = kwargs["Accessor"]
        self._element = kwargs["Element"]
        self._replaced_element = kwargs["ReplacedElement"]


    @property
    def Accessor(self) -> object:
        """
        This contains the accessor to the element which changed.
        
        The type and the value of the accessor depends on the service.
        """
        return self._accessor
    
    @Accessor.setter
    def Accessor(self, value: object) -> None:
        self._accessor = value

    @property
    def Element(self) -> object:
        """
        This contains the element that was inserted or changed.
        """
        return self._element
    
    @Element.setter
    def Element(self, value: object) -> None:
        self._element = value

    @property
    def ReplacedElement(self) -> object:
        """
        This contains the element that was replaced or removed.
        """
        return self._replaced_element
    
    @ReplacedElement.setter
    def ReplacedElement(self, value: object) -> None:
        self._replaced_element = value


__all__ = ['ElementChange']
