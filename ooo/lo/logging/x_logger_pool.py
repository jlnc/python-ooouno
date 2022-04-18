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
# Namespace: com.sun.star.logging
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_logger import XLogger as XLogger_9a510aa7

class XLoggerPool(ABC):
    """
    implements a pool for named XLogger instances
    
    **since**
    
        OOo 2.3

    See Also:
        `API XLoggerPool <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1logging_1_1XLoggerPool.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.XLoggerPool'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.logging.XLoggerPool'

    @abstractmethod
    def getDefaultLogger(self) -> 'XLogger_9a510aa7':
        """
        retrieves a logger with the default name \"org.openoffice.logging.DefaultLogger\".
        
        Calling this method is equivalent to calling getNamedLogger( \"org.openoffice.logging.DefaultLogger\" ).
        """
    @abstractmethod
    def getNamedLogger(self, Name: str) -> 'XLogger_9a510aa7':
        """
        retrieves a logger with the given name
        
        Multiple attempts to retrieve a logger with the same name will return the same instance.
        
        Newly created logger instances are initialized via configuration. See the configuration module /org.openoffice.Office.Logging for an explanation of the initialization pattern.
        """

__all__ = ['XLoggerPool']

