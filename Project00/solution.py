from typing import TypeVar  # For use in type hinting

# Type declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared Singly Linked List type
Node = TypeVar('Node')  # forward declared Node type


class SLLNode:
    """
    Node implementation
    Do not modify
    """

    __slots__ = ['data', 'next']

    def __init__(self, data: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param data: data value held by the node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method, casts SLL nodes to strings
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: True if the nodes are ==, else False
        """
        return self is other if other is not None else False


class SinglyLinkedList:
    """
    SLL implementation
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        :return: string representation of SLL
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right operand of `==`
        :return: True if equal, else False
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ========== Modify below ========== #

    def append(self, data: T) -> None:
        """
        Append an SLLNode to the end of the SLL
        :param data: data to append
        :return: None
        """
        newNode = SLLNode(data)
        # empty list
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        # end of nonempty list
        else:
            self.tail.next = newNode
            self.tail = newNode
        return

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of SLL
        """
        if self.head is None:
            return "None"
        currNode = self.head
        # initializes string with head
        SLLString = str(self.head.data)
        # iterate through nodes
        while currNode is not self.tail:
            # iterate step first because we have head already
            currNode = currNode.next
            SLLString += " --> " + str(currNode.data)
        return SLLString
    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        count = 0
        currNode = self.head
        # increments count on every step
        while currNode is not None:
            count += 1
            currNode = currNode.next
        return count

    def total(self) -> T:
        """
        Sums up the values in the list
        :return: total sum of values in the list
        """
        if self.head is None:
            return None
        sum = self.head.data
        currNode = self.head
        # add data to sum on each step through the SLL
        while currNode is not None:
            currNode = currNode.next
            if currNode is not None:
                sum += currNode.data
        return sum

    def delete(self, data: T) -> bool:
        """
        Deletes the first node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        # edge cases
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return True

        currNode = self.head
        prevNode = None
        while currNode is not None:
            # this is the one we want
            if currNode.data == data:
                # if head, we need to establish new head
                if currNode == self.head:
                    self.head = currNode.next
                    currNode.next = None
                # if head, we need to establish new tail
                elif currNode == self.tail:
                    prevNode.next = None
                    self.tail = prevNode
                # if somewhere in middle
                else:
                    # last node points to one after deleted
                    prevNode.next = currNode.next
                return True
            # step right one node
            prevNode = currNode
            currNode = currNode.next
        return False


    def delete_all(self, data: T) -> bool:
        """
        Deletes all instances of a node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False

        We were told to avoid using the previous delete function,
        this has a very similar structure
        """
        # edge cases
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return True
        currNode = self.head
        prevNode = None
        # to keep track of if any nodes were removed
        removedAny = False
        while currNode is not None:
            # the one we want
            if currNode.data == data:
                # same logic as delete
                if currNode == self.head:
                    self.head = currNode.next
                    currNode.next = None
                    currNode = self.head
                elif currNode == self.tail:
                    prevNode.next = None
                    self.tail = prevNode
                else:
                    prevNode.next = currNode.next
                    currNode.next = None
                    currNode = prevNode.next
                removedAny = True
            else:
                prevNode = currNode
                currNode = currNode.next
        return removedAny

    def find(self, data: T) -> bool:
        """
        Looks through the SLL for a node containing `data`
        :param data: data to search for
        :return: True if found, else False
        """
        currNode = self.head
        while currNode is not None:
            if currNode.data == data:
                return True
            currNode = currNode.next
        return False

    def find_sum(self, data: T) -> int:
        """
        Returns the number of occurrences of `data` in this list
        :param data: data to find and sum up
        :return: number of times the data occurred
        """
        count = 0
        currNode = self.head
        while currNode is not None:
            if currNode.data == data:
                count +=1
            currNode = currNode.next
        return count


def help_mario(roster: SLL, ally: str) -> bool:
    """
    Updates the roster of racers to put Mario's ally at the front
    Preserves relative order of racers around ally
    :param roster: initial order of racers
    :param ally: the racer that needs to go first
    :return: True if the roster was changed, else False
    """
    prevNode = None
    currNode = roster.head
    # edge cases
    if currNode is None or roster.head == roster.tail:
        return False
    # no need for change
    if roster.head.data == ally:
        return False
    while currNode is not None:
        if currNode.data == ally:
            # the old head will move to after the tail
            roster.tail.next = roster.head
            # prev node will be new tail
            prevNode.next = None
            roster.tail = prevNode
            # ally will be new head
            roster.head = currNode
            return True
        prevNode = currNode
        currNode = currNode.next
    return False