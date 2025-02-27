from htmlnode import HTMLNode

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

