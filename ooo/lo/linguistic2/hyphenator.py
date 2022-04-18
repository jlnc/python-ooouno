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
# Namespace: com.sun.star.linguistic2
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..lang.x_service_display_name import XServiceDisplayName as XServiceDisplayName_a050e2a
from .x_hyphenator import XHyphenator as XHyphenator_ff4e0def
from .x_lingu_service_event_broadcaster import XLinguServiceEventBroadcaster as XLinguServiceEventBroadcaster_3ad01509

class Hyphenator(XComponent_98dc0ab5, XInitialization_d46c0cca, XServiceDisplayName_a050e2a, XHyphenator_ff4e0def, XLinguServiceEventBroadcaster_3ad01509):
    """
    Service Class

    offers hyphenation functionality.

    See Also:
        `API Hyphenator <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1linguistic2_1_1Hyphenator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.Hyphenator'
    __ooo_type_name__: str = 'service'



__all__ = ['Hyphenator']

