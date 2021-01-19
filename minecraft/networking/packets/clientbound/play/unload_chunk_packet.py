from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    Integer
)

class UnloadChunkPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x1E if context.protocol_version == 578 else -1

    packet_name = 'unload chunk packet'

    definition = [
        {'chunk_x': Integer},
        {'chunk_z': Integer}
    ]
