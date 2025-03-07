import unittest
import re
from markdownblock import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from main import extract_title

"""27 tests complted"""
class TestMarkdownBlock(unittest.TestCase):

    """Start tests for markdown_to_block()==========================================================================================="""
    def test_markdown_to_block(self):
        md = """# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item\n"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
           "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ]
        )
    
    def test_markdown_to_blocks(self):
        md = """\nThis is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items\n"""
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
        block = """1. this is line one\n2. this is line three\n5. this is line three"""
        self.assertNotEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ul(self):
        block = """- Africa\n- England\n- Paraguay"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_quote(self):
        block = "> To be, or not to be, THAT is the question . . . "
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type(block), BlockType.PARAGRAPH)

"""34 tests completed"""
class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph_with_formatting(self):
        # Input markdown with a paragraph containing formatted text
        markdown_input = "This is a paragraph with **bold** and _italic_ formatting."
        
        # Get the HTML node from your function
        html_node = markdown_to_html_node(markdown_input)
        
        # Convert the node to HTML string
        actual_html = html_node.to_html()
        
        # The expected HTML output
        expected_html = "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> formatting.</p></div>"
        
        # Assert that the actual output matches the expected output
        self.assertEqual(actual_html, expected_html)

    def test_paragraph_with_formatting2(self):
        markdown_input = "This is another paragraph with **bold**, *italic*, and `code` formatting."
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = "<div><p>This is another paragraph with <b>bold</b>, <i>italic</i>, and <code>code</code> formatting.</p></div>"
        self.assertEqual(actual_html, expected_html)

    def test_heading_1(self):
        markdown_input = "# Heading Level 1"
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = "<div><h1>Heading Level 1</h1></div>"
        self.assertEqual(actual_html, expected_html)
    
    def test_heading_3(self):
        markdown_input = "### Heading Level 3"
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = "<div><h3>Heading Level 3</h3></div>"
        self.assertEqual(actual_html, expected_html)
    
    def test_heading_6(self):
        markdown_input = "###### Heading Level 6"
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = "<div><h6>Heading Level 6</h6></div>"
        self.assertEqual(actual_html, expected_html)

    def test_code_block(self):
        markdown_input = """```\nfunction example() {\n  return "This is a code block";\n  // No _italic_ or **bold** processing should happen here\n}\n```\n\n"""     
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = """<div><pre><code>function example() {\n  return "This is a code block";\n  // No _italic_ or **bold** processing should happen here\n}</code></pre></div>"""
        self.assertEqual(actual_html, expected_html) 

    def test_quote_block(self):
        markdown_input = """> This is a blockquote\n> It can span multiple lines\n> And can contain **formatting**"""
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = """<div><blockquote><p>This is a blockquote</p><p>It can span multiple lines</p><p>And can contain <b>formatting</b></p></blockquote></div>"""
        self.assertEqual(actual_html, expected_html)
        print(actual_html)

    def test_unordered_list(self):
        markdown_input = """* Item 1\n* Item 2 with **bold**\n* Item 3 with *italic*"""
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = """<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b></li><li>Item 3 with <i>italic</i></li></ul></div>"""
        self.assertEqual(actual_html, expected_html)

    def test_ordered_list(self):
        markdown_input = """1. First item\n2. Second item with **bold**\n3. Third item with _italic_"""
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = """<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ol></div>"""
        self.assertEqual(actual_html, expected_html)

    def test_multiple_items(self):
        markdown_input = """# Document Title\n\nThis is a paragraph with **bold** and *italic* text.\n\n## Section 1\n\n* List item 1\n* List item 2\n\n> Important quote here\n> With multiple lines"""
        html_node = markdown_to_html_node(markdown_input)
        actual_html = html_node.to_html()
        expected_html = """<div><h1>Document Title</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Section 1</h2><ul><li>List item 1</li><li>List item 2</li></ul><blockquote><p>Important quote here</p><p>With multiple lines</p></blockquote></div>"""
        self.assertEqual(actual_html, expected_html)
        print(actual_html)

"""44 tests completed"""
class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        markdown = "# Hello, World!\n\nThis is a test."
        self.assertEqual(extract_title(markdown), "Hello, World!")
    
    def test_title_with_leading_trailing_spaces(self):
        markdown = "#    Spaces Galore    \n\nThis is a test."
        self.assertEqual(extract_title(markdown), "Spaces Galore")

    def test_no_title(self):
        markdown = "This is a test with no title."
        with self.assertRaises(Exception):
            extract_title(markdown)

    # DEBUGGING ExctractTitle def test_no_title_2(self):  --->  Cannot Use this, it is incorrect!
    # DEBUGGING ExctractTitle     markdown = "This is a test with no title."
    # DEBUGGING ExctractTitle     self.assertEqual(extract_title(markdown), "No h1 header found in markdown")

    def test_multiple_titles(self):
        markdown = "# First Title\n\n## Second Title\n\n# Another First Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_full_markdown(self):
        markdown = """# This is a heading\n\nThis is a paragraph with some text.\n\n## This is a subheading\n\n- This is a list item\n- Another list item\n\n> This is a blockquote"""
        self.assertEqual(extract_title(markdown), "This is a heading")

"""49 tests completed"""


if __name__ == "__main__":
    unittest.main()