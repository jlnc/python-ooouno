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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.animations
# Libre Office Version: 7.4
from __future__ import annotations
from enum import Enum


class Timing(Enum):
    """
    Enum Class

    ENUM Timing

    See Also:
        `API Timing <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations.html#ad073880fe621cbabcd7a7cf904ef332f>`_
    """
    __ooo_ns__: str = "com.sun.star.animations"
    __ooo_full_ns__: str = "com.sun.star.animations.Timing"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.animations.Timing"

    INDEFINITE = "INDEFINITE"
    """
    specifies that a duration, end or start time is indefinite
    """
    MEDIA = "MEDIA"
    """
    specifies a simple duration as the intrinsic media duration.
    
    This is only valid for elements that define media.
    """

__all__ = ["Timing"]

