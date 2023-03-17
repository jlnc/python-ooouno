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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.4
from enum import Enum


class MethodMode(Enum):
    """
    Enum Class

    

    See Also:
        `API MethodMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1reflection.html#a5e114fee85d0f2f8cb01480a474dd9b4>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.MethodMode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.reflection.MethodMode'

    ONEWAY = 'ONEWAY'
    """
    method may be run asynchronously
    """
    TWOWAY = 'TWOWAY'
    """
    method is run The
    """

__all__ = ['MethodMode']

