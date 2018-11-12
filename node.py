
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
        # self.child_node_list = list()
        self.child_node_list = dict()


    def searchChildByEdge(self, character_string):

        # length of the search character string
        len_of_char_str = len(character_string)

        # always check first character of search string
        # because this is a recursive loop
        # empty string exception will be handled on call
        character = character_string[0]

        # check if edge exsits
        for child in self.child_node_list:

            # get child
            child = self.child_node_list[child]

            # check if child edge is equal to search character
            if child.edge == character:

                # found last child in the search
                if len_of_char_str == 1:
                    return child

                # found child but still more to search
                else:
                    return child.searchChildByEdge(character_string[1:])

        '''
        # loop through all child to see if their value equals search
        for child in self.child_node_list:

            # check if child edge is equal to search character
            if child.edge == character:

                # found last child in the search
                if len_of_char_str == 1:
                    return child

                # found child but still more to search
                else:
                    return child.searchChildByEdge(character_string[1:])
        '''

        # not found!
        return False


    def searchChildByParentId(self, parent_id):

        # exception handler for when looking for 0 parent id
        if not parent_id:
            return self

        # loop through all child to see if their value equals search
        if parent_id in self.child_node_list:
            return self.child_node_list[parent_id]
        else:
            for k in self.child_node_list:
                if k <= parent_id:
                    # get node child
                    child = self.child_node_list[k]

                    # check child subsearch
                    return_from_recursive_search = child.searchChildByParentId(parent_id)

                    # if child found, return or else, go loop next interation
                    if return_from_recursive_search:
                        return return_from_recursive_search

        '''
        for child in self.child_node_list:

            # check if child id is equal to search parent id
            if child.id == parent_id:
                return child

            # if child node is larger than parent id,
            # then dont need to do its children
            elif child.id > parent_id:
                pass

            # found child but still more to search
            else:
                # check child subsearch
                return_from_recursive_search = child.searchChildByParentId(parent_id)

                # if child found, return or else, go loop next interation
                if return_from_recursive_search:
                    return return_from_recursive_search
        '''

        # not found!
        return False


    def addChild(self, new_child, character_string):

        # set default last child as me!
        last_child = self

        # search when the string is not zero!
        if len(character_string):
            # get last child
            last_child = self.searchChildByEdge(character_string)

        # set new child parent id
        new_child.parent_id = last_child.id

        # set new child parent node pointer
        new_child.parent_node = last_child

        # added new child to parent
        # last_child.child_node_list.append(new_child)
        last_child.child_node_list[new_child.id] = new_child

        # return child for logging
        return new_child


    def addChildByParentId(self, idx, o):

        # check for node in TRIE that has this parent id
        search_result = self.searchChildByParentId(o[0])

        # create child node to add
        new_child_to_add = Node(parent_id=o[0], parent_node=search_result, id=idx, edge=o[1])

        # add child to parent node
        # search_result.child_node_list.append(new_child_to_add)
        search_result.child_node_list[new_child_to_add.id] = new_child_to_add

        # return child because edge data start's with child node
        return new_child_to_add