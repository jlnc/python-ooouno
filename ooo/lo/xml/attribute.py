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
# Namespace: com.sun.star.xml
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Attribute(object):
    """
    Struct Class

    A struct to keep information of an element's attribute.

    See Also:
        `API Attribute <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1Attribute.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.Attribute'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.xml.Attribute'
    """Literal Constant ``com.sun.star.xml.Attribute``"""

    def __init__(self, Name: typing.Optional[str] = '', NamespaceURL: typing.Optional[str] = '', Value: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            NamespaceURL (str, optional): NamespaceURL value.
            Value (str, optional): Value value.
        """
        super().__init__()

        if isinstance(Name, Attribute):
            oth: Attribute = Name
            self.Name = oth.Name
            self.NamespaceURL = oth.NamespaceURL
            self.Value = oth.Value
            return

        kargs = {
            "Name": Name,
            "NamespaceURL": NamespaceURL,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._namespace_url = kwargs["NamespaceURL"]
        self._value = kwargs["Value"]


    @property
    def Name(self) -> str:
        """
        the attribute name
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def NamespaceURL(self) -> str:
        """
        the attribute namespace URL
        """
        return self._namespace_url
    
    @NamespaceURL.setter
    def NamespaceURL(self, value: str) -> None:
        self._namespace_url = value

    @property
    def Value(self) -> str:
        """
        the attribute value
        """
        return self._value
    
    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['Attribute']
