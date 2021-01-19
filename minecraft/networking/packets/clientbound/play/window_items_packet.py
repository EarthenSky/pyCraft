from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    UnsignedByte, Short
)

from quarry.types.buffer import Buffer1_14

#NOTE: pip install quarry in order to use this packet
# https://github.com/barneygale/quarry/blob/53b2b1c5c482204ec8d87ebae9711971a6db70be/quarry/types/chunk.py

class WindowItemsPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x15 if context.protocol_version == 578 else -1

    packet_name = 'window items'

    def read(self, file_object):
        # make buffer for unpacking slots
        packet_data = file_object.read()
        buff = Buffer1_14( packet_data )

        self.window_id, count = buff.unpack('Bh')

        self.slots = []
        for i in range(0, count):
            self.slots.append( buff.unpack_slot() )
