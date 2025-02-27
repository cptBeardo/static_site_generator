from htmlnode import HTMLNode, LeafNode, ParentNode

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

node5 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold Text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
print(node5.to_html())  # Circle back to this

# DEBUGGING: leaf = LeafNode("b", "Bold Text")
# DEBUGGING: print(leaf.to_html())  # Should print: <b>Bold Text</b>