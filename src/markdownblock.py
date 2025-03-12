import re
from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from splitnode import *

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")

    result_blocks = []

    for block in markdown_blocks:
        cleaned_block = block.strip()

        if cleaned_block:
            result_blocks.append(cleaned_block)

    return result_blocks

class BlockType(Enum):
    PARAGRAPH = 'paragraph' # normal text
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(mdblock: str) -> BlockType:  # :str) -> BlockType is optional and only there to show what we are expecting
    if mdblock.startswith("```") and mdblock.endswith("```"):
        return BlockType.CODE

    if mdblock.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING

    lines = mdblock.split("\n")

    all_quote_lines = all(line.startswith('>') for line in lines)
    if all_quote_lines:
        return BlockType.QUOTE
    
    if all(line.startswith(('* ', '- ', '+ ')) for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered_list = True
    for i, line in enumerate(lines):  # enumerate() returns a numbered list
        expected_start = f"{i+1}. "
        if not line.startswith(expected_start):
            is_ordered_list = False
            break   # tells the for loop to stop after finding just one false

    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)  # Split markdown into blocks
    html_blocks = []  # Process each block and collect the resulting HTML nodes
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            html_blocks.append(wrap_paragraph_block(block))
        elif block_type == BlockType.HEADING:
            html_blocks.append(wrap_heading_block(block))
        elif block_type == BlockType.CODE:
            html_blocks.append(wrap_code_block(block))
        elif block_type == BlockType.QUOTE:
            html_blocks.append(wrap_quotes_block(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_blocks.append(wrap_unordered_list_block(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_blocks.append(wrap_ordered_list_block(block))
        else:
            raise Exception("No valid BlockType")

    return ParentNode('div', html_blocks, None)

def wrap_quotes_block(text):
    lines = text.split("\n")
    quote_content = []
    
    for line in lines:
        """correct, but won't pass test"""
        if line.startswith(">"):
            line = line[1:]
            if line and line[0] == ' ':
                line = line[1:]
            quote_content.append(ParentNode('p', text_to_children(line), None))

    return ParentNode('blockquote', quote_content, None)

        """incorrect, but used to pass test"""
    #    if not line.startswith(">"):
    #        raise ValueError("invalid quote block")
    #    quote_content.append(line.lstrip(">").strip())    
    #content = "\n".join(quote_content)
    #children = text_to_children(content)

    #return ParentNode('blockquote', children, None) # change "children" back to "quote_content" if using correct and back if not

def wrap_unordered_list_block(text):
    children = wrap_list_items(text)
    return ParentNode("ul", children, None)

def wrap_ordered_list_block(text):
    children = wrap_list_items(text)
    return ParentNode("ol", children, None)

def wrap_list_items(text):
    lines = text.split("\n")
    list_item_nodes = []
    for line in lines:
        if not line.strip():
            continue
        
        text_start = line.find(" ")+1
        if text_start <= 0:
            continue

        content = line[text_start:]
        children = text_to_children(content)

        list_item_nodes.append(ParentNode("li", children, None))
        
    return list_item_nodes

def wrap_code_block(text):  # IMPORTANT: DON'T process inline markdown for code blocks!!!!
    if text.startswith("```") and text.endswith("```"): # this if block removes the leading and trailing "```" and accounts for multiple lines of code
        text = text[3:-3].strip()

    code_text = TextNode(text, TextType.TEXT)
    code_node = text_node_to_html_node(code_text)
    code_parent = ParentNode('code', [code_node], None)
    pre_parent = ParentNode('pre', [code_parent], None)
    return pre_parent

def wrap_heading_block(text):  # all good, don't touch
    level = 0
    for char in text:
        if char == '#':
            level += 1
        else:
            break
    
    level = max(1, min(6, level))
    content = text[level:].lstrip()
    children = text_to_children(content)
    return ParentNode(f"h{level}", children, None)

def wrap_paragraph_block(text): # all good, don't touch
    children = text_to_children(text)
    return ParentNode('p', children, None)

def text_to_children(text):
    # helper function to find the children for each ParentNode
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes          
