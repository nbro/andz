#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: July, 2015

Last update: 05/02/16

Contains an implementation of a min priority queue using a min heap.
"""

import sys
from ands.ds.MinHeap import MinHeap
from ands.ds.HeapNode import HeapNode


__all__ = ["MinPriorityQueue"]


class MinPriorityQueue(MinHeap):
    """Typical minimum priority queue,
    where smaller numbers for priorities represent higher priorities."""

    def __init__(self, ls=[]):
        """If ls is provided, it should be a list of tuples.
        Each of these tuples contains 2 items.
        The first item of the tuple is the element's name or value,
        the second item of the tuple is the priority of that same element.
        A smaller number means a higher priority.
        """
        MinHeap.__init__(self, ls)

    def insert_with_priority(self, element, priority=sys.maxsize):
        """Adds an element to this min priority queue.

        You can specify the priority of the element
        by assigning a value to "priority".

        Note that the value assigned to priority
        should be an object that overrides functions
        such as __lt__, __gt__, __le__, __ge__,
        __eq__, __ne__, in other words, it should be a comparable object.

        Note that all the priorities of all elements in self
        should be of the same type, in order to be able to compare them.

        If element is an HeapNode, the priority argument's value is ignored,
        and the priority of the element (HeapNode) is used.

        :type element : object
        :type priority : object"""
        if not isinstance(element, HeapNode):
            self.add(HeapNode(key=priority, value=element))
        else:
            self.add(element)

    def extract_min(self, priority=False, heap_node=False):
        """Removes and returns the element with highest priority to exit from the queue.

        Since this is a MinPriorityQueue,
        note that if A has an higher priority than B,
        then A.priority is less than B.priority,
        even if it could seem a little bit counter-intuitive.

        If priority is set to True, a tuple is returned;
        the first item of this tuple is the initial added element
        and the second item is the priority of the element,
        that is the tuple would be (element_with_highest_priority, priority).

        If heap_node is set to True,
        the HeapNode object representing the element is returned.
        You can also obtain the priority of this element through the HeapNode object,
        by getting its key field.

        If priority and heap_node are set both to False,
        only the element that was initial added (without the priority) is returned.

        If self is empty, None is returned.

        **Time Complexity**: O(log<sub>2</sub>(n)).

        :rtype : object"""
        min_heap_node = self.remove_min()
        if min_heap_node is not None:
            if priority:
                return min_heap_node.value, min_heap_node.key
            if not priority and not heap_node:
                return min_heap_node.value
            if heap_node:
                return min_heap_node

    def peek(self, priority=False):
        """Returns (without removing) the element with highest priority.

        Note that if A has an higher priority than B,
        then A.priority is less than B.priority,
        even if it is a little bit counter-intuitive.

        If priority is set to True,
        a tuple of the form (element, priority) is returned,
        otherwise only element is returned,
        where element is the element in self with highest priority.

        Time complexity: O(1)."""
        min_heap_node = self.find_min()
        if min_heap_node is not None:
            if priority:
                return min_heap_node.value, min_heap_node.key
            else:
                return min_heap_node.value

    def contains_element(self, element):
        if self.search_by_value(element) != -1:
            return True
        return False

    def change_priority(self, element, new_priority):
        """Changes priority of an element inside self.

        Note that if element is no more in self,
        an ValueError will be raised explaining it.

        Note that element should be of same type
        as element when inserting_with_priority
        and of the same type of the first item of each tuple
        in the initial list (when creating a MinPriorityQueue).

        Same thing can be said about new_priority.

        Time complexity: O(n), because of the call to search_by_value.

        :type element : object
        :type new_priority : object"""
        index_of_element = self.search_by_value(element)
        if index_of_element == -1:
            raise ValueError(str(element) + " not found.")
        self.replace(index_of_element, HeapNode(key=new_priority, value=element))

    
if __name__ == "__main__":
    mpq = MinPriorityQueue(ls=[("12", "1"), ("14", "1"), ("28", "2"), ("6", "2"),
                               ("18", "2"), ("7", "3"), ("10", "3")])
    mpq.show()
    mpq.insert_with_priority("2015", "2.0")
    mpq.show()
    a = mpq.extract_min()
    print("Removed element with highest priority:", a)
    print("Peeking...", mpq.peek())
    mpq.show()
    mpq.change_priority("18", "0")
    mpq.show()
