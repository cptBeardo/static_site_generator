import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    """Start initial TestTextNode tests============================================================="""
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_textnoteq(self):
        node = TextNode("Random text herer", TextType.BOLD)
        node2 = TextNode("Different Text Here", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_inequality(self):  # If you want to test that two nodes with different URLs are not equal, you would use assertNotEqual:
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_url_default(self):  # If you want to test that the URL default value is correctly set to None:
        node = TextNode("Some text", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_url_assignment(self):  # If you want to test that a URL can be properly assigned and retrieved:
        url = "https://example.com"
        node = TextNode("Link text", TextType.LINK, url)
        self.assertEqual(node.url, url)

    """Start tests for TextNode to HTMLNode======================================================"""
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("stupid text here", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "stupid text here")

    def test_italic(self):
        node = TextNode("more random text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "more random text")

    def test_code(self):
        node = TextNode("more random text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "more random text")

    
    def test_image(self):
        node = TextNode("alt image text here", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIn("src", html_node.props)
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertIn("alt", html_node.props)
        self.assertEqual(html_node.props["alt"], "alt image text here")

    def test_link(self):
        node = TextNode("more random text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "more random text")
        self.assertIn("href", html_node.props)
        self.assertEqual(html_node.props["href"], "https://example.com")
                

if __name__ == "__main__":
    unittest.main()
