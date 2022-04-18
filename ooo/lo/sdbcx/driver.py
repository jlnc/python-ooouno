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
# Namespace: com.sun.star.sdbcx
from ..sdbc.driver import Driver as Driver_70e70910
from .x_create_catalog import XCreateCatalog as XCreateCatalog_d3410c83
from .x_data_definition_supplier import XDataDefinitionSupplier as XDataDefinitionSupplier_5632104b
from .x_drop_catalog import XDropCatalog as XDropCatalog_bb040bc4

class Driver(Driver_70e70910, XCreateCatalog_d3410c83, XDataDefinitionSupplier_5632104b, XDropCatalog_bb040bc4):
    """
    Service Class

    extends the service com.sun.star.sdbc.Driver by beans for data definition.
    
    This service is optional for each driver. Its purpose is to define a common way for database definition, as the DDL differs between most DBMS.
    
    Definition and deletion of database catalogs can't be defined in a common manner for DBMS, but it should be possible to hide much of the complexity of creation and deletion of catalogs. Each driver could provide methods to cover these tasks.

    See Also:
        `API Driver <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Driver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Driver'
    __ooo_type_name__: str = 'service'



__all__ = ['Driver']

