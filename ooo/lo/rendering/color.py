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
# TypeDef
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rendering
import typing
from .color_component import ColorComponent

Color = typing.NewType('Color', typing.Tuple[ColorComponent, ...])
"""
TypeDef type alias

Shorthand for the device-dependent color components, and easier to read.

See Also:
    `API Color <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering.html#a22cfb0d628f89a8edb356ae3231d4e22>`_
"""

