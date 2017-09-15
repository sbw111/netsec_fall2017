import asyncio
import playground
from playground.network.packet import PacketType
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory
from ConnectPackets import ConnectResult, RequestConnect, VerifyAnswer, VerifyQuestion
from PassThrough import PassThrough1, PassThrough2


class MyServerProtocol(asyncio.Protocol):

    def __init__(self):
        self.transport = None

    def __MsgJug(self, pkt):
        if isinstance(pkt, RequestConnect):
            packet2 = VerifyQuestion()
            packet2.iD = pkt.iD
            packet2.question = "What's your best friend's first name?"
            self.transport.write(packet2.__serialize__())
        elif isinstance(pkt, VerifyAnswer):
            packet4 = ConnectResult()
            packet4.iD = pkt.iD
            if pkt.answer == b"Sze":
                packet4.result = True
            else:
                packet4.result = False
            self.transport.write(packet4.__serialize__())
            print('Close the client socket')
            self.transport.close()

    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info('peername')
        print('Build Connection from {}'.format(peername))
        self._deserializer = PacketType.Deserializer()

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            self.__MsgJug(pkt)

if __name__ == "__main__":

    f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
    ptConnector = playground.Connector(protocolStack=f)
    playground.setConnector("passthrough", ptConnector)

    loop = asyncio.get_event_loop()
    coro = playground.getConnector('passthrough').create_playground_server(MyServerProtocol, 666)
    server = loop.run_until_complete(coro)
    print("Echo Server Started at {}".format(server.sockets[0].gethostname()))
    loop.run_forever()
    loop.close()
