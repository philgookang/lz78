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

# encrypyt 할때 dic 사용 해야 되는지, decrypt 할때 사용하면 되는거징
# 파일 인코딩을 직접 bit 단위로 해야하는건가요?