from linked_list import LinkedList

def merge_sort(linked_list):
    """
    sorts a linked list in ascending order
    - Recursevely divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list == None or linked_list == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes 
    Returns a new, merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right
    merged =LinkedList()

    # Add a fake head that is discarde later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    #Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either

    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node