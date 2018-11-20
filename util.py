import math


class Util:

    def encode(self, x):
        # calculate how many bytes are needed to represent integer x except 2 number bits
        x_size = math.ceil((math.log(x + 1, 2) + 2) / 8)

        if x_size != 1:
            # setting number bits
            mask = (x_size - 1) << 6 + ((x_size - 1) * 8)
            x |= mask

        # encode integer as bytes. Big Endian
        x = x.to_bytes(x_size, 'big')

        return x


    def calculateBinaryRequired(self, current):
        size = 1
        check_size = (2 ** size) - 1
        while current > check_size:
            size += 1
            check_size = (2 ** size) - 1

        return size


    def fillZeroCharacter(self, character):

        binvar = str(bin(ord(character)))[2:]
        string_size = len(binvar)

        loop_cnt = (7 - string_size)

        for i in range(loop_cnt):
            binvar = "0" + binvar

        return binvar