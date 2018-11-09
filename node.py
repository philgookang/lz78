
class Node:

    # node #
    id = None

    # parent node #
    parent_id = None

    # edge value
    edge = None

    # is root
    is_root = None

    # child node list
    child_node_list = None


    def __init__(self, parent_id = None, id = None, edge = None, is_root = False):
        self.id = id
        self.parent_id = parent_id
        self.edge = edge
        self.is_root = is_root
        self.child_node_list = list()


    def searchChild(self, character_string):

        # length of the search character string
        len_of_char_str = len(character_string)

        # always check first character of search string
        # because this is a recursive loop
        # empty string exception will be handled on call
        character = character_string[0]

        # loop through all child to see if their value equals search
        for child in self.child_node_list:

            # check if child edge is equal to search character
            if child.edge == character:

                # found last child in the search
                if len_of_char_str == 1:
                    return child

                # found child but still more to search
                else:
                    return child.searchChild(character_string[1:])

        # not found!
        return False


    def addChild(self, new_child, character_string):

        # length of the search character string
        len_of_char_str = len(character_string)

        # search string is zero 0
        if not len_of_char_str:

            # set root id
            new_child.parent_id = self.id

            # add child root child list
            self.child_node_list.append(new_child)
        else:
            # get last child
            last_child = self.searchChild(character_string)

            # set new child parent id
            new_child.parent_id = last_child.id

            # added new child to parent
            last_child.child_node_list.append(new_child)

        # return child for logging
        return new_child