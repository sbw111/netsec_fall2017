import asyncio
import playground
from playground.network.packet import PacketType
from ConnectPackets import ConnectResult, RequestConnect, VerifyAnswer, VerifyQuestion


class MyClientProtocol(asyncio.Protocol):

    def __init__(self, loop):
        self.loop = loop

    def __MsgJug(self, pkt):
        if isinstance(pkt, VerifyQuestion):
            self.__ReturnAnswer(pkt)
        elif isinstance(pkt, ConnectResult):
            print("Final Connect Answer: ", pkt.result)
            # self.loop.stop()

    def connection_made(self, transport):
        self.transport = transport
        self._deserializer = PacketType.Deserializer()
        self.transport.write(self.__GenID())
        print('hi')

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            self.__MsgJug(pkt)

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

    def __GenID(self):
        packet1 = RequestConnect()
        packet1.iD = "ELROY"
        return packet1.__serialize__()

    def __ReturnAnswer(self, pkt):
        packet3 = VerifyAnswer()
        packet3.iD = pkt.iD
        packet3.answer = b"Sze"
        self.transport.write(packet3.__serialize__())

loop = asyncio.get_event_loop()
coro = playground.getConnector().create_playground_connection(lambda: MyClientProtocol(loop), '20174.1.1.1', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
