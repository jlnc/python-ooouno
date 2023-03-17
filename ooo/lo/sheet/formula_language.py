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
# Namespace: com.sun.star.sheet


class FormulaLanguage(object):
    """
    Const Class

    Constants designating the formula language used with XFormulaOpCodeMapper methods.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API FormulaLanguage <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FormulaLanguage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FormulaLanguage'
    __ooo_type_name__: str = 'const'

    ODFF = 0
    """
    Function names and operators as defined by the OASIS OpenDocument Format (ODF) Formula specification (ODFF aka OpenFormula).
    """
    ODF_11 = 1
    """
    Function names and operators as used in ODF documents prior to the ODFF specification, up to ODF v1.1.
    """
    ENGLISH = 2
    """
    Function names and operators as used in the English language user interface.
    """
    NATIVE = 3
    """
    Function names and operators as used in the current native language user interface.
    """
    XL_ENGLISH = 4
    """
    Function names and operators as used in the English version of Excel.
    
    This formula language is also used in VBA formulas.
    """
    OOXML = 5
    """
    Function names and operators as used in OOXML.
    
    **since**
    
        LibreOffice 4.2
    """
    API = 6
    """
    Function names and operators as used with XFunctionAccess and other API context.
    
    Names are mostly identical to ENGLISH and ODF_11, but while ENGLISH names can be adapted to UI needs and ODF_11 has to stay error compatible, the API names strive to stay compatible but may get corrected in case of errors. Earlier versions than LibreOffice 5.3 always used ODF_11 in API context.
    
    **since**
    
        LibreOffice 5.3
    """

__all__ = ['FormulaLanguage']
