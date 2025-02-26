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
    