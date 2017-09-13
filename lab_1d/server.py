import asyncio
import playground
from playground.network.packet import PacketType
from ConnectPackets import ConnectResult, RequestConnect, VerifyAnswer, VerifyQuestion


class MyServerProtocol(asyncio.Protocol):

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
        peername = transport.get_extra_info('peername')
        print('Build Connection from {}'.format(peername))
        self.transport = transport
        self._deserializer = PacketType.Deserializer()

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            self.__MsgJug(pkt)


loop = asyncio.get_event_loop()

coro = playground.getConnector().create_playground_server(MyServerProtocol, 8888)

server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
