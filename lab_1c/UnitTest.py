from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from playground.network.common import PortKey
from asyncio import Protocol
from server import MyServerProtocol
from client import MyClientProtocol
import asyncio
from ConnectPackets import RequestConnect
from playground.common import logging as p_logging


def basicUnitTest():

    # asyncio.set_event_loop(TestLoopEx())
    clientProtocol = MyClientProtocol()
    serverProtocol = MyServerProtocol()
    transportToServer = MockTransportToProtocol(serverProtocol)
    transportToClient = MockTransportToProtocol(clientProtocol)
    clientProtocol.connection_made(transportToServer)
    serverProtocol.connection_made(transportToClient)

    packet1 = RequestConnect()
    packet1.iD = "ELROY"
    clientProtocol.transport.write(packet1.__serialize__())

if __name__ == "__main__":
    p_logging.EnablePresetLogging(p_logging.PRESET_TEST)
    basicUnitTest()
    print("Basic Unit Test Successful.")
