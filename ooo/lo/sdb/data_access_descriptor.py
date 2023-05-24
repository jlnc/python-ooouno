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
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c
    from ..sdbc.x_result_set import XResultSet as XResultSet_98e30aa7

class DataAccessDescriptor(ABC):
    """
    Service Class

    descriptor for accessing basic data access objects.
    
    Various components interacting with the database access world require to specify (or provide themselves) an object such as a query, a table, a result set, a connection to a data source, a column within a table, and so on.All of these objects are usually not specified with a single property, but with a set of properties, and for various objects, various (but not always different) properties are needed.The DataAccessDescriptor describes the super set of the properties for the most common data access objects.
    
    Every component providing or requiring a DataAccessDescriptor for some functionality is urged to specify which properties are mandatory, and which ones optional. Additionally, it's free to specify any additional requirements about the relations of properties.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DataAccessDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DataAccessDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DataAccessDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ConnectionInfo(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        specifies additional info to use when creating a connection from a ConnectionResource
        
        This member is evaluated only when ConnectionResource is used: In this case, com.sun.star.sdbc.XDriverManager.getConnectionWithInfo() is used to create a connection for the given connection resource, instead of com.sun.star.sdbc.XDriverManager.getConnection().
        
        If the sequence is empty, it is ignored.
        """
        ...

    @abstractproperty
    def Selection(self) -> typing.Tuple[object, ...]:
        """
        specifies a selection to confine the records in a result set.
        
        When you specify a result set either implicitly (DataSourceName, Command, CommandType) or explicitly (ResultSet), the set of results can be additionally refined with this property.
        
        The single elements of the Selection are either record numbers (see com.sun.star.sdbc.XResultSet.getRow()), or bookmarks (see com.sun.star.sdbcx.XRowLocate.getBookmark()).It is up to the component which provides or requires a DataAccessDescriptor to specify which of the two alternatives it expects. If it does not specify this, then the property BookmarkSelection becomes mandatory.
        
        If the elements specify bookmarks, and a ResultSet has been specified, then this result set is required to support the com.sun.star.sdbcx.XRowLocate interface.
        """
        ...

    @abstractproperty
    def ActiveConnection(self) -> XConnection_a36a0b0c:
        """
        is a connection to use.
        
        This object is guaranteed to be a com.sun.star.sdbc.Connection, but usually it will be a Connection from the module com.sun.star.sdb.Especially in the case where no DataSourceName is given, but CommandType is CommandType.QUERY, the ActiveConnection needs to fully support the Connection service, to actually retrieve the query specified by Command
        
        If no ActiveConnection is given, then a DataSourceName is required.
        """
        ...

    @abstractproperty
    def BookmarkSelection(self) -> bool:
        """
        specifies how to interpret Selection
        
        If present, BookmarkSelection specifies the semantics of Selection. If not present, it's up to the implementing component to specify this semantics.
        
        If TRUE, then the single elements of the array specified by Selection are bookmarks relative to the result set, if FALSE, they're record numbers.
        """
        ...

    @abstractproperty
    def Column(self) -> XPropertySet_bc180bfa:
        """
        specifies a column object
        
        For reasons of performance and saving resources, a supplier of an DataAccessDescriptor which is used to describe a column object can pass this object directly, instead of specifying it only implicitly with the ColumnName property.
        
        The object will at least support the com.sun.star.sdbcx.Column service, but more often it will even be a Column from the com.sun.star.sdb module.
        """
        ...

    @abstractproperty
    def ColumnName(self) -> str:
        """
        specifies a column name.
        
        This property is usually used together with the Command and CommandType properties.
        """
        ...

    @abstractproperty
    def Command(self) -> str:
        """
        specifies the command to execute to retrieve a result set.
        
        This property is only meaningful together with the CommandType property, thus either both or none of them are present.
        """
        ...

    @abstractproperty
    def CommandType(self) -> int:
        """
        specifies the type of the command to be executed to retrieve a result set.
        
        Command needs to be interpreted depending on the value of this property.
        
        This property is only meaningful together with the Command property, thus either both or none of them are present.
        """
        ...

    @abstractproperty
    def ConnectionResource(self) -> str:
        """
        specifies the database URL which locates a database driver.
        
        This database URL is usually used to create a Connection. If no ConnectionResource is given, then an ActiveConnection is required.
        """
        ...

    @abstractproperty
    def DataSourceName(self) -> str:
        """
        specifies the name of the datasource to access.
        
        This data source is usually used to create a Connection. If no DataSourceName is given and the DatabaseLocation and the ConnectionResource are empty, then an ActiveConnection is required.
        """
        ...

    @abstractproperty
    def DatabaseLocation(self) -> str:
        """
        specifies the URL of the database file.
        
        This database location is usually used to create a Connection. If no DatabaseLocation is given and the ConnectionResource is empty, then an ActiveConnection is required.
        """
        ...

    @abstractproperty
    def EscapeProcessing(self) -> bool:
        """
        specifies if the Command should be analyzed on the client side before sending it to the database server.
        
        The default value of this property is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        
        This property is usually present together with the Command and CommandType properties, and is evaluated if and only if CommandType equals CommandType.COMMAND.
        """
        ...

    @abstractproperty
    def Filter(self) -> str:
        """
        specifies an additional filter to optionally use.
        
        The Filter string has to form a WHERE-clause, without the WHERE-string itself.
        
        If a DataSourceName, Command and CommandType are specified, a RowSet can be created with this information. If the results provided by the row set are to be additionally filtered, the Filter property can be used.
        
        Note that the Filter property does not make sense if a ResultSet has been specified in the DataAccessDescriptor.
        """
        ...

    @abstractproperty
    def GroupBy(self) -> str:
        """
        specifies an additional GROUP BY clause which should be applied on top of the given Command.
        
        The keyword GROUP BY itself is not part of this property.
        """
        ...

    @abstractproperty
    def HavingClause(self) -> str:
        """
        specifies an additional HAVING clause which should be applied on top of the given Command.
        
        The keyword HAVING itself is not part of this property.
        """
        ...

    @abstractproperty
    def Order(self) -> str:
        """
        specifies an additional ORDER BY clause which should be applied on top of the given Command.
        
        The keyword ORDER BY itself is not part of this property.
        """
        ...

    @abstractproperty
    def ResultSet(self) -> XResultSet_98e30aa7:
        """
        specifies an already existent result set to use.
        
        Usually, you use the properties DataSourceName (alternatively ActiveConnection), Command and CommandType to specify how to obtain a result set. However, in scenarios where the provider of a DataAccessDescriptor has access to an already existent result set, it can pass it along for reusage. This is encouraged to increase performance.
        
        The object will at least support the com.sun.star.sdbc.ResultSet service.
        
        Note that any superservices of com.sun.star.sdbc.ResultSet are also allowed. Especially, this member can denote an instance of the com.sun.star.sdb.RowSet, or an instance obtained by calling com.sun.star.sdb.XResultSetAccess.createResultSet() on such a com.sun.star.sdb.RowSet. This becomes important in conjunction with the Selection property.
        """
        ...


__all__ = ['DataAccessDescriptor']

