
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


    def addChild(self, new_child):

        # added new child to parent
        self.child_node_list[new_child.id] = new_child

        # return child for logging
        return new_child


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


    def searchChildByParentId(self, parent_id):

        # exception handler for when looking for 0 parent id
        if not parent_id:
            return self

        # loop through all child to see if their value equals search
        if parent_id in self.child_node_list:
            return self.child_node_list[parent_id]

        # not found then go one depth more
        else:

            # loop through child to see if they have the node
            for k in self.child_node_list:

                # check if parent id is larger then child
                if k <= parent_id:

                    # get node child
                    child = self.child_node_list[k]

                    # check child subsearch
                    return_from_recursive_search = child.searchChildByParentId(parent_id)

                    # if child found, return or else, go loop next interation
                    if return_from_recursive_search:
                        # node found, lets return it!
                        return return_from_recursive_search
        # not found!
        return False