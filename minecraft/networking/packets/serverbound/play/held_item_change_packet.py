from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    Short
)

class HeldItemChangePacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x23 if context.protocol_version >= 578 else -1

    packet_name = "held item change"
    definition = [
        {"slot": Short}
    ] 