from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING, BUFFER, BOOL, INT


class RequestConnect(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.bshi.RequestConnect"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("iD", STRING)
    ]


class VerifyQuestion(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.bshi.VerifyQuestion"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("iD", STRING),
        ("question", STRING)
    ]


class VerifyAnswer(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.bshi.VerifyAnswer"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("iD", STRING),
        ("answer", BUFFER)
    ]


class ConnectResult(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.bshi.ConnectResult"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("iD", STRING),
        ("result", BOOL)
    ]
