from htmlnode import *
from textnode import *
from splitnode import *
from main import *

# Sanity Check 1: Default attributes
# DEBUGGING: node1 = HTMLNode()  # Everything should default
# DEBUGGING: print(node1)

# Sanity Check 2: With attributes
# DEBUGGING: node2 = HTMLNode(tag="div", value="Hello", children=[HTMLNode(tag="span")], props={"class": "test"})
# DEBUGGING: print(node2)
# DEBUGGING: print(node2.props_to_html())

# Sanity Check 3: Just props
# DEBUGGING: node3 = HTMLNode(props={"id": "unique"})
# DEBUGGING: print(node3.props_to_html())

# Sanity Check 4: no children left in LeafNode
# DEBUGGING: node4 = LeafNode(tag="span", value="example text")
# DEBUGGING: print(node4)

# DEBUGGING:node5 = ParentNode(
# DEBUGGING:    "p",
# DEBUGGING:    [
# DEBUGGING:        LeafNode("b", "Bold Text"),
# DEBUGGING:        LeafNode(None, "Normal text"),
# DEBUGGING:        LeafNode("i", "italic text"),
# DEBUGGING:        LeafNode(None, "Normal text"),
# DEBUGGING:    ],
# DEBUGGING:)
# DEBUGGING:print(node5.to_html())  # Circle back to this

# DEBUGGING: leaf = LeafNode("b", "Bold Text")
# DEBUGGING: print(leaf.to_html())  # Should print: <b>Bold Text</b>

# DEBUGGING: node6 = split_nodes_delimiter(["This is **bold** text"], "**", TextType.TEXT)
# DEBUGGING: print(split_nodes_delimiter.new_nodes)

# Create a sample old_nodes list
old_nodes = [
    TextNode("This is text with a **bold word** in it", TextType.TEXT),
    TextNode("This is already bold", TextType.BOLD)
]

# Print out the old_nodes to see their structure
print("Old Nodes:")
for node in old_nodes:
    print(f"Text: '{node.text}', Type: {node.text_type}")

# Let's imagine how split_nodes_delimiter would work with "**" delimiter
print("\nIf we split with '**' delimiter for BOLD type, we would get:")
print("1. TextNode('This is text with a ', TEXT)")
print("2. TextNode('bold word', BOLD)")
print("3. TextNode(' in it', TEXT)")
print("4. TextNode('This is already bold', BOLD) - unchanged because it's not TEXT type")