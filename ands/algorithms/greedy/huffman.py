#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

### Warning

There are still some functions that I need to implement,
but the basic idea of the huffman algorithm is here,
so I decided to include it already in this repository.

### Description

Huffman coding to encode messages with a variable length of bits.

The tree created by the huffman algorithm is not a binary search tree,
but simply a binary tree, that is the left child is not necessarily smaller
than the node i, or the right child is not necessarily greater than the node i,
for all nodes i in the tree.

The tree produce by the huffman algorithm is a full tree:
if C is the alphabet from which the characters are drawn and
all characters frequencies are positive,
then the tree for an optimal prefix code as exactly |C| leaves,
one for each character in C, and exactly |C| - 1 internal nodes,
and by the way we need |C| - 1 merges to construct the tree.

Note that the codewords produced by the build_huffman_codes
contain distinct prefixes among each other,
and this is very useful when decoding the huffman codes,
because there's no ambiguity.

Given a tree T corresponding to a prefix code,
we can easily compute the number of bits necessary to encode a message,
given a certain alphabet C:
For each character c in the alphabet C,
let c.freq be the frequency of c in the message to encode,
and let d(c) denote the depth of the leaf c in the tree
(note that d(c) is also the length of the codeword to encode c),
the number of bits to encode the message is therefore:

bits(T):= sum {for all c in C} of c.freq * d(c).


### TODO
- Correctness of Huffman algorithm
"""

from ands.ds.HeapNode import HeapNode
from ands.ds.MinPriorityQueue import MinPriorityQueue


# export only functions and classes of this module that are implemented
__all__ = ["calculate_frequencies",
           "print_frequencies",
           "huffman",
           "build_huffman_codes",
           "huffman_fibonacci_encoder"]

def calculate_frequencies(message):
    frequencies = {}
    for char in message:
        if char not in frequencies.keys():
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies

def print_frequencies(frequencies):
    from tabulate import tabulate
    import operator
    print(tabulate(sorted(frequencies.items(), key=operator.itemgetter(1)), headers=("Letter", "Frequency"), tablefmt="grid"))

def huffman(message: str, verbose=False):
    """Creates a Huffman tree representing all the codewords for message.

    **Time Complexity**: O(n*log<sub>2</sub>(n))."""

    # Counting the frequencies of each character or symbol
    frequencies = calculate_frequencies(message)

    if verbose:
        print_frequencies(frequencies)

    # Creates a queue in O(n) time using the build-min-heap algorithm.
    mpq = MinPriorityQueue(frequencies.items())

    while not mpq.is_empty():

        left = mpq.extract_min(heap_node=True)
        right = mpq.extract_min(heap_node=True)

        if right is None:
            return left
        
        node = HeapNode(key=left.key + right.key, value=left.value + right.value)

        node.left = left
        node.right = right
        
        left.parent = node
        right.parent = node

        mpq.insert_with_priority(node)

def build_huffman_codes(root: HeapNode):
    """Starting from the `root` node obtained by the `huffman` algorithm,
    this function builds a dictionary where keys are the original characters,
    and their values are the corresponding huffman codes."""
    huffman_codes = {}

    for char in root.value:
        current_node = root
        huffman_code = ""  # huffman code of char
    
        while True:
            if current_node.left is not None and \
               char in current_node.left.value:
                huffman_code += "0"
                current_node = current_node.left
            elif current_node.right is not None:
                huffman_code += "1"
                current_node = current_node.right
            else:
                break
            
        huffman_codes[char] = huffman_code
        
    return huffman_codes


# TODO: CREATE AN ENCODE AND DECODE FUNCTIONS

def huffman_encoder(huffman_codes):
    pass

def huffman_decoder(encoded_message):
    pass

def huffman_fibonacci_encoder(fn: "list of list"):
    """`fn` is supposed to be a `list` of `tuple`s,
    whose first element is the character or symbol,
    whereas the second element is its corresponding frequency,
    that happen to be the Fibonacci numbers."""
    import operator

    fn.sort(key=operator.itemgetter(1), reverse=True)  # sorts by frequency
    huffman_codes = {fn[-1][0]: "0"*(len(fn) - 1)}

    for i, char in enumerate(fn[:-1]):
        prefix = "0" * i
        codeword = prefix + "1"
        huffman_codes[char[0]] = codeword
    return huffman_codes

hfc = huffman_fibonacci_encoder([("a", 1), ("b", 1), ("c", 2), ("d", 3),
                                ("e", 5), ("f", 8), ("g", 13), ("h", 21)])

def huffman_fibonacci_decoder(encoded_message):
    # TODO: Huffman decoder for Fibonacci numbers
    pass


if __name__ == "__main__":
    root1 = huffman("Cyka Blyat")
    root2 = huffman("Shook Ones")
    print(build_huffman_codes(root1))
    print(build_huffman_codes(root2))
