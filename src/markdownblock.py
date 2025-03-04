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
