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
# Namespace: com.sun.star.awt


class InvalidateStyle(object):
    """
    Const Class

    specifies how to invalidate windows.

    See Also:
        `API InvalidateStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1InvalidateStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.InvalidateStyle'
    __ooo_type_name__: str = 'const'

    CHILDREN = 1
    """
    The child windows are invalidated, too.
    """
    NOCHILDREN = 2
    """
    The child windows are not invalidated.
    """
    NOERASE = 4
    """
    The invalidated area is painted with the background color/pattern.
    """
    UPDATE = 8
    """
    The invalidated area is updated immediately.
    """
    TRANSPARENT = 16
    """
    The parent window is invalidated, too.
    """
    NOTRANSPARENT = 32
    """
    The parent window is not invalidated.
    """
    NOCLIPCHILDREN = 16384
    """
    The area is invalidated regardless of overlapping child windows.
    """

__all__ = ['InvalidateStyle']
