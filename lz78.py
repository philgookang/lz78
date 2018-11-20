from node import *
from fileio import *
import time

class LZ78:

    dic         = None
    rootNode    = None
    output      = None


    def __init__(self):
        self.output = list()
        self.dic = list()
        self.rootNode = Node(id=0, is_root=True)


    def encrypt(self, input_file):

        io = Fileio()
        text_list = io.read_text(input_file)
        # text_list = ["aaabbabaabaaabab"]

        # set search start node to root as default
        search_start_node = self.rootNode

        # default start node id is 1
        node_id = 1

        # set cummulative string variable
        character_string = ""

        # start encoding time
        start_time = time.time()

        # is_found child pointer leave outside for last ending insert
        is_found = None

        # go through line by line in text
        for line in text_list:

            for character in line:

                # check in dic if n
                is_found = search_start_node.searchChildByEdge(character)

                if not is_found:

                    # create child node to add
                    new_child_to_add = Node(parent_id=search_start_node.id, parent_node=search_start_node, id=node_id, edge=character)

                    # add new child to trie
                    # get update child with parent_id
                    new_child_to_add = search_start_node.addChild(new_child_to_add)

                    # save output
                    self.output.append((new_child_to_add.parent_id, new_child_to_add.edge))

                    character_string = ""               # reset search character string
                    node_id += 1                        # set next node id
                    search_start_node = self.rootNode   # reset start node to the top root
                else:
                    # set next search start node
                    search_start_node = is_found

                    # cummulative character string
                    character_string += character

        # check if loop finished preemptly
        if character_string != "":
            self.output.append((is_found.parent_id, is_found.edge))

        # start encoding time
        end_time = time.time()

        print('encoding time: ', (end_time - start_time))


    def decrypt(self, recover_file):

        # set fixed size for dictionary
        self.dic = [None] * (len(self.output) + 1)

        # create out variable
        output = self.output

        # original final string
        original_string = ""

        # 0 index just make it blank!
        self.dic[0] = ""

        # start encoding time
        start_time = time.time()

        # loop through output list
        for idx, o in enumerate(output):

            try:

                # create current search key
                key = (idx + 1)

                # parent id
                parent_id = o[0]

                # edge
                edge = o[1]

                # check if parent_id is in dictionary
                if self.dic[parent_id] != None:
                    edge = self.dic[parent_id] + edge

                # add to string makeup
                original_string += edge

                # need to add to dictionary
                self.dic[key] = edge

            except IndexError as e:
                pass

        io = Fileio()
        io.save_text(recover_file, original_string)

        # start encoding time
        end_time = time.time()

        print('decoding time: ', (end_time - start_time))


    def save(self, output_filename):
        io = Fileio()
        io.save_binary(output_filename, self.output)


    def open(self, input_file):
        io = Fileio()
        self.output = io.read_binary(input_file)