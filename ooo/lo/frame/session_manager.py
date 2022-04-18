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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.frame
from .x_session_manager_client import XSessionManagerClient as XSessionManagerClient_379b0f69

class SessionManager(XSessionManagerClient_379b0f69):
    """
    Service Class

    The SessionManager service provides an interface to the session manager of the desktop.
    
    A session manager keeps track of applications that are running when the desktop shuts down and starts them again in the same state they were left when the desktop starts up the next time. To be able to do this the session manager needs cooperation from applications; applications have to provide sufficient information to be started again as well as restore the state they were left in. The normal flow of operation looks like this:

    See Also:
        `API SessionManager <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1SessionManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.SessionManager'
    __ooo_type_name__: str = 'service'



__all__ = ['SessionManager']

