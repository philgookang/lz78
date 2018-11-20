from util import *
from bitarray import bitarray

class Fileio:

    def read_text(self, input_file):
        return_list = list()
        with open(input_file) as ins:
            for line in ins:
                return_list.append(line)
        return return_list

    def save_text(self, filename, string_to_save):
        file = open(filename, 'w')
        file.write(string_to_save)
        file.close()


    def save_binary(self, filename, output):

        binary_list = bitarray()

        for idx, o in enumerate(output):

            size = Util().calculateBinaryRequired(idx)

            node_id = o[0]
            node_edge = o[1]

            node_id_bin_format = '{:0' + str(size) + 'b}'
            node_id_bin = node_id_bin_format.format(node_id)

            binary_list.extend(node_id_bin)
            binary_list.extend(Util().fillZeroCharacter(node_edge))

        with open(filename, 'wb') as fh:
            binary_list.tofile(fh)


    def read_binary(self, input_file):

        binary_list = bitarray()

        with open(input_file, 'rb') as fh:
            binary_list.fromfile(fh)

        start = 0
        end = 1
        size = 1
        idx = 0

        decode_output_list = []

        binary_list_item_count = len(binary_list)

        tmp = []

        while True:

            if start >= binary_list_item_count:
                break

            size = Util().calculateBinaryRequired((idx + 1))

            node_id = binary_list[start:end]
            node_edge = binary_list[end:(end + 7)]

            start = (end + 7)
            end = start + size

            tmp.append([node_id, node_edge])

            try:
                o1 = int(node_id.to01(), 2)
                o2 = chr(int(node_edge.to01(), 2))

                a = (o1, o2)
                decode_output_list.append(a)

            except ValueError as e:
                break

            idx += 1

        return decode_output_list
