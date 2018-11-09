
from node import Node

class LZ78:

    rootNode = None
    output = None
    dev = True

    def __init__(self):
        self.output = list()
        self.rootNode = Node(id=0, is_root=True)

    def encrypt(self, input_file):

        node_id = 1
        character_string = ""

        with open(input_file) as ins:
            for line in ins:
                for character in line:

                    is_found = self.rootNode.searchChild(character_string + character)

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

        output = self.output

        rootNode = Node(id=0, is_root=True)

        # for o in output:


    def log(self):
        if self.dev:
            print(self.output)

input_file = "infile.txt"

lz = LZ78()
lz.encrypt(input_file)
lz.decrypt(input_file)
lz.log()

