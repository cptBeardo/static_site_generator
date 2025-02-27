import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
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
        

if __name__ == "__main__":
    unittest.main()
