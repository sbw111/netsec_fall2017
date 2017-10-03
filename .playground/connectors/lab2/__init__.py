import playground
from netsec_fall2017.lab_2a_handshake import ServerProtocol, ClientProtocol, PassThroughProtocol
from playground.network.common import StackingProtocolFactory

cf = StackingProtocolFactory(lambda: PassThroughProtocol1(), lambda: ClientProtocol())
sf = StackingProtocolFactory(lambda: PassThroughProtocol1(), lambda: ServerProtocol())

lab2_connector = playground.Connector(protocolStack=(cf, sf))
playground.setConnector('lab2_protocol', lab2_connector)
