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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 7.4
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:

    def _get_class():
        orig_init = None
        ordered_keys = ('Message', 'Context')
        def init(self, *args, **kwargs):
            if len(kwargs) == 0 and len(args) == 1 and getattr(args[0], "__class__", None) == self.__class__:
                orig_init(self, args[0])
                return
            kargs = kwargs.copy()
            for i, arg in enumerate(args):
                kargs[ordered_keys[i]] = arg
            orig_init(self, **kargs)

        type_name = 'com.sun.star.document.LockFileIgnoreRequest'
        ex = uno.getClass(type_name)
        ex.__ooo_ns__ = 'com.sun.star.document'
        ex.__ooo_full_ns__= type_name
        ex.__ooo_type_name__ = 'exception'
        orig_init = ex.__init__
        ex.__init__ = init
        return ex

    LockFileIgnoreRequest = _get_class()

else:
    if TYPE_CHECKING:
        from com.sun.star.document import LockFileIgnoreRequest as LockFileIgnoreRequest
    else:
        from ...lo.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest

__all__ = ['LockFileIgnoreRequest']

