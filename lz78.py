
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

        # with open(input_file) as ins:
        #     for line in ins:
        line = "aaabbabaabaaabab"
        #       aaabbabaabaaabab
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

            # check for node in TRIE that has this parent id
            search_result = self.rootNode.addChildByParentId((idx + 1), o)

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


    def log(self):
        if self.dev:
            print(self.output)

input_file = "infile.txt"

enc_lz = LZ78()
dec_lz = LZ78()

enc_lz.encrypt(input_file)

dec_lz.output = enc_lz.output
dec_lz.decrypt(input_file)
# lz.log()

