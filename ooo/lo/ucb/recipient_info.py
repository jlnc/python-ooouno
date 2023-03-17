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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .outgoing_message_state import OutgoingMessageState as OutgoingMessageState_c200e54


class RecipientInfo(object):
    """
    Struct Class

    contains all information needed to send a message using one send protocol.
    
    To send one message via two different protocols, two RecipientInfos are needed - to send one message to different users with one protocol, one RecipientInfo can be used.

    See Also:
        `API RecipientInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RecipientInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.RecipientInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.RecipientInfo'
    """Literal Constant ``com.sun.star.ucb.RecipientInfo``"""

    def __init__(self, ProtocolType: typing.Optional[str] = '', State: typing.Optional[OutgoingMessageState_c200e54] = OutgoingMessageState_c200e54.WRITTEN, To: typing.Optional[str] = '', CC: typing.Optional[str] = '', BCC: typing.Optional[str] = '', Newsgroups: typing.Optional[str] = '', Server: typing.Optional[str] = '', Username: typing.Optional[str] = '', Password: typing.Optional[str] = '', VIMPostOfficePath: typing.Optional[str] = '', ProtocolErrorString: typing.Optional[str] = '', ProtocolErrorNumber: typing.Optional[int] = 0, SendTries: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            ProtocolType (str, optional): ProtocolType value.
            State (OutgoingMessageState, optional): State value.
            To (str, optional): To value.
            CC (str, optional): CC value.
            BCC (str, optional): BCC value.
            Newsgroups (str, optional): Newsgroups value.
            Server (str, optional): Server value.
            Username (str, optional): Username value.
            Password (str, optional): Password value.
            VIMPostOfficePath (str, optional): VIMPostOfficePath value.
            ProtocolErrorString (str, optional): ProtocolErrorString value.
            ProtocolErrorNumber (int, optional): ProtocolErrorNumber value.
            SendTries (int, optional): SendTries value.
        """
        super().__init__()

        if isinstance(ProtocolType, RecipientInfo):
            oth: RecipientInfo = ProtocolType
            self.ProtocolType = oth.ProtocolType
            self.State = oth.State
            self.To = oth.To
            self.CC = oth.CC
            self.BCC = oth.BCC
            self.Newsgroups = oth.Newsgroups
            self.Server = oth.Server
            self.Username = oth.Username
            self.Password = oth.Password
            self.VIMPostOfficePath = oth.VIMPostOfficePath
            self.ProtocolErrorString = oth.ProtocolErrorString
            self.ProtocolErrorNumber = oth.ProtocolErrorNumber
            self.SendTries = oth.SendTries
            return

        kargs = {
            "ProtocolType": ProtocolType,
            "State": State,
            "To": To,
            "CC": CC,
            "BCC": BCC,
            "Newsgroups": Newsgroups,
            "Server": Server,
            "Username": Username,
            "Password": Password,
            "VIMPostOfficePath": VIMPostOfficePath,
            "ProtocolErrorString": ProtocolErrorString,
            "ProtocolErrorNumber": ProtocolErrorNumber,
            "SendTries": SendTries,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._protocol_type = kwargs["ProtocolType"]
        self._state = kwargs["State"]
        self._to = kwargs["To"]
        self._cc = kwargs["CC"]
        self._bcc = kwargs["BCC"]
        self._newsgroups = kwargs["Newsgroups"]
        self._server = kwargs["Server"]
        self._username = kwargs["Username"]
        self._password = kwargs["Password"]
        self._vim_post_office_path = kwargs["VIMPostOfficePath"]
        self._protocol_error_string = kwargs["ProtocolErrorString"]
        self._protocol_error_number = kwargs["ProtocolErrorNumber"]
        self._send_tries = kwargs["SendTries"]


    @property
    def ProtocolType(self) -> str:
        """
        the protocol to use for sending (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """
        return self._protocol_type
    
    @ProtocolType.setter
    def ProtocolType(self, value: str) -> None:
        self._protocol_type = value

    @property
    def State(self) -> OutgoingMessageState_c200e54:
        """
        the current state of the message.
        """
        return self._state
    
    @State.setter
    def State(self, value: OutgoingMessageState_c200e54) -> None:
        self._state = value

    @property
    def To(self) -> str:
        """
        the recipient(s) (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._to
    
    @To.setter
    def To(self, value: str) -> None:
        self._to = value

    @property
    def CC(self) -> str:
        """
        the recipient(s) of a \"carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._cc
    
    @CC.setter
    def CC(self, value: str) -> None:
        self._cc = value

    @property
    def BCC(self) -> str:
        """
        the recipient(s) of \"blind carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._bcc
    
    @BCC.setter
    def BCC(self, value: str) -> None:
        self._bcc = value

    @property
    def Newsgroups(self) -> str:
        """
        the newsgroup(s) to which an article is be posted.
        
        Multiple addresses are separated by commas.
        """
        return self._newsgroups
    
    @Newsgroups.setter
    def Newsgroups(self, value: str) -> None:
        self._newsgroups = value

    @property
    def Server(self) -> str:
        """
        the name of the server to be used for sending the message.
        """
        return self._server
    
    @Server.setter
    def Server(self, value: str) -> None:
        self._server = value

    @property
    def Username(self) -> str:
        """
        the user name to be used for authorizing on the send server.
        """
        return self._username
    
    @Username.setter
    def Username(self, value: str) -> None:
        self._username = value

    @property
    def Password(self) -> str:
        """
        the password to be used for authorizing on the send server.
        """
        return self._password
    
    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value

    @property
    def VIMPostOfficePath(self) -> str:
        """
        the Post Office Path (VIM only).
        """
        return self._vim_post_office_path
    
    @VIMPostOfficePath.setter
    def VIMPostOfficePath(self, value: str) -> None:
        self._vim_post_office_path = value

    @property
    def ProtocolErrorString(self) -> str:
        """
        string representing the last error (generated by send server).
        """
        return self._protocol_error_string
    
    @ProtocolErrorString.setter
    def ProtocolErrorString(self, value: str) -> None:
        self._protocol_error_string = value

    @property
    def ProtocolErrorNumber(self) -> int:
        """
        the number representing the last error (generated by send server).
        """
        return self._protocol_error_number
    
    @ProtocolErrorNumber.setter
    def ProtocolErrorNumber(self, value: int) -> None:
        self._protocol_error_number = value

    @property
    def SendTries(self) -> int:
        """
        the count of tries to send a message.
        
        This count is 1 if the message was sent with the first try and increases with every unsuccessful retry.
        """
        return self._send_tries
    
    @SendTries.setter
    def SendTries(self, value: int) -> None:
        self._send_tries = value


__all__ = ['RecipientInfo']
