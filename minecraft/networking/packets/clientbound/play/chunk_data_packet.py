from minecraft.networking.packets import Packet
from minecraft.networking.types import (
    VarInt, Integer, Boolean, Short, UnsignedByte
)

from quarry.types.buffer import Buffer1_14

#NOTE: pip install quarry in order to use this packet!!!
# https://github.com/barneygale/quarry/blob/53b2b1c5c482204ec8d87ebae9711971a6db70be/quarry/types/chunk.py


class ChunkData:
    def __init__(self):
        pass

    def read(self, file_object):
        # Unpacking chunk
        packet_data = file_object.read()
        buff = Buffer1_14(packet_data)

        self.chunk_x, self.chunk_z, self.full_chunk = buff.unpack('ii?')

        if(self.full_chunk == False):
            print("IGNORED FULL CHUNK PACKET")
            return # ignore full chunk calls while in development

        self.primary_bitmask = buff.unpack_varint()
        
        self.heightmap = buff.unpack_nbt()
        #self.motion_blcoking = self.heightmap.body.value['MOTION_BLOCKING'].value

        if(self.full_chunk == True): 
            self.biomes = buff.unpack_array('I', 1024) # changed in 1.15
        else:
            self.biomes = None  

        self.data_size = buff.unpack_varint()
        self.chunk_sections = buff.unpack_chunk(self.primary_bitmask)  # 3D array

        self.block_entities = [buff.unpack_nbt() for _ in range(buff.unpack_varint())]


class ChunkDataPacket(Packet):
    @staticmethod
    def get_id(context):
        return 0x22 #if context.protocol_version >= 578 else -1

    packet_name = 'chunk data packet'

    def read(self, file_object):
        self.chunk_data = ChunkData()
        self.chunk_data.read(file_object)  
        #TODO: if performance is an issue, possibly dont read until cpu is more free.
    
    # do i need this?
    def write_fields(self, packet_buffer):
        pass
