import unittest
import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode
from splitnode import *

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
    def test_text_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_bold(self):
        node = TextNode("stupid text here", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "stupid text here")

    def test_text_node_italic(self):
        node = TextNode("more random text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "more random text")

    def test_text_node_code(self):
        node = TextNode("more random text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "more random text")

    
    def test_text_node_image(self):
        node = TextNode("alt image text here", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIn("src", html_node.props)
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertIn("alt", html_node.props)
        self.assertEqual(html_node.props["alt"], "alt image text here")

    def test_text_node_link(self):
        node = TextNode("more random text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "more random text")
        self.assertIn("href", html_node.props)
        self.assertEqual(html_node.props["href"], "https://example.com")


    """Start tests for splitnode.py===================================================================    """       
    def test_bold(self):
        old_nodes = [
            TextNode("This is text with a **bold word** in it", TextType.TEXT),
            TextNode("This is already bold", TextType.BOLD)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        # remember to assert expectations:
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold word")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " in it")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "This is already bold")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)

    def test_italic(self):
        old_nodes = [
            TextNode("This is text with an _italic word_ in it", TextType.TEXT),
            TextNode("This is already italic", TextType.ITALIC)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "italic word")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " in it")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "This is already italic")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)
        
    def test_code(self):
        old_nodes = [
            TextNode("This is text with a `code word` in it", TextType.TEXT),
            TextNode("This is already code", TextType.CODE)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        # remember to assert expectations:
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code word")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " in it")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "This is already code")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)

    def test_non_found(self):
        old_nodes = [
            TextNode("This is text with a _italic word_ in it", TextType.TEXT),
            TextNode("This is already bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "-", TextType.IMAGE)

        self.assertNotEqual(len(new_nodes), 4)


    """Start tests for image and link extraction========================================================================"""
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches2 = extract_markdown_links(
            "This is text with a [link to a random site](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link to a random site", "https://i.imgur.com/zjjcJKZ.png")], matches2)

    def test_extract_markdown_links_not_equal(self):
        matches3 = extract_markdown_images(
            "This is text with a [link to a random site](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertNotEqual("link to a random site", "https://i.imgur.com/zjjcJKZ.png")

    """Start tests for splitting images and links======================================================================"""
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with [a link to my website](https://cameronsmusic.com).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("a link to my website", TextType.LINK, "https://cameronsmusic.com"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_links_not_split(self):
        node = TextNode(
            "This text doesn't contain any [images] and doesn't have any (image urls), but does contain a [link](https://falsepositive.com) to a fake site", 
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertNotEqual(
            [
                TextNode("This text doesn't contain any ", TextType.TEXT),
                TextNode("images", TextType.LINK, " and doesn't have any (image urls)"),
                TextNode(", but does contain a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://falsepositive.com"),
                TextNode(" to a fake site", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_links_not_image(self):
        node = TextNode(
            "This text contains a ![link](https://badlink.com) that is improperly formatted as an image",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This text contains a ![link](https://badlink.com) that is improperly formatted as an image", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "This text contains both an ![image](https://..src/image.jpg) and a [link](https://cameronsmusic.com), but I only want the image",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text contains both an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://..src/image.jpg"),
                TextNode(" and a [link](https://cameronsmusic.com), but I only want the image", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "This text contains both an ![image](https://..src/image.jpg) and a [link](https://cameronsmusic.com), but I only want the link",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text contains both an ![image](https://..src/image.jpg) and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://cameronsmusic.com"),
                TextNode(", but I only want the link", TextType.TEXT),
            ],
            new_nodes
        )



if __name__ == "__main__":
    unittest.main()
