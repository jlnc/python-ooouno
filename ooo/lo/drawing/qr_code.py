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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class QRCode(object):
    """
    Struct Class

    This struct defines the attributes of a QR Code.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API QRCode <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1QRCode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.QRCode'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.QRCode'
    """Literal Constant ``com.sun.star.drawing.QRCode``"""

    def __init__(self, Payload: typing.Optional[str] = '', ErrorCorrection: typing.Optional[int] = 0, Border: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Payload (str, optional): Payload value.
            ErrorCorrection (int, optional): ErrorCorrection value.
            Border (int, optional): Border value.
        """
        super().__init__()

        if isinstance(Payload, QRCode):
            oth: QRCode = Payload
            self.Payload = oth.Payload
            self.ErrorCorrection = oth.ErrorCorrection
            self.Border = oth.Border
            return

        kargs = {
            "Payload": Payload,
            "ErrorCorrection": ErrorCorrection,
            "Border": Border,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._payload = kwargs["Payload"]
        self._error_correction = kwargs["ErrorCorrection"]
        self._border = kwargs["Border"]


    @property
    def Payload(self) -> str:
        """
        Text for which QR Code is made.
        """
        return self._payload
    
    @Payload.setter
    def Payload(self, value: str) -> None:
        self._payload = value

    @property
    def ErrorCorrection(self) -> int:
        """
        Qr Code Error Correction Level.
        """
        return self._error_correction
    
    @ErrorCorrection.setter
    def ErrorCorrection(self, value: int) -> None:
        self._error_correction = value

    @property
    def Border(self) -> int:
        """
        Border surrounding the Qr Code It is a non-negative value.
        
        One Border unit is equal to one dot in the generated QR code.
        """
        return self._border
    
    @Border.setter
    def Border(self, value: int) -> None:
        self._border = value


__all__ = ['QRCode']
