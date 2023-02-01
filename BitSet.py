class BitVector:
    def __init__(self, size):
        self.len = size // 32 + 1
        self.vector = self.len * [0]

    def set(self, index):
        block = self.__find_block(index)
        mask = self.__mask_maker(index)
        self.vector[block] |= mask

    def reset(self, index):
        block = self.__find_block(index)
        mask = self.__mask_maker(index)
        self.vector[block] &= mask

    def view(self):
        for block in self.vector:
            print(bin(block), end = ' ')
        print()
        
    def __mask_maker(self, index):
        if index < 32:
            num = index
        else:
            num = index % 32
        mask = 1 << num
        return mask
    def __find_block(self, index):
        block = index // 32
        return block