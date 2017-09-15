import asyncio
import playground
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory


class PassThrough1(StackingProtocol):

    def connection_made(self, transport):
        self.transport = transport
        print('1:Start Call Connection')
        self.higherProtocol().connection_made(StackingTransport(self.transport))

    def data_received(self, data):
        print('1:Start transport data')
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        print('1:Close Connection')
        self.higherProtocol().connection_lost(exc)


class PassThrough2(StackingProtocol):

    def connection_made(self, transport):
        self.transport = transport
        print('2:Start Call Connection')
        self.higherProtocol().connection_made(StackingTransport(self.transport))

    def data_received(self, data):
        print('2:Start transport data')
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        print('2:Close Connection')
        self.higherProtocol().connection_lost(exc)
