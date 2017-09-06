from playground.network.packet import PacketType
from ConnectPackets import ConnectResult, RequestConnect, VerifyAnswer, VerifyQuestion


def UnitTest_RequestConnect(iD):
	packet1=RequestConnect()
	packet1.iD=iD
	packet1Bytes=packet1.__serialize__()
	packet1a=PacketType.Deserialize(packet1Bytes)
	assert packet1==packet1a


def UnitTest_VerifyQuestion(iD,question):
	packet2=VerifyQuestion()
	packet2.iD=iD
	packet2.question=question
	packet2Bytes=packet2.__serialize__()
	packet2a=PacketType.Deserialize(packet2Bytes)
	assert packet2==packet2a
	
def UnitTest_VerifyAnswer(iD,answer):
	packet3=VerifyAnswer()
	packet3.iD=iD
	packet3.answer=answer
	packet3Bytes=packet3.__serialize__()
	packet3a=PacketType.Deserialize(packet3Bytes)
	assert packet3==packet3a

def UnitTest_ConnectResult(iD,result):
	packet4=ConnectResult()
	packet4.iD=iD
	packet4.result=result
	packet4Bytes=packet4.__serialize__()
	packet4a=PacketType.Deserialize(packet4Bytes)
	assert packet4==packet4a



if __name__=="__main__":
	#1
	UnitTest_RequestConnect("May")
	UnitTest_VerifyQuestion("May","What's your mother's mid name?")
	UnitTest_VerifyAnswer("May",b"It's a secret.")
	UnitTest_ConnectResult("May",False)
	#2
	UnitTest_RequestConnect("Five")
	UnitTest_VerifyQuestion("Five","What's your favorite book?")
	UnitTest_VerifyAnswer("Five",b"Nothing!")
	UnitTest_ConnectResult("Five",True)