"""
Determining the network prefix

An IPv4 network mask consists of 32 bits,
a sequence of 1s followed by a block of 0s.
The trailing block of 0s designates that part
as being the host identifier.

The following example shows the separation
of the network prefix and the host identifier
from an address (192.168.5.130) and its associated
/24 network mask (255.255.255.0).
The operation is visualized in a table
using binary address formats.


                           Binary form                  Dot-decimal notation
IP address	11000000.10101000.00000101.10000010	192.168.5.130
Subnet mask	11111111.11111111.11111111.00000000	255.255.255.0
Network prefix	11000000.10101000.00000101.00000000	192.168.5.0
Host part	00000000.00000000.00000000.10000010	0.0.0.130

The mathematical operation for calculating the network prefix
is the bitwise AND of IP address and subnet mask.
The result of the operation yields the network prefix 192.168.5.0.
The host part 130 can be derived by using bitwise AND of IP address
and one's complement of the subnet mask.
"""


# Based on: http://stackoverflow.com/a/9475354/3924118
def split_every_n(s, n=8):
    return [s[i:i+n] for i in range(0, len(s), n)]

def dot_notation(b):
    blocks = split_every_n(b, 8)
    dn = []

    for block in blocks:
        dn.append(str(int(block, 2)))
        dn.append(".")

    return "".join(dn)


def reverse_bits(bits):
    s = list(bits)
    for i, bit in enumerate(s):
        if bit == '1':
            s[i] = '0'
        else:
            s[i] = '1'
    return "".join(s)

# Example
ip = int('11000000101010000000010110000010', 2)

subnet_str = '11111111111111111111111100000000'
subnet = int(subnet_str, 2)

# ip = int(input("Enter your 32-bit IPv4 address as a sequence of 0s and 1s: "), 2)
# subnet = int(input("Enter your 32-bit subnet mask as a sequence of 0s and 1s: "), 2)

network_prefix = bin(ip & subnet)[2:]
print("Your network prefix in binary is:", network_prefix)

dn = dot_notation(network_prefix)
print("...and in dot notation is:", dn)

subnet_ones_complement = int(reverse_bits(subnet_str), 2)
# print(subnet_ones_complement)

host = bin(ip & subnet_ones_complement)[2:]

print("Your host identifier in binary is:", host)

host_dn = dot_notation(host)
print("...and in dot notation is:", host_dn)

