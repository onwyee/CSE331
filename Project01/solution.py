"""
Project 1
CSE 331 SS25
Authors of DLL: Andrew McDonald, Alex Woodring, Andrew Haas, Matt Kight, Lukas Richters, 
                Anna De Biasi, Tanawan Premsri, Hank Murdock, & Sai Ramesh
Authors of Application: Divya Sudha & Leo Specht
solution.py
"""

from __future__ import annotations
from typing import List, TypeVar, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        return self.size == 0

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        newNode = Node(val)

        if self.size == 0:
            self.head = self.tail = newNode
        elif back:
            # tail --> new
            self.tail.next = newNode
            # tail <-- new
            newNode.prev = self.tail
            # tail = new
            self.tail = newNode
        elif not back:
            # new <-- head
            self.head.prev = newNode
            # new --> head
            newNode.next = self.head
            # head = new
            self.head = newNode
        self.size += 1
        return
    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.size == 0:
            return
        if self.size == 1:
            self.head = self.tail = None
        elif back:
            # saves node that will be new tail
            newTail = self.tail.prev
            # newtail points to none
            newTail.next = None
            self.tail = newTail

        elif not back:
            # saves node that will be new head
            newHead = self.head.next
            # newhead points to none
            newHead.prev = None
            self.head = newHead
        self.size -= 1
        return
    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = self.tail = None
        self.size = 0
        for value in source:
            self.push(value, True)
        return

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        currNode = self.head
        dllList = []
        while currNode is not None:
            dllList.append(currNode.value)
            currNode = currNode.next
        return dllList

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        currNode = self.head
        matches = []
        # iterates through DLL
        while currNode is not None:
            if currNode.value == val:
                matches.append(currNode)
                # breaks if we only need one
                if find_first:
                    return matches
            currNode = currNode.next
        return matches
    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object..

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return an empty list.
        """
        lis = self._find_nodes(val)
        # if none found
        if len(lis) == 0:
            return None
        return lis[0]

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        return self._find_nodes(val, False)


    def remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if self.head is None:
            return
        if self.size == 1:
            self.head = self.tail = None
        else:
            # if we have to remove head
            if to_remove == self.head:
                # severs connection to the removed
                to_remove.next.prev = None
                # sets new head
                self.head = to_remove.next
            # if we have to remove tail
            elif to_remove == self.tail:
                # severs connection to old tail
                to_remove.prev.next = None
                # sets new tail
                self.tail = to_remove.prev
            else:
                # post-removed node points to pre-removed and vice versa
                to_remove.next.prev, to_remove.prev.next = to_remove.prev, to_remove.next
        self.size -= 1
        return

    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        val = self.find(val)
        if val is not None:
            self.remove_node(val)
            return True
        return False

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        vals = self.find_all(val)
        for item in vals:
            self.remove_node(item)
        return len(vals)

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        # reversal doesn't change order
        if self.size < 2:
            return None
        # take second to last node
        currNode = self.tail.prev
        # change pointer, old tail will be new head
        self.tail.prev = None
        # next node after currNode is moved
        nextNode = currNode.prev
        # old tail will be new head
        self.head = self.tail

        while currNode is not None:
            # adds node to other side of tail
            self.tail.next = currNode
            currNode.prev = self.tail
            # updates new tail
            self.tail = currNode
            # step through DLL, nextNode only if we are not at last node to move
            currNode = nextNode
            if nextNode:
                nextNode = nextNode.prev
        self.tail.next = None
        return


class Spotify_Music_Player:
    def __init__(self, paid: bool=False) -> None:
        """
        Initializes the Spotify_Music_Player class

        :param paid: Account type for Spotify
        :return: None
        """
        self.songlist = DLL()
        self.playing = self.songlist.head
        self.paid = paid

    def play_favorite_next(self, favorite_song, forward=True) -> None:
        """
        Changes the song order so that the favorite sone is played after the current one

        :param favorite_song: Song to be played next
        :param forward: This tells you where to remove the favorite song node from, in order to move it after the currently playing song, if already in the song list. If True, remove latest node in the tree that contains the favorite song. If False, remove the first occurence of favorite song and move it to be after the playing node.
        :return: None
        """
        # favorite is only song
        if self.songlist.empty():
            self.songlist.push(favorite_song)
            self.playing = self.songlist.head
            return

        # finds favorite songs
        nodes = self.songlist.find_all(favorite_song)
        currNode = self.playing

        if nodes:
            # if forward, we will need last of found favorites
            # else, we will need the first of found favorites
            # tests only can have 2 favs, one before one after
            ind = -1 if forward else 0
            fav = nodes[ind]
            # severs connections
            self.songlist.remove_node(fav)
        else:
            # favorite song isnt in cue, so we add instance as node
            fav = Node(favorite_song)

        # using push updates tail easier
        if currNode is self.songlist.tail:
            self.songlist.push(favorite_song)
        else:
            # establishes connections from fav to new surrounding nodes
            fav.next = currNode.next
            fav.prev = currNode
            # establishes connections from surrounding nodes to fav
            currNode.next = fav
            fav.next.prev = fav
        return





    def add_ads(self, advertisement: str, favorite: str) ->None:
        """
        Inserts ads for non-premium Spotify accounts

        :param advertisement: Value of ad to be inserted.
        :param favorite: User's favorite song so ad can be inserted after it.
        """
        if not self.paid:
            currNode = self.songlist.head
            noAd = False
            # edge case if head of list is favorite
            if currNode.value == favorite:
                newAd = Node(advertisement)
                newAd.next = currNode
                currNode.prev = newAd
                self.songlist.head = newAd
                # toggles, no ad after this song
                noAd = True
            while currNode.next:
                # match and no ad before previous song
                if currNode.next.value == favorite and not noAd:
                    newAd = Node(advertisement)
                    # establishes new connections to added ad
                    currNode.next.prev = newAd
                    newAd.next = currNode.next
                    currNode.next = newAd
                    newAd.prev = currNode
                    # ensures no ad will be placed after this song
                    noAd = True
                    currNode = currNode.next
                else:
                    noAd = False

                currNode = currNode.next



