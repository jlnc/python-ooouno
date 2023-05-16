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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from enum import Enum


class LockDepth(Enum):
    """
    Enum Class


    See Also:
        `API LockDepth <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a01e925906d2f84e461036af17439e9ca>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.LockDepth'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.ucb.LockDepth'

    INFINITY = 'INFINITY'
    """
    Infinity (includes children and children's children and ...).
    """
    ONE = 'ONE'
    """
    One (includes children).
    """
    ZERO = 'ZERO'
    """
    Zero (includes no children).
    """

__all__ = ['LockDepth']

