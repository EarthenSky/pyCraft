from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    Byte, Short
)

from quarry.types.buffer import Buffer1_14

#NOTE: pip install quarry in order to use this packet
# https://github.com/barneygale/quarry/blob/53b2b1c5c482204ec8d87ebae9711971a6db70be/quarry/types/chunk.py

class SetSlotPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x17 if context.protocol_version == 578 else -1

    packet_name = "set slot"

    def read(self, file_object):
        packet_data = file_object.read()
        buff = Buffer1_14( packet_data )

        # unpack byte & Short
        self.window_id, self.slot = buff.unpack("bh")

        # unpack the slot next
        self.slot_data = buff.unpack_slot() 