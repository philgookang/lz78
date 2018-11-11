import math


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
        number_byte = list()

        node_id = ""
        edge = ""
        ascii_number = ""

        for byte in encoded:

            # add to decode list
            number_byte.append(byte)

            try:
                ascii_number = int.from_bytes(number_byte, 'big')

            except TypeError as err:
                print("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
                pass

            if ascii_number != "":

                if node_id == "":
                    node_id = ascii_number
                else:
                    edge = chr(ascii_number)
                    c = ( node_id,  edge)
                    tmp_output_list.append(c)

                    node_id = ""
                    edge = ""

                ascii_number = ""
                number_byte.clear()

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

            # node_id_byte_size = (node_id.bit_length() + len(str(node_id))) // 8
            # node_edge_byte_size = (node_edge.bit_length() + len(tuple_item[1])) // 8

            node_id_byte_size = math.ceil((node_id.bit_length() + len(str(node_id))) / 8)
            node_edge_byte_size = math.ceil((node_edge.bit_length() + len(tuple_item[1])) / 8)

            # encode integer as bytes. Big Endian
            node_id_bytes = node_id.to_bytes(node_id_byte_size, 'big')
            node_edge_bytes = node_edge.to_bytes(node_edge_byte_size, 'big')


            # save big endian string encoded
            file.write(node_id_bytes)

            # save big endian string encoded
            file.write(node_edge_bytes)

        # close file
        file.close()