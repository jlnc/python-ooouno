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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ...uno.exception import Exception as Exception_85530a09
from ...uno.x_interface import XInterface as XInterface_8f010a43

class MergeRecoveryRequest(Exception_85530a09):
    """
    Exception Class

    is passed to an InteractionHandler when merging fails due to invalid layer data or access problems.
    
    **since**
    
        OOo 2.0

    See Also:
        `API MergeRecoveryRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1backend_1_1MergeRecoveryRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.MergeRecoveryRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.MergeRecoveryRequest'
    __pyunostruct__: str = 'com.sun.star.configuration.backend.MergeRecoveryRequest'

    typeName: str = 'com.sun.star.configuration.backend.MergeRecoveryRequest'
    """Literal Constant ``com.sun.star.configuration.backend.MergeRecoveryRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, ErrorDetails: typing.Optional[object] = None, ErrorLayerId: typing.Optional[str] = '', IsRemovalRequest: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrorDetails (object, optional): ErrorDetails value.
            ErrorLayerId (str, optional): ErrorLayerId value.
            IsRemovalRequest (bool, optional): IsRemovalRequest value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "ErrorDetails": ErrorDetails,
            "ErrorLayerId": ErrorLayerId,
            "IsRemovalRequest": IsRemovalRequest,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._error_details = kwargs["ErrorDetails"]
        self._error_layer_id = kwargs["ErrorLayerId"]
        self._is_removal_request = kwargs["IsRemovalRequest"]
        inst_keys = ('ErrorDetails', 'ErrorLayerId', 'IsRemovalRequest')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def ErrorDetails(self) -> object:
        """
        data that provides more detailed information about the reason and location of the error.
        
        Typically this member should contain an exception characterizing the error in detail.
        
        For example the following exceptions may be used:
        
        If no more detail information is available, this may be left VOID.
        """
        return self._error_details
    
    @ErrorDetails.setter
    def ErrorDetails(self, value: object) -> None:
        self._error_details = value

    @property
    def ErrorLayerId(self) -> str:
        """
        Identifier of the layer object containing the invalid data.
        """
        return self._error_layer_id
    
    @ErrorLayerId.setter
    def ErrorLayerId(self, value: str) -> None:
        self._error_layer_id = value

    @property
    def IsRemovalRequest(self) -> bool:
        """
        specifies whether the requester wants to remove or skip the invalid layer.
        
        If TRUE the requester wants to remove the underlying data of the layer.
        If FALSE the request is to skip the underlying data this time, but without removing it.
        """
        return self._is_removal_request
    
    @IsRemovalRequest.setter
    def IsRemovalRequest(self, value: bool) -> None:
        self._is_removal_request = value


