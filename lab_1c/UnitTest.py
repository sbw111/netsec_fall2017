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
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(clientProtocol, serverProtocol)
    clientProtocol.connection_made(cTransport)
    serverProtocol.connection_made(sTransport)

    packet1 = RequestConnect()
    packet1.iD = "ELROY"
    clientProtocol.transport.write(packet1.__serialize__())

if __name__ == "__main__":
    # p_logging.EnablePresetLogging(p_logging.PRESET_TEST)
    basicUnitTest()
    print("Basic Unit Test Successful.")
