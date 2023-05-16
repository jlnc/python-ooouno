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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class TemplateDescription(metaclass=UnoConstMeta, type_name="com.sun.star.ui.dialogs.TemplateDescription", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ui.dialogs.TemplateDescription``"""
        pass

    class TemplateDescriptionEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ui.dialogs.TemplateDescription", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ui.dialogs.TemplateDescription`` as Enum values"""
        pass

else:
    from com.sun.star.ui.dialogs import TemplateDescription as TemplateDescription

    class TemplateDescriptionEnum(IntEnum):
        """
        Enum of Const Class TemplateDescription

        The implementation of a FilePicker service may support the usage of different templates.
        
        The following constants define the currently specified templates.
        
        **since**
        
            LibreOffice 5.3
        """
        FILEOPEN_SIMPLE = TemplateDescription.FILEOPEN_SIMPLE
        """
        A FileOpen dialog without any additional controls.
        """
        FILESAVE_SIMPLE = TemplateDescription.FILESAVE_SIMPLE
        """
        A FileSave dialog without any additional controls.
        """
        FILESAVE_AUTOEXTENSION_PASSWORD = TemplateDescription.FILESAVE_AUTOEXTENSION_PASSWORD
        """
        A FileSave dialog with additional controls.
        """
        FILESAVE_AUTOEXTENSION_PASSWORD_FILTEROPTIONS = TemplateDescription.FILESAVE_AUTOEXTENSION_PASSWORD_FILTEROPTIONS
        """
        A FileSave dialog with additional controls.
        """
        FILESAVE_AUTOEXTENSION_SELECTION = TemplateDescription.FILESAVE_AUTOEXTENSION_SELECTION
        """
        A FileSave dialog with additional controls.
        """
        FILESAVE_AUTOEXTENSION_TEMPLATE = TemplateDescription.FILESAVE_AUTOEXTENSION_TEMPLATE
        """
        A FileSave dialog with additional controls.
        """
        FILEOPEN_LINK_PREVIEW_IMAGE_TEMPLATE = TemplateDescription.FILEOPEN_LINK_PREVIEW_IMAGE_TEMPLATE
        """
        A FileOpen dialog with additional controls.
        """
        FILEOPEN_PLAY = TemplateDescription.FILEOPEN_PLAY
        """
        A FileOpen dialog with additional controls.
        """
        FILEOPEN_READONLY_VERSION = TemplateDescription.FILEOPEN_READONLY_VERSION
        """
        A FileOpen dialog with additional controls.
        """
        FILEOPEN_LINK_PREVIEW = TemplateDescription.FILEOPEN_LINK_PREVIEW
        """
        A FileOpen dialog with additional controls.
        """
        FILESAVE_AUTOEXTENSION = TemplateDescription.FILESAVE_AUTOEXTENSION
        """
        A FileSave dialog with additional controls.
        """
        FILEOPEN_PREVIEW = TemplateDescription.FILEOPEN_PREVIEW
        """
        A FileOpen dialog with additional controls.
        
        **since**
        
            LibreOffice 5.3
        """
        FILEOPEN_LINK_PLAY = TemplateDescription.FILEOPEN_LINK_PLAY
        """
        A FileOpen dialog with additional controls.
        
        **since**
        
            LibreOffice 5.3
        """
        FILEOPEN_LINK_PREVIEW_IMAGE_ANCHOR = TemplateDescription.FILEOPEN_LINK_PREVIEW_IMAGE_ANCHOR
        """
        A FileOpen dialog with additional controls.
        
        **since**
        
            LibreOffice 6.1
        """

__all__ = ['TemplateDescription', 'TemplateDescriptionEnum']
