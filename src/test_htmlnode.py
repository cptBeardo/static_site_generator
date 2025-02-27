import pytest  # Only needed for these specific tests
from htmlnode import HTMLNode, LeafNode

def test_htmlnode_defaults():
    node = HTMLNode()

    # Assert default attributes
    assert node.tag is None
    assert node.value is None
    assert node.children == []
    assert node.props == {}

def test_htmlnode_with_values():
    node = HTMLNode(tag="div", value="Hello", children=[HTMLNode(tag="span")], props={"class": "test"})

    # Assert non-default attributes
    assert node.tag == "div"
    assert node.value == "Hello"
    assert len(node.children) == 1
    assert len(node.props) == 1
    assert node.props["class"] == "test"

def test_props_to_html():
    node = HTMLNode(props={"class": "test", "id": "unique"})

    # Assert the props_to_html result
    assert node.props_to_html() == ' class="test" id="unique"'

def test_props_to_html_no_props():
    node = HTMLNode()

    # Assert empty props result in an empty string
    assert node.props_to_html() == ""

def test_repr():
    node = HTMLNode(tag="p", value="Text", children=[], props={"id": "paragraph"})
    
    # Assert the __repr__ string looks correct
    assert repr(node) == "HTMLNode contains: tag=p, value=Text, 0 children, 1 props"

def test_leaf_to_html_p():
    node = LeafNode("p", "Hello, world!")
    assert node.to_html() == "<p>Hello, world!</p>"

def test_leaf_with_no_tag():
    """Test a leaf node with no tag returns just the value."""
    node = LeafNode(None, "Just some text")
    assert node.to_html() == "Just some text"

def test_leaf_with_props():
    """Test a leaf node with attributes/props renders correctly."""
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    assert node.to_html() == '<a href="https://www.google.com">Click me!</a>'

def test_leaf_with_multiple_props():
    """Test a leaf node with multiple attributes/props renders correctly."""
    node = LeafNode("img", "", {"src": "image.jpg", "alt": "An image", "width": "500"})
    assert node.to_html() == '<img src="image.jpg" alt="An image" width="500"></img>'


# need import pytest for these specific results i.e. pytest.raises
def test_leaf_node_no_value_raises_error():
    """Test that a leaf node with no value raises a ValueError."""
    node = LeafNode("p", None)
    with pytest.raises(ValueError):
        node.to_html()

def test_leaf_node_add_child_raises_error():
    """Test that trying to add a child to a leaf node raises a ValueError."""
    node = LeafNode("p", "text")
    child = LeafNode("span", "child")
    with pytest.raises(ValueError):
        node.add_child(child)

