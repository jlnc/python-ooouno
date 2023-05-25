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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.task
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class XJob(XInterface_8f010a43):
    """
    specifies a job which is to be executed synchronously
    
    Instead of XAsyncJob the implementation of this interface will be executed synchronously every time. That means: they can be sure that the current stack context will be blocked till this job finish it's work.

    See Also:
        `API XJob <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XJob.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XJob'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XJob'

    @abstractmethod
    def execute(self, Arguments: typing.Tuple[NamedValue_a37a0af3, ...]) -> object:
        """
        executes the job synchronously

        Raises:
            : ````
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XJob']


