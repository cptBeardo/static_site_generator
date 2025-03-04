import re
from enum import Enum

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

    all_quote_lines = all(line.startswith('> ') for line in lines)
    if all_quote_lines:
        return BlockType.QUOTE
    
    if all(line.startswith('- ') for line in lines):
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





            
