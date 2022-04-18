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
# Namespace: com.sun.star.sheet
from ..container.x_child import XChild as XChild_a6390b07
from .x_sheet_annotation import XSheetAnnotation as XSheetAnnotation_ef4a0d8d
from .x_sheet_annotation_shape_supplier import XSheetAnnotationShapeSupplier as XSheetAnnotationShapeSupplier_c37312d2
from ..text.x_simple_text import XSimpleText as XSimpleText_a5ca0b34

class CellAnnotation(XChild_a6390b07, XSheetAnnotation_ef4a0d8d, XSheetAnnotationShapeSupplier_c37312d2, XSimpleText_a5ca0b34):
    """
    Service Class

    represents a cell annotation object attached to a spreadsheet cell.

    See Also:
        `API CellAnnotation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1CellAnnotation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.CellAnnotation'
    __ooo_type_name__: str = 'service'



__all__ = ['CellAnnotation']

