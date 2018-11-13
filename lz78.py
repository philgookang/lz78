from node import *
from fileio import *
import time

class LZ78:

    dic = None
    rootNode = None
    output = None
    dev = False

    def __init__(self):
        self.output = list()
        self.dic = dict()
        self.rootNode = Node(id=0, is_root=True)

    def encrypt(self, input_file):

        node_id = 1
        character_string = ""

        io = Fileio()
        text_list = io.read_text(input_file)
        # text_list = ["aaabbabaabaaabab"]

        # start encoding time
        start_time = time.time()

        # go through line by line in text
        for line in text_list:
            for character in line:

                is_found = self.rootNode.searchChildByEdge(character_string + character)

                if not is_found:
                    if self.dev:
                        print((node_id, character_string + character))

                    # create child node to add
                    new_child_to_add = Node(id=node_id, edge=character)

                    # add new child to trie
                    # get update child with parent_id
                    new_child_to_add = self.rootNode.addChild(new_child_to_add, character_string)

                    # save output
                    self.output.append((new_child_to_add.parent_id, new_child_to_add.edge))

                    character_string = ""
                    node_id += 1
                else:
                    character_string += character

        # start encoding time
        end_time = time.time()

        print('encoding time: ', (end_time - start_time))


    def decrypt(self, output_file):

        # create out variable
        output = self.output

        # original final string
        original_string = ""

        # 0 index just make it blank!
        self.dic[0] = ""

        # start encoding time
        start_time = time.time()

        # loop through output list
        for idx,o in enumerate(output):

            # create current search key
            key = (idx + 1)

            # parent id
            parent_id = o[0]

            # edge
            edge = o[1]

            # check if parent_id is in dictionary
            if parent_id in self.dic:
                edge = self.dic[parent_id] +  edge

            # add to string makeup
            original_string += edge

            # need to add to dictionary
            self.dic[key] = edge


        if self.dev:
            print(original_string)

        io = Fileio()
        io.save_text(output_file, original_string)

        # start encoding time
        end_time = time.time()

        print('encoding time: ', (end_time - start_time))

    def save(self, output_filename):
        io = Fileio()
        io.save_binary(output_filename, self.output)

    def open(self, input_file):
        io = Fileio()
        self.output = io.read_binary(input_file)

    def log(self):
        if self.dev:
            print(self.output)

