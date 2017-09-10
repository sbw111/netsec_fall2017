from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from playground.network.common import PortKey
from asyncio import Protocol
from server import MyServerProtocol
from client import MyClientProtocol
import asyncio


def basicUnitTest():

    asyncio.set_event_loop(TestLoopEx())
    server = MyServerProtocol()
    client = MyClientProtocol()
    transportToServer = MockTransportToProtocol(server)
    transportToClient = MockTransportToProtocol(client)
    server.connection_made(transportToClient)
    client.connection_made(transportToServer)

if __name__ == "__main__":
    basicUnitTest()
    print("Basic Unit Test Successful.")
