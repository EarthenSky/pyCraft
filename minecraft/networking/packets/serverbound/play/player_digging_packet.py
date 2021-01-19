from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    Position, VarInt, Byte
)

class PlayerDiggingPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x1A if context.protocol_version >= 578 else -1
    
    packet_name = "player digging"
    definition = [
        {'Status': VarInt},
        {'Location': Position},
        {'Face': Byte}]