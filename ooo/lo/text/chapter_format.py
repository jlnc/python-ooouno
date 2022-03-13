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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text


class ChapterFormat(object):
    """
    Const Class

    These constants define the display format of the chapter number in a chapter text field.

    See Also:
        `API ChapterFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1ChapterFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.ChapterFormat'
    __ooo_type_name__: str = 'const'

    NAME = 0
    """
    The title of the chapter is displayed.
    """
    NUMBER = 1
    """
    The number including prefix and suffix of the chapter is displayed.
    """
    NAME_NUMBER = 2
    """
    The title and number including prefix and suffix of the chapter are displayed.
    """
    NO_PREFIX_SUFFIX = 3
    """
    The name and number of the chapter are displayed.
    """
    DIGIT = 4
    """
    The number of the chapter is displayed.
    """

__all__ = ['ChapterFormat']
