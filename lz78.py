from node import *
from fileio import *

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


    def decrypt(self, output_file):

        # create out variable
        output = self.output

        # original final string
        original_string = ""

        # loop through output list
        for idx,o in enumerate(output):

            # create current search key
            key = (idx + 1)

            # empty node
            search_result = None

            # edge character
            edge = o[1]

            # edge id
            node_id = o[0]

            # get node
            if edge in self.dic:

                # set current node
                edge_list = self.dic[edge]

                for node in edge_list:
                    if node.id == node_id:
                        search_result = node
                        break

            # check if node was not found in dictionary
            if search_result == None:

                # add list in hash location
                self.dic[edge] = list()

                # check for node in TRIE that has this parent id
                search_result = self.rootNode.searchChildByParentId(o[0])



            # create child node to add
            new_child_to_add = Node(parent_id=o[0], parent_node=search_result, id=key, edge=o[1])

            # set node to current hash index
            self.dic[edge].append(new_child_to_add)

            # add child to parent node
            search_result.child_node_list.append(new_child_to_add)


            # return child because edge data start's with child node
            search_result = new_child_to_add




            # temp save current node to root path
            statement = ""

            # loop through all the edges
            while search_result.edge:

                # save edge value
                statement = search_result.edge + statement

                # change next node
                search_result = search_result.parent_node

            # add temp statement to final string list
            original_string = original_string + statement

            if self.dev:
                print(statement)


        if self.dev:
            print(original_string)

        io = Fileio()
        io.save_text(output_file, original_string)

    def save(self, output_filename):
        io = Fileio()
        io.save_binary(output_filename, self.output)

    def open(self, input_file):
        io = Fileio()
        self.output = io.read_binary(input_file)

    def log(self):
        if self.dev:
            print(self.output)

