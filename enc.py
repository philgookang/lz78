
from bitarray import bitarray

bits = bitarray()

bits.extend(str(bin(1))[2:])
bits.extend(str(bin(2))[2:])
bits.extend(str(bin(3))[2:])
bits.extend(str(bin(4))[2:])
bits.extend(str(bin(21))[2:])
bits.extend(str(bin(ord('l')))[2:])

# print(str(bin(1)), bin(2), bin(3), bin(4), bin(21), bin(ord('l')))
# print(bits)


print(str(bin(ord("a")))[2:])
print(str(bin(ord("x")))[2:])
print(str(bin(ord(" ")))[2:])

o2 = chr(int('0100000', 2))

print("--" + o2 + "--")




# vv = str(bin(2)).format(14, "08b")
print( '{:0b}'.format(1) )
print( '{:0b}'.format(4) )
print( '{:04b}'.format(2) )
print( '{:08b}'.format(21) )
print( '{:016b}'.format(2) )
print( '{:032b}'.format(2) )
print( '{:032b}'.format(22100123) )

# for i in range(1, 2500):
#     i


print('--')
print(int('1', 2))
print(int('00000000010', 2))
# print(int('00000010', 2))
# print(int('00000001010100010011100010011011', 2))


def calculateBinaryRequired(current):
    size = 1
    check_size = (2**size) - 1
    while current > check_size:
        size += 1
        check_size = (2 ** size) - 1

    return size

def fillZero(size, binstr):

    strlen = len(binstr)
    filllen = size - strlen

    for i in range(filllen):
        binstr = "0" + binstr

    return binstr

# print(calculateBinaryRequired(1))
# print(calculateBinaryRequired(4))
# print(calculateBinaryRequired(21))


# print( '{:0b}'.format(4) )

'''
print()
for i in range(3000):
    print(calculateBinaryRequired(i), i, bin(i))
'''


print("++")

output = [(0, 'a'), (1, 'a'), (0, 'b'), (3, 'a'), (4, 'a'), (5, 'a'), (4, 'b')]
print(output)

binary_list = bitarray()
skip = []
binary_temp_list = []


for idx,o in enumerate(output):


    size = calculateBinaryRequired(idx)

    skip.append(size)

    node_id = o[0]
    node_edge = o[1]
    node_id_bin = fillZero(size, str(bin(node_id))[2:])

    bb = '{:0'+str(size)+'b}'
    aa = bb.format(node_id)

    binary_list.extend(aa)
    binary_list.extend(str(bin(ord(node_edge)))[2:])

    binary_temp_list.append([node_id_bin, str(bin(ord(node_edge)))[2:]])



with open('somefile.bin', 'wb') as fh:
    binary_list.tofile(fh)


print(binary_list)


binary_list = bitarray()
with open('somefile.bin', 'rb') as fh:
    binary_list.fromfile(fh)


start = 0
end = 1
size = 1
idx = 0

decode_output_list = []

ttmptmp = []

ooo = len(binary_list)

while True:

    if start >= ooo:
        break

    size = calculateBinaryRequired((idx + 1))

    node_id = binary_list[start:end]
    node_edge = binary_list[end:(end + 7)]

    start = (end + 7)
    end = start + size

    ttmptmp.append([node_id, node_edge])

    o1 = int(node_id.to01(), 2)
    o2 = chr(int(node_edge.to01(), 2))


    a = (o1, o2)
    decode_output_list.append(a)

    idx += 1




print(decode_output_list)





