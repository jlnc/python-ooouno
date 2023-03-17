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
# Libre Office Version: 7.4
from enum import Enum


class IOErrorCode(Enum):
    """
    Enum Class

    

    See Also:
        `API IOErrorCode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#ab0378c2985abaca86838ed9936c3a2d5>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.IOErrorCode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.ucb.IOErrorCode'

    ABORT = 'ABORT'
    """
    An operation was aborted.
    """
    ACCESS_DENIED = 'ACCESS_DENIED'
    """
    An object cannot be accessed due to insufficient user rights.
    """
    ALREADY_EXISTING = 'ALREADY_EXISTING'
    """
    An object already exists.
    """
    BAD_CRC = 'BAD_CRC'
    """
    A bad checksum.
    """
    CANT_CREATE = 'CANT_CREATE'
    """
    An object could not be created.
    """
    CANT_READ = 'CANT_READ'
    """
    Data could not be read from a file.
    """
    CANT_SEEK = 'CANT_SEEK'
    """
    A seek operation could not be run.
    """
    CANT_TELL = 'CANT_TELL'
    """
    A tell operation could not be run.
    """
    CANT_WRITE = 'CANT_WRITE'
    """
    Data could not be written to a file.
    """
    CURRENT_DIRECTORY = 'CURRENT_DIRECTORY'
    """
    A function is not possible because the path contains the current directory.
    """
    DEVICE_NOT_READY = 'DEVICE_NOT_READY'
    """
    A device (drive) not ready.
    """
    DIFFERENT_DEVICES = 'DIFFERENT_DEVICES'
    """
    A function is not possible because the devices (drives) are not identical.
    """
    GENERAL = 'GENERAL'
    """
    A general input/output error.
    """
    INVALID_ACCESS = 'INVALID_ACCESS'
    """
    An invalid attempt was made to access an object.
    """
    INVALID_CHARACTER = 'INVALID_CHARACTER'
    """
    A file name contains invalid characters.
    """
    INVALID_DEVICE = 'INVALID_DEVICE'
    """
    A specified device is invalid.
    """
    INVALID_LENGTH = 'INVALID_LENGTH'
    """
    Invalid data length.
    """
    INVALID_PARAMETER = 'INVALID_PARAMETER'
    """
    An operation was started with an invalid parameter.
    """
    IS_WILDCARD = 'IS_WILDCARD'
    """
    An operation cannot be run on file names containing wildcards.
    """
    LOCKING_VIOLATION = 'LOCKING_VIOLATION'
    """
    A locking problem.
    """
    MISPLACED_CHARACTER = 'MISPLACED_CHARACTER'
    """
    An invalid file name.
    """
    NAME_TOO_LONG = 'NAME_TOO_LONG'
    """
    A file name is too long.
    """
    NOT_EXISTING = 'NOT_EXISTING'
    """
    A nonexistent object.
    """
    NOT_EXISTING_PATH = 'NOT_EXISTING_PATH'
    """
    The path to a file does not exist.
    """
    NOT_SUPPORTED = 'NOT_SUPPORTED'
    """
    An action is not supported.
    """
    NO_DIRECTORY = 'NO_DIRECTORY'
    """
    An object is not a directory.
    """
    NO_FILE = 'NO_FILE'
    """
    An object is not a file.
    """
    OUT_OF_DISK_SPACE = 'OUT_OF_DISK_SPACE'
    """
    No more space on a device.
    """
    OUT_OF_FILE_HANDLES = 'OUT_OF_FILE_HANDLES'
    """
    No more file handles available.
    """
    OUT_OF_MEMORY = 'OUT_OF_MEMORY'
    """
    An operation could not be run due to insufficient memory.
    """
    PENDING = 'PENDING'
    """
    An operation is still pending.
    """
    RECURSIVE = 'RECURSIVE'
    """
    An object cannot be copied into itself.
    """
    UNKNOWN = 'UNKNOWN'
    """
    Unknown.
    
    An unknown I/O error has occurred.
    """
    WRITE_PROTECTED = 'WRITE_PROTECTED'
    """
    A function is not possible because the object is write protected.
    """
    WRONG_FORMAT = 'WRONG_FORMAT'
    """
    An incorrect file format.
    """
    WRONG_VERSION = 'WRONG_VERSION'
    """
    An incorrect file version.
    """

__all__ = ['IOErrorCode']

