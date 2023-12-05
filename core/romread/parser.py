import struct

def read_nds_rom(file_path):
    with open(file_path, 'rb') as rom_file:
        header_data = rom_file.read(0x200)
        rom_header = struct.unpack('>4sI4s4sIHHIIIIIIHHHHHHHH', header_data)

        title = rom_header[2].decode('utf-8').rstrip('\x00')
        game_code = rom_header[3].decode('utf-8').rstrip('\x00')
        arm9_rom_offset = rom_header[8]
        arm9_entry_address = rom_header[11]
      # todo : getting game information based on ROM data (CRITICAL!!! THIS IS REQUIRED FOR THE EMULATOR TO WORK [DUH!])

        print(f'Title: {title}')
        print(f'Game Code: {game_code}')
        print(f'Arm9 ROM Offset: {arm9_rom_offset}')
        print(f'Arm9 Entry Address: {hex(arm9_entry_address)}')

if __name__ == "__main__":
    rom_path = "path/to/your/rom.nds"
    read_nds_rom(rom_path)
