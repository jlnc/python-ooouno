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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.task
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class ClassifiedInteractionRequest(Exception_85530a09):
    """
    Exception Class

    A classified interaction request.

    See Also:
        `API ClassifiedInteractionRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1ClassifiedInteractionRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.ClassifiedInteractionRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.ClassifiedInteractionRequest'
    __pyunostruct__: str = 'com.sun.star.task.ClassifiedInteractionRequest'

    typeName: str = 'com.sun.star.task.ClassifiedInteractionRequest'
    """Literal Constant ``com.sun.star.task.ClassifiedInteractionRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._classification = kwargs["Classification"]
        inst_keys = ('Classification',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Classification(self) -> InteractionClassification_6c4d10e7:
        """
        The classification of the request.
        """
        return self._classification
    
    @Classification.setter
    def Classification(self, value: InteractionClassification_6c4d10e7) -> None:
        self._classification = value


__all__ = ['ClassifiedInteractionRequest']

