from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    VarInt
)

class PickItemPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x17 if context.protocol_version >= 578 else -1

    packet_name = "pick item"
    definition = [
        {"slot_to_use": VarInt}
    ]