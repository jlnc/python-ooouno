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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.scanner.scan_error import ScanError as ScanError
except ImportError:
    pass
try:
    from ...dyn.scanner.scanner_context import ScannerContext as ScannerContext
except ImportError:
    pass
try:
    from ...dyn.scanner.scanner_exception import ScannerException as ScannerException
except ImportError:
    pass
try:
    from ...dyn.scanner.scanner_manager import ScannerManager as ScannerManager
except ImportError:
    pass
try:
    from ...dyn.scanner.x_scanner_manager import XScannerManager as XScannerManager
except ImportError:
    pass
try:
    from ...dyn.scanner.x_scanner_manager2 import XScannerManager2 as XScannerManager2
except ImportError:
    pass
