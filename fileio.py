import math

from util import *

class Fileio:

    def read_text(self, input_file):
        return_list = list()
        with open(input_file) as ins:
            for line in ins:
                return_list.append(line)
        return return_list


    def read_binary(self, input_file):

        file = open(input_file, 'rb')
        encoded = file.read()

        tmp_output_list = list()

        x_size = 0  # number of consecutive bytes which need to be combined
        write_b = None  # buffer for temporal bytes

        node_id = ""
        node_edge = ""

        for byte in encoded:

            # x_size == 0 means that previous data successfully decoded and added to result list 'st'
            # decode next binary data
            if x_size == 0:
                # check 2 MSBs to know how many bytes comprises a codeword
                header = byte & 192
                header = header >> 6

                # reset number bits for precise calculations
                if byte >= 128:
                    byte -= 128
                if byte >= 64:
                    byte -= 64

                # convert int to bytes for concatenation with consecutive bytes
                write_b = byte.to_bytes(1,'big')

                # number of bytes of a codeword
                x_size = header + 1

            else:
                # concatenate consecutive byte
                write_b += byte.to_bytes(1,'big')

            x_size -= 1

            # if x_size = 0, add write_b to st list
            if x_size == 0:

                if node_id == "":
                    node_id = int.from_bytes(write_b,'big')
                elif node_edge == "":
                    node_edge = chr(int.from_bytes(write_b, 'big'))

                    c = (node_id, node_edge)
                    tmp_output_list.append(c)

                    node_id = ""
                    node_edge = ""

                # convert bytes to int and add the result list
                # tmp_output_list.append(int.from_bytes(write_b,'big'))
                write_b = None # initialize buffer

        return tmp_output_list


    def save_text(self, filename, string_to_save):
        file = open(filename, 'w')
        file.write(string_to_save)
        file.close()


    def save_binary(self, filename, output):

        file = open(filename, "wb")

        for tuple_item in output:

            node_id = tuple_item[0]
            node_edge = ord(tuple_item[1])

            # encode integer as bytes. Big Endian
            node_id_bytes = Util().encode(node_id)
            node_edge_bytes = Util().encode(node_edge)

            # save big endian string encoded
            file.write(node_id_bytes)

            # save big endian string encoded
            file.write(node_edge_bytes)

        # close file
        file.close()