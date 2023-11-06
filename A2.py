class Node:
    """A Huffman Tree Node"""

    def __init__(self, freq_, symbol_, left_=None, right_=None):
        # frequency of symbol
        self.freq = freq_

        # symbol name (character)
        self.symbol = symbol_

        # node left of current node
        self.left = left_

        # node right of current node
        self.right = right_

        # tree direction (0/1)
        self.huff = ""


def print_nodes(node, val=""):
    """Utility function to print Huffman codes for all symbols in the newly created Huffman tree"""
    # Huffman code for the current node
    new_val = val + str(node.huff)

    # If the node is not an edge node, then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # If the node is an edge node, then display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Take user input for characters and their frequencies
chars = []
freq = []
num_chars = int(input("Enter the number of characters: "))

for i in range(num_chars):
    char = input(f"Enter character {i + 1}: ")
    frequency = int(input(f"Enter frequency for character {char}: "))
    chars.append(char)
    freq.append(frequency)

# Create Huffman tree nodes from user input
nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
    # Sort all the nodes in ascending order based on their frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # Pick the 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # Assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # Combine the 2 smallest nodes to create a new node as their parent
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # Remove the 2 nodes and add their parent as a new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print("Characters:", chars)
print("Frequency:", freq, "\nHuffman Encoding:")
print_nodes(nodes[0])
