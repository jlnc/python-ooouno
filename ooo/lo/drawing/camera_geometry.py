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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .direction3_d import Direction3D as Direction3D_c9370c0c
from .position3_d import Position3D as Position3D_bddc0bc0


class CameraGeometry(object):
    """
    Struct Class

    specifies a three-dimensional camera.

    See Also:
        `API CameraGeometry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1CameraGeometry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.CameraGeometry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.CameraGeometry'
    """Literal Constant ``com.sun.star.drawing.CameraGeometry``"""

    def __init__(self, vrp: typing.Optional[Position3D_bddc0bc0] = UNO_NONE, vpn: typing.Optional[Direction3D_c9370c0c] = UNO_NONE, vup: typing.Optional[Direction3D_c9370c0c] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            vrp (Position3D, optional): vrp value.
            vpn (Direction3D, optional): vpn value.
            vup (Direction3D, optional): vup value.
        """
        super().__init__()

        if isinstance(vrp, CameraGeometry):
            oth: CameraGeometry = vrp
            self.vrp = oth.vrp
            self.vpn = oth.vpn
            self.vup = oth.vup
            return

        kargs = {
            "vrp": vrp,
            "vpn": vpn,
            "vup": vup,
        }
        if kargs["vrp"] is UNO_NONE:
            kargs["vrp"] = None
        if kargs["vpn"] is UNO_NONE:
            kargs["vpn"] = None
        if kargs["vup"] is UNO_NONE:
            kargs["vup"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._vrp = kwargs["vrp"]
        self._vpn = kwargs["vpn"]
        self._vup = kwargs["vup"]


    @property
    def vrp(self) -> Position3D_bddc0bc0:
        """
        is the camera position
        """
        return self._vrp
    
    @vrp.setter
    def vrp(self, value: Position3D_bddc0bc0) -> None:
        self._vrp = value

    @property
    def vpn(self) -> Direction3D_c9370c0c:
        """
        is the camera view direction
        """
        return self._vpn
    
    @vpn.setter
    def vpn(self, value: Direction3D_c9370c0c) -> None:
        self._vpn = value

    @property
    def vup(self) -> Direction3D_c9370c0c:
        """
        is the camera up direction
        """
        return self._vup
    
    @vup.setter
    def vup(self, value: Direction3D_c9370c0c) -> None:
        self._vup = value


__all__ = ['CameraGeometry']
