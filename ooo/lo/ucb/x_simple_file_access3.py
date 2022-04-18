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
# Namespace: com.sun.star.ucb
from abc import abstractmethod
from .x_simple_file_access2 import XSimpleFileAccess2 as XSimpleFileAccess2_ebe60d08

class XSimpleFileAccess3(XSimpleFileAccess2_ebe60d08):
    """
    This is an extension to the interface XSimpleFileAccess2.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSimpleFileAccess3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XSimpleFileAccess3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XSimpleFileAccess3'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XSimpleFileAccess3'

    @abstractmethod
    def isHidden(self, FileURL: str) -> bool:
        """
        Checks if a file is \"hidden\".

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def setHidden(self, FileURL: str, bHidden: bool) -> None:
        """
        Sets the \"hidden\" of a file according to the boolean parameter, if the actual process has the right to do so and the used operation system supports this operation.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """

__all__ = ['XSimpleFileAccess3']

