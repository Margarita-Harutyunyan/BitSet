class BitVector:
    def __init__(self, size):
        self.__len = size // 32 + 1
        self.__vector = self.__len * [0]

    def set(self, index):
        block = self.__find_block(index)
        mask = self.__mask_maker(index)
        self.__vector[block] |= mask

    def reset(self, index):
        block = self.__find_block(index)
        mask = self.__mask_maker(index)
        self.__vector[block] ^= mask

    def view(self):
        for block in self.__vector:
            print(bin(block), end = ' ')
        print()
        
    def __mask_maker(self, index):
        block = self.__find_block(index)
        offset = (self.__len * 32) - index
        mask = 1 << offset
        return mask
    def __find_block(self, index):
        block = index // 32
        return block
