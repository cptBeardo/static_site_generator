import unittest
import re
from markdownblock import markdown_to_blocks, block_to_block_type, BlockType

"""27 tests complted"""
class TestMarkdownBlock(unittest.TestCase):

    """Start tests for markdown_to_block()==========================================================================================="""
    def test_markdown_to_block(self):
        md = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
           "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ]
        )
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

"""29 tests completed"""
class TestBlockType(unittest.TestCase):
    """Start testing for identify BlockType (29 tests currently)========================================================================"""
    def test_block_to_block_type_heading(self):
        block = "### This is the Start of my BlockType Testing"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```this is a code test```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_ol(self):
        block = """1. this is line one
2. this is line three
5. this is line three"""
        self.assertNotEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ul(self):
        block = """- Africa
- England
- Paraguay"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_quote(self):
        block = "> To be, or not to be, THAT is the question . . . "
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type(block), BlockType.PARAGRAPH)

"""34 tests completed"""


if __name__ == "__main__":
    unittest.main()