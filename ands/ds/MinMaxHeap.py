#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Creation: 18/02/16

Last update: 19/02/16

Min-Max Heap is a heap that supports find-min and find-max operations in constant time.
Moreover, both remove-min and remove-max are supported in logarithmic time.
It's therefore an useful data structure to implement (or represent) double-ended priority queues.

## References:

- [Min-Max Heaps and Generalized Priority Queues](http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f03/Artikler/02../Atkinson86.pdf)

- [brownhead/minmaxheap-cpp](https://github.com/brownhead/minmaxheap-cpp/blob/master/MinMaxHeap.hpp)

- [gnarmis/minmaxheap.py](https://gist.github.com/gnarmis/4647645)

- [http://www.diku.dk/forskning/performance-engineering/Jesper/heaplab/heapsurvey_html/node11.html](http://www.diku.dk/forskning/performance-engineering/Jesper/heaplab/heapsurvey_html/node11.html)

- [http://www.math.clemson.edu/~warner/M865/HeapDelete.html](http://www.math.clemson.edu/~warner/M865/HeapDelete.html)
"""

from ands.ds.Heap import Heap
from ands.ds.HeapNode import HeapNode


class MinMaxHeap(Heap):

    def __init__(self, ls=[]):
        Heap.__init__(self, ls)

    def push_down(self, i: int) -> None:
        if self.is_on_even_level(i):
            self.push_down_min(i)
        else:
            self.push_down_max(i)
            
    def push_down_min(self, i: int) -> None:
        """Helper method for `push_down`."""
        if self.has_children(i):            
            m = self.index_of_min(i)
            
            if self.is_grandchild(m, i):
                if self.heap[m] < self.heap[i]:
                    self.swap(i, m)
                    
                    mp = self.parent_index(m)
                    if mp != -1 and self.heap[m] > self.heap[mp]:
                        self.swap(m, mp)
                    self.push_down_min(m)
                    
            else:  # self.heap[m] is a child of self.heap[i]
                if self.heap[m] < self.heap[i]:
                    self.swap(i, m)

    def push_down_max(self, i: int) -> None:
        """Helper method for `push_down`."""        
        if self.has_children(i):
            m = self.index_of_max(i)

            if self.is_grandchild(m, i):        
                if self.heap[m] > self.heap[i]:
                    self.swap(i, m)

                    mp = self.parent_index(m)
                    if mp != -1 and self.heap[m] < self.heap[mp]:
                        self.swap(m, mp)
                    self.push_down_max(m)
                    
            else:  # self.heap[m] is a child of self.heap[i]
                if self.heap[m] > self.heap[i]:
                    self.swap(i, m)

    def push_up(self, i: int) -> None:
        if self.is_on_even_level(i):
            p = self.parent_index(i)
            if p != -1 and self.heap[i] > self.heap[p]:
                self.swap(i, p)
                self.push_up_max(p)
            else:
                 self.push_up_min(i)
        else:
            p = self.parent_index(i)            
            if p != -1 and self.heap[i] < self.heap[p]:
                self.swap(i, p)
                self.push_up_min(p)
            else:
                self.push_up_max(i)

    def push_up_min(self, i: int) -> None:
        """Helper method for `push_up`."""        
        g = self.grandparent_index(i)
        if g != -1:
            if self.heap[i] < self.heap[g]:
                self.swap(i, g)
                self.push_up_min(g)

    def push_up_max(self, i: int) -> None:
        """Helper method for `push_up`."""        
        g = self.grandparent_index(i)
        if g != -1:
            if self.heap[i] > self.heap[g]:
                self.swap(i, g)
                self.push_up_max(g)
                
    def find_max(self) -> HeapNode:
        """Returns the `HeapNode` object representing the maximum element."""
        if not self.is_empty():
            return self.heap[self.find_max_index()]

    def find_min(self) -> HeapNode:
        """Returns the `HeapNode` object representing the minimum element."""
        if not self.is_empty():
            return self.heap[0]
        
    def remove_max(self) -> HeapNode:
        """Deletes and returns the `HeapNode` object representing the maximum element."""        
        if not self.is_empty():
            return self.delete(self.find_max_index())

    def remove_min(self) -> HeapNode:
        """Deletes and returns the `HeapNode` object representing the minimum element."""        
        if not self.is_empty():
            return self.delete(0)

    def find_max_index(self) -> int:
        """Returns the index of the maximum element in this min-max heap."""
        if self.is_empty():
            return -1
        elif self.size() == 1:
            return 0
        elif self.size() == 2:
            return 1
        else:
            return 1 if self.heap[1] > self.heap[2] else 2
            
    def index_of_min(self, i: int) -> int:
        """Returns the index of the smallest element
        among the children and grandchildren of the node at index `i`."""        
        m = l = self.left_index(i)
        r = self.right_index(i)

        if r != -1 and self.heap[r] < self.heap[m]:
            m = r

        if l != -1:
            gll = self.left_index(l)
            if gll != -1 and self.heap[gll] < self.heap[m]:
                m = gll
            glr = self.right_index(l)
            if glr != -1 and self.heap[glr] < self.heap[m]:
                m = glr
            
        if r != -1:
            grl = self.left_index(r)
            if grl != -1 and self.heap[grl] < self.heap[m]:
                m = grl
            grr = self.right_index(r)
            if grr != -1 and self.heap[grr] < self.heap[m]:
                m = grr

        return m

    def index_of_max(self, i: int) -> int:
        """Returns the index of the largest element
        among the children and grandchildren of the node at index `i`."""
        m = l = self.left_index(i)
        r = self.right_index(i)

        if r != -1 and self.heap[r] > self.heap[m]:
            m = r

        if l != -1:
            gll = self.left_index(l)
            if gll != -1 and self.heap[gll] > self.heap[m]:
                m = gll
            glr = self.right_index(l)
            if glr != -1 and self.heap[glr] > self.heap[m]:
                m = glr
            
        if r != -1:
            grl = self.left_index(r)
            if grl != -1 and self.heap[grl] > self.heap[m]:
                m = grl
            grr = self.right_index(r)
            if grr != -1 and self.heap[grr] > self.heap[m]:
                m = grr

        return m


def is_min_max_heap(h):
    """Returns `True` if `h` is a valid `MinMaxHeap` object. `False` otherwise."""
    if not isinstance(h, MinMaxHeap):
        return False
    
    if h.heap:
        for item in h.heap:
            if not isinstance(item, HeapNode):
                return False
            
        if h.size() == 1:
            return True
        
        if h.size() == 2:
            return h.heap[1] > h.heap[0]
        
        if h.size() >= 3:
            if (h.heap[0] != min(h.heap) or
                (h.heap[1] != max(h.heap) and
                 h.heap[2] != max(h.heap))):
                return False
             
        for i, item in reversed(list(enumerate(h.heap))):
            p = h.parent_index(i)
            if p != -1:
                if h.is_on_even_level(i):
                    if h.heap[p] < item:
                        return False
                else:
                    if h.heap[p] > item:
                        return False
                
            g = h.grandparent_index(i)
            if g != -1:
                if h.is_on_even_level(i):
                    if h.heap[g] > item:
                        return False
                else:
                    if h.heap[g] < item:
                        return False
    return True        
