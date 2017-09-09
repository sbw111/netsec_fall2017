import asyncio
from playground.network.packet import PacketType
from ConnectPackets import ConnectResult, RequestConnect, VerifyAnswer, VerifyQuestion


class MyClientProtocol(asyncio.Protocol):

    def __init__(self, loop):
        self.transport = None
        self.loop = loop

    def connection_made(self, transport):
        self.transport = transport
        self._deserializer = PacketType.Deserializer()
        transport.write(self.__GenID())

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            if pkt != None:
                if pkt.DEFINITION_IDENTIFIER == "lab1b.bshi.VerifyQuestion":
                    self.__ReturnAnswer(pkt)
                elif pkt.DEFINITION_IDENTIFIER == "lab1b.bshi.ConnectResult":
                    print(pkt.result)

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.transport = None
        self.loop.Stop()

    def __GenID(self):
        packet1 = RequestConnect()
        packet1.iD = "ELROY"
        return packet1.__serialize__()

    def __ReturnAnswer(self, pkt):
        packet3 = VerifyAnswer()
        packet3.iD = pkt.iD
        packet3.answer = b"Sze"
        self.transport.write(packet3.__serialize__())
'''
loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: MyClientProtocol(), '127.0.0.1', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
'''