from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    Double, Boolean
)


class PlayerPositionPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x11  # this is only updated for version 1.15.2 (=578)

    packet_name = 'player position'
    
    get_definition = staticmethod(lambda context: [
        {'x': Double},
        {'feet_y': Double},
        {'z': Double},
        {'on_ground': Boolean}])
