from htmlnode import HTMLNode, LeafNode

# Sanity Check 1: Default attributes
node1 = HTMLNode()  # Everything should default
print(node1)

# Sanity Check 2: With attributes
node2 = HTMLNode(tag="div", value="Hello", children=[HTMLNode(tag="span")], props={"class": "test"})
print(node2)
print(node2.props_to_html())

# Sanity Check 3: Just props
node3 = HTMLNode(props={"id": "unique"})
print(node3.props_to_html())

# Sanity Check 4: no children left in LeafNode
node4 = LeafNode(tag="span", value="example text")
print(node4)

