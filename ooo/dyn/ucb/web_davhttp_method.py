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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.ucb.WebDAVHTTPMethod import (CONNECT, COPY, DELETE, GET, HEAD, LOCK, MKCOL, MOVE, OPTIONS, PATCH, POST, PROPFIND, PROPPATCH, PUT, TRACE, UNLOCK)

    def _get_enum():
        # Dynamically create class that actually contains UNO enum instances
        _dict = {
            "__doc__": "Dynamically created class that represents com.sun.star.ucb.WebDAVHTTPMethod Enum. Class loosly mimics Enum",
            "__new__": uno_enum_class_new,
            "__ooo_ns__": "com.sun.star.ucb",
            "__ooo_full_ns__": "com.sun.star.ucb.WebDAVHTTPMethod",
            "__ooo_type_name__": "enum",
            "CONNECT": CONNECT,
            "COPY": COPY,
            "DELETE": DELETE,
            "GET": GET,
            "HEAD": HEAD,
            "LOCK": LOCK,
            "MKCOL": MKCOL,
            "MOVE": MOVE,
            "OPTIONS": OPTIONS,
            "PATCH": PATCH,
            "POST": POST,
            "PROPFIND": PROPFIND,
            "PROPPATCH": PROPPATCH,
            "PUT": PUT,
            "TRACE": TRACE,
            "UNLOCK": UNLOCK,
        }
        result = type('WebDAVHTTPMethod', (object,), _dict)
        return result

    WebDAVHTTPMethod = _get_enum()
else:
    from ...lo.ucb.web_davhttp_method import WebDAVHTTPMethod as WebDAVHTTPMethod

__all__ = ['WebDAVHTTPMethod']

