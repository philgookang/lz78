
class Node:

    # node #
    id = None

    # parent node #
    parent_id = None

    # parent node pointer
    parent_node = None

    # edge value
    edge = None

    # is root
    is_root = None

    # child node list
    child_node_list = None


    def __init__(self, parent_id = None, parent_node = None, id = None, edge = None, is_root = False):
        self.id = id
        self.parent_id = parent_id
        self.parent_node = parent_node
        self.edge = edge
        self.is_root = is_root
        self.child_node_list = dict()


    def searchChildByEdge(self, character):

        # check if edge exsits
        for child in self.child_node_list:

            # get child
            child = self.child_node_list[child]

            # check if child edge is equal to search character
            if child.edge == character:
                return child

        # not found!
        return False


    def addChild(self, new_child):

        # added new child to parent
        self.child_node_list[new_child.id] = new_child

        # return child for logging
        return new_child
