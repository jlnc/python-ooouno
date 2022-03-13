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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb
from ..frame.x_controller import XController as XController_b00e0b8f
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class TableDesign(XController_b00e0b8f, XInitialization_d46c0cca):
    """
    Service Class

    implements a component which allows the creation of tables.
    
    This service implements a user interface for creating tables through a graphical design interface.
    
    The design view of the TableDesign is divided into two parts. The first part contains the rows where columns can be defined for the table. The second part contains the properties of the selected column.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TableDesign <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1TableDesign.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.TableDesign'
    __ooo_type_name__: str = 'service'



__all__ = ['TableDesign']

