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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc


class DataType(object):
    """
    Const Class

    These constants are used to specify database data types which are used to identify the generic SQL types.
    
    The definition is based on JDBC 3.0.
    
    The actual type constant values are equivalent to those in the X/Open CLI.
    
    Precise information about the specific types can be got from XDatabaseMetaData.getTypeInfo().
    
    **since**
    
        OOo 2.0

    See Also:
        `API DataType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1DataType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.DataType'
    __ooo_type_name__: str = 'const'

    BIT = -7
    TINYINT = -6
    SMALLINT = 5
    INTEGER = 4
    BIGINT = -5
    FLOAT = 6
    REAL = 7
    DOUBLE = 8
    NUMERIC = 2
    DECIMAL = 3
    CHAR = 1
    VARCHAR = 12
    LONGVARCHAR = -1
    DATE = 91
    TIME = 92
    TIMESTAMP = 93
    BINARY = -2
    VARBINARY = -3
    LONGVARBINARY = -4
    SQLNULL = 0
    OTHER = 1111
    """
    indicates that the SQL type is database-specific and gets mapped to an object that can be accessed via the method com.sun.star.sdbc.XRow.getObject().
    """
    OBJECT = 2000
    """
    indicates a type which is represented by an object which implements this type.
    """
    DISTINCT = 2001
    """
    describes a type based on a built-in type.
    
    It is a user-defined data type (UDT).
    """
    STRUCT = 2002
    """
    indicates a type consisting of attributes that may be any type.
    
    It is a user-defined data type (UDT).
    """
    ARRAY = 2003
    """
    indicates a type representing an SQL ARRAY.
    """
    BLOB = 2004
    """
    indicates a type representing an SQL Binary Large Object.
    """
    CLOB = 2005
    """
    indicates a type representing an SQL Character Large Object.
    """
    REF = 2006
    """
    indicates a type representing an SQL REF, a referencing type.
    """
    BOOLEAN = 16
    """
    identifies the generic SQL type BOOLEAN.
    
    **since**
    
        OOo 2.0
    """

__all__ = ['DataType']
