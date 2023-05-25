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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from __future__ import annotations
from enum import Enum


class InterruptReason(Enum):
    """
    Enum Class


    See Also:
        `API InterruptReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script.html#a298e9238891ddece524d1b3732aa33e4>`_
    """
    __ooo_ns__: str = "com.sun.star.script"
    __ooo_full_ns__: str = "com.sun.star.script.InterruptReason"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.script.InterruptReason"

    BreakPoint = "BreakPoint"
    """
    script stopped at a breakpoint.
    """
    Cancel = "Cancel"
    """
    script in the engine was cancelled.
    
    script execution was cancelled.
    """
    CompileError = "CompileError"
    """
    script has invalid syntax.
    """
    RuntimeError = "RuntimeError"
    """
    runtime error occurred during script execution.
    """
    Step = "Step"
    """
    script stops because only one scripting engine command was executed.
    """
    StepOut = "StepOut"
    """
    script stops because it leaves a function.
    """
    StepOver = "StepOver"
    """
    script stops because one step was executed.
    """
    StepStatement = "StepStatement"
    """
    script stop because one step was executed.
    """

__all__ = ["InterruptReason"]

