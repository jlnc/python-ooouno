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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
from .single_backend import SingleBackend as SingleBackend_c64d1280

class LocalSingleBackend(SingleBackend_c64d1280):
    """
    Service Class

    implements SingleBackend that stores data in the local file system using the OOR XML formats.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API LocalSingleBackend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1LocalSingleBackend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.LocalSingleBackend'
    __ooo_type_name__: str = 'service'


__all__ = ['LocalSingleBackend']

